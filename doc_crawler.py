#!/usr/bin/env python3
"""
Documentation Crawler for llms.txt
Crawls documentation sites and converts them to markdown files for LLM consumption.
Uses configuration files for flexible site management.
"""

import requests
import re
import time
import urllib.parse
from pathlib import Path
import json
from typing import Set, List, Dict, Optional
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from openrouter_client import get_llm
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from collections import deque
from config_manager import load_config, create_sample_config
from html_processor import HtmlProcessor
from output_manager import OutputManager # Added import
import os
from urllib.parse import urljoin
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
import logging

logger = logging.getLogger(__name__)

@tool("content_metadata_tool")
def content_metadata_tool(title: str, description: str) -> str:
    """
    Generate a human-readable title and a concise 1-sentence description for a content item.
    Args:
        title: A suitable human-readable title for the file (omit extension).
        description: A concise 1-sentence summary for use in a document index or LLM retrieval.
    Returns:
        String "OK" (output is ignored; tool parameters are what matter for extraction).
    """
    return "OK"

class DocSpider(Spider):
    name = 'doc_spider'

    def __init__(self, start_urls=None, allowed_domains=None, url_prefix=None,
                 content_selectors=None, link_selectors=None, remove_selectors=None,
                 title_selectors=None, exclude_patterns=None, include_patterns=None,
                 skip_extensions=None, file_extensions=None, max_depth=None,
                 max_pages=None, delay=None, timeout=None, headers=None,
                 output_manager=None, *args, **kwargs):
        super(DocSpider, self).__init__(*args, **kwargs)
        self.start_urls = start_urls or []
        self.allowed_domains = allowed_domains or []
        self.url_prefix = url_prefix
        self.content_selectors = content_selectors or []
        self.link_selectors = link_selectors or []
        self.remove_selectors = remove_selectors or []
        self.title_selectors = title_selectors or []
        self.exclude_patterns = exclude_patterns or []
        self.include_patterns = include_patterns or []
        self.skip_extensions = skip_extensions or []
        self.file_extensions = file_extensions or []
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.delay = delay
        self.timeout = timeout
        self.headers = headers or {}
        self.output_manager = output_manager
        self.visited_urls = set()
        self.pages_crawled = 0
        self.lock = threading.Lock()
        self.stop_crawl = threading.Event()
        # Get html_processor from output_manager
        self.html_processor = output_manager.html_processor if output_manager else None

    def parse(self, response):
        if self.pages_crawled >= self.max_pages and self.max_pages != -1:
            return

        self.pages_crawled += 1
        current_url = response.url

        if current_url in self.visited_urls:
            return
        self.visited_urls.add(current_url)

        # Use HtmlProcessor to clean and extract content and links
        html = response.text
        if self.html_processor:
            processed = self.html_processor.parse_and_extract_html_content(
                html, current_url, self.visited_urls
            )
            content = processed['content']
            title = processed['title']
            links = processed['links']
        else:
            content = html
            title = current_url.split('/')[-1] or 'index'
            links = []

        # Save content
        if content:
            self.logger.info(f"Extracted content from {current_url}")
            content_data = {
                'url': current_url,
                'title': title,
                'content': content,
                'success': True,
                'depth': response.meta.get('depth', 0)
            }
            self.output_manager.save_markdown_file(
                content_data=content_data,
                lock=self.lock,
                stop_crawl_event=self.stop_crawl,
                current_visited_count=len(self.visited_urls),
                thread_name=threading.current_thread().name
            )
        else:
            self.logger.warning(f"No content extracted from {current_url}")

        # Use HtmlProcessor.extract_links for recursion
        for link in links:
            if link not in self.visited_urls:
                self.logger.info(f"Following link: {link}")
                yield response.follow(link, self.parse)

    def _should_follow_link(self, url):
        # Check if URL matches prefix
        if self.url_prefix and not url.startswith(self.url_prefix):
            return False

        # Check if URL matches include/exclude patterns
        for pattern in self.exclude_patterns:
            if re.search(pattern, url):
                return False

        if self.include_patterns:
            matches_include = False
            for pattern in self.include_patterns:
                if re.search(pattern, url):
                    matches_include = True
                    break
            if not matches_include:
                return False

        # Check file extensions
        if self.skip_extensions:
            ext = os.path.splitext(url)[1].lower()
            if ext in self.skip_extensions:
                return False

        if self.file_extensions:
            ext = os.path.splitext(url)[1].lower()
            if ext not in self.file_extensions:
                return False

        return True

class DocCrawler:
    def __init__(self, config: Dict):
        self.config = config
        self.base_url = config['site']['url'].rstrip('/')
        self.domain = urllib.parse.urlparse(self.base_url).netloc
        self.output_dir = Path(config['output']['directory'])
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay = config['crawling']['delay']
        self.max_pages = config['crawling']['max_pages']
        self.max_depth = config['crawling'].get('max_depth', 1)
        self.url_prefix = config.get('link_processing', {}).get('url_prefix', '')
        if not self.url_prefix:
            # Set default prefix based on base URL
            parsed_url = urllib.parse.urlparse(self.base_url)
            path_parts = parsed_url.path.split('/')
            if len(path_parts) > 1:
                self.url_prefix = f"{parsed_url.scheme}://{parsed_url.netloc}{'/'.join(path_parts[:-1])}"
            else:
                self.url_prefix = self.base_url
        # Normalize URL prefix by removing trailing slash
        self.url_prefix = self.url_prefix.rstrip('/')
        self.num_threads = config['crawling'].get('num_threads', 10)
        self.llm_concurrency = config['output'].get('llm_concurrency', 1)
        self.visited_urls: Set[str] = set()
        self.url_depths: Dict[str, int] = {}  # Track depth for each URL
        self.scraped_content: List[Dict] = []
        self.urls_to_visit = deque([(self.base_url, 0)])  # (url, depth) pairs
        self.lock = threading.Lock()  # Lock for thread safety
        self.stop_crawl = threading.Event()  # Event to signal stopping the crawl

        # GitHub specific settings
        self.is_github = self._is_github_domain(self.domain)
        if self.is_github:
            self.github_owner = None
            self.github_repo = None
            self.github_branch = 'main'  # Default branch
            self._parse_github_url(self.base_url)

        # Update allowed domains to include the base domain
        allowed_domains = set(config['site'].get('allowed_domains', []))
        allowed_domains.add(self.domain)
        self.allowed_domains = list(allowed_domains)

        # Instantiate HtmlProcessor
        self.html_processor = HtmlProcessor(
            site_config=config['site'],
            crawling_config=config['crawling'],
            output_config=config['output'],
            base_domain=self.domain
        )

        # Instantiate OutputManager
        self.output_manager = OutputManager(
            output_config=config['output'],
            output_dir=self.output_dir,
            max_pages=self.max_pages,
            content_metadata_tool_func=content_metadata_tool,
            get_llm_func=get_llm
        )
        # Set html_processor in output_manager
        self.output_manager.html_processor = self.html_processor

        # Session for connection reuse
        self.session = requests.Session()
        self.session.headers.update(config['crawling'].get('headers', {
            'User-Agent': 'Mozilla/5.0 (compatible; DocCrawler/1.0; +https://example.com/bot)'
        }))

        # Add additional start URLs if configured
        start_urls = self.config['site'].get('start_urls', [])
        for url in start_urls:
            self.urls_to_visit.append((url, 0))

        print(f"Initialized crawler with base URL: {self.base_url}")
        print(f"Output directory: {self.output_dir}")
        print(f"Number of threads: {self.num_threads}")
        print(f"Max depth: {self.max_depth}")
        print(f"URL prefix: {self.url_prefix}")
        print(f"LLM concurrency: {self.llm_concurrency}")
        print(f"Allowed domains: {self.allowed_domains}")
        if self.is_github:
            print(f"GitHub mode enabled for {self.github_owner}/{self.github_repo}")

    def _parse_github_url(self, url: str) -> None:
        """Parse GitHub URL to extract owner and repo."""
        parsed_url = urllib.parse.urlparse(url)
        path_parts = [p for p in parsed_url.path.split('/') if p]
        if len(path_parts) >= 2:
            self.github_owner = path_parts[0]
            self.github_repo = path_parts[1]
        else:
            raise ValueError(f"Invalid GitHub URL format: {url}")

    def _is_github_domain(self, domain: str) -> bool:
        """Check if the domain is a GitHub domain."""
        return domain in ['github.com', 'raw.githubusercontent.com']

    def _is_github_url(self, url: str) -> bool:
        """Check if URL is a GitHub URL."""
        parsed_url = urllib.parse.urlparse(url)
        return self._is_github_domain(parsed_url.netloc)

    def _is_github_file_url(self, url: str) -> bool:
        """Check if URL is a GitHub file URL."""
        if not self._is_github_url(url):
            return False
        parsed_url = urllib.parse.urlparse(url)
        path_parts = parsed_url.path.split('/')
        return len(path_parts) >= 5 and path_parts[3] == 'blob'

    def _is_github_tree_url(self, url: str) -> bool:
        """Check if URL is a GitHub tree/directory URL."""
        if not self._is_github_url(url):
            return False
        parsed_url = urllib.parse.urlparse(url)
        path_parts = parsed_url.path.split('/')
        return len(path_parts) >= 4 and path_parts[3] == 'tree'

    def _get_github_raw_url(self, file_url: str) -> str:
        """
        Convert a GitHub repository file page URL to a raw content URL.
        Example:
        https://github.com/org/repo/blob/main/xxx/yyy.md
        -> https://raw.githubusercontent.com/org/repo/refs/heads/main/xxx/yyy.md
        """
        if not self.is_github or not self.github_owner or not self.github_repo:
            return file_url

        # Parse the blob path
        parsed_url = urllib.parse.urlparse(file_url)
        path_parts = [p for p in parsed_url.path.split('/') if p]
        # Structure: /org/repo/blob/branch/path/to/file
        if len(path_parts) >= 5 and path_parts[2] == 'blob':
            branch = path_parts[3]
            file_path = '/'.join(path_parts[4:])
            # Note: branch must be prefixed with refs/heads/
            return f"https://raw.githubusercontent.com/{self.github_owner}/{self.github_repo}/refs/heads/{branch}/{file_path}"
        else:
            # Fallback
            return file_url

    def _get_github_file_path(self, url: str) -> Optional[str]:
        """Extract file path from GitHub URL."""
        if not self._is_github_file_url(url):
            return None
        parsed_url = urllib.parse.urlparse(url)
        path_parts = parsed_url.path.split('/')
        if len(path_parts) >= 5:
            return '/'.join(path_parts[4:])
        return None

    def _normalize_url(self, url: str) -> str:
        """
        Normalize URL for comparison by:
        1. Removing trailing slash
        2. Ensuring consistent scheme (http vs https)
        3. Removing any query parameters or fragments
        """
        parsed = urllib.parse.urlparse(url)
        # Reconstruct URL without trailing slash, query, or fragment
        normalized = urllib.parse.urlunparse((
            parsed.scheme,
            parsed.netloc,
            parsed.path.rstrip('/'),
            '',
            '',
            ''
        ))
        return normalized

    def _url_matches_prefix(self, url: str) -> bool:
        """
        Check if URL matches the prefix, handling various URL formats.
        """
        normalized_url = self._normalize_url(url)
        normalized_prefix = self._normalize_url(self.url_prefix)
        return normalized_url.startswith(normalized_prefix)

    def should_crawl_url(self, url: str, depth: int) -> bool:
        """Check if a URL should be crawled based on depth and prefix rules."""
        if self.max_depth != -1 and depth > self.max_depth:
            return False

        parsed_url = urllib.parse.urlparse(url)
        if parsed_url.netloc not in self.allowed_domains:
            return False

        # For the initial URL (depth 0), don't apply url_prefix restriction
        if depth == 0:
            return True

        if self.is_github:
            # For GitHub, check if it's a file URL and has allowed extension
            if self._is_github_file_url(url):
                file_path = self._get_github_file_path(url)
                if file_path:
                    ext = os.path.splitext(file_path)[1].lower()
                    return ext in self.config['crawling'].get('file_extensions', [])
            # For directory URLs or root URL, check if they match the prefix
            return self._url_matches_prefix(url)
        else:
            # For regular websites, just check the prefix
            return self._url_matches_prefix(url)

    def extract_content(self, url: str, depth: int, delay: float) -> Dict:
        """Fetch page content and use HtmlProcessor to extract and convert it."""
        try:
            print(f"Crawling: {url} (depth: {depth})")
            time.sleep(delay)

            if self.is_github and self._is_github_file_url(url):
                raw_url = self._get_github_raw_url(url)
                response = self.session.get(raw_url, timeout=self.config['crawling'].get('timeout', 10))
                response.raise_for_status()
                content = response.text
                title = os.path.basename(url)
                return {
                    'url': url,
                    'title': title,
                    'content': content,
                    'links': [],  # Raw files don't have links
                    'depth': depth,
                    'success': True,
                    'thread_name': threading.current_thread().name
                }
            else:
                # Regular website or GitHub directory
                response = self.session.get(url, timeout=self.config['crawling'].get('timeout', 10))
                response.raise_for_status()
                processed_data = self.html_processor.parse_and_extract_html_content(
                    response.text, url, self.visited_urls
                )
                return {
                    'url': url,
                    'title': processed_data['title'],
                    'content': processed_data['content'],
                    'links': processed_data['links'],
                    'depth': depth,
                    'success': True,
                    'thread_name': threading.current_thread().name
                }
        except requests.exceptions.RequestException as e:
            print(f"Request error crawling {url}: {str(e)}")
            return {
                'url': url,
                'title': 'Request Error',
                'content': f"Failed to fetch page: {str(e)}",
                'links': [],
                'depth': depth,
                'success': False
            }
        except Exception as e:
            import traceback
            print(f"Error processing content for {url}: {str(e)}")
            print("Full traceback:")
            print(traceback.format_exc())
            return {
                'url': url,
                'title': 'Error',
                'content': f"Failed to crawl: {str(e)}",
                'depth': depth,
                'success': False
            }

    # Methods save_markdown_file, create_llms_txt, summarize_and_title are moved to OutputManager

    def _get_start_urls(self) -> List[str]:
        """Get the list of start URLs for crawling."""
        start_urls = set()

        # Always add the site URL as the first start URL
        if self.base_url:
            start_urls.add(self.base_url)

        # Add any additional start URLs from config
        config_start_urls = self.config.get('site', {}).get('start_urls', [])
        start_urls.update(config_start_urls)

        return list(start_urls)

    def crawl_site(self):
        """Crawl the site and save the content."""
        try:
            # Get start URLs
            self.start_urls = self._get_start_urls()
            if not self.start_urls:
                raise ValueError("No start URLs configured")

            # Get allowed domains
            self.allowed_domains = self._get_allowed_domains()

            # Get selectors and patterns from config
            self.content_selectors = self.config['site'].get('content_selectors', [])
            self.link_selectors = self.config['site'].get('link_selectors', [])
            self.remove_selectors = self.config['site'].get('remove_selectors', [])
            self.title_selectors = self.config['site'].get('title_selectors', [])
            self.exclude_patterns = self.config['site'].get('exclude_patterns', [])
            self.include_patterns = self.config['site'].get('include_patterns', [])
            self.skip_extensions = self.config['crawling'].get('skip_extensions', [])
            self.file_extensions = self.config['crawling'].get('file_extensions', [])
            self.timeout = self.config['crawling'].get('timeout', 10)
            self.headers = self.config['crawling'].get('headers', {})

            # Initialize the crawler
            self.crawler = CrawlerProcess(self._get_crawler_settings())

            # Add the crawler to the process
            self.crawler.crawl(
                DocSpider,
                start_urls=self.start_urls,
                allowed_domains=self.allowed_domains,
                url_prefix=self.url_prefix,
                content_selectors=self.content_selectors,
                link_selectors=self.link_selectors,
                remove_selectors=self.remove_selectors,
                title_selectors=self.title_selectors,
                exclude_patterns=self.exclude_patterns,
                include_patterns=self.include_patterns,
                skip_extensions=self.skip_extensions,
                file_extensions=self.file_extensions,
                max_depth=self.max_depth,
                max_pages=self.max_pages,
                delay=self.delay,
                timeout=self.timeout,
                headers=self.headers,
                output_manager=self.output_manager
            )

            # Start the crawler
            self.crawler.start()

        except Exception as e:
            logger.error(f"Error during crawling: {e}")
            raise

    def crawl(self):
        """Controls crawl plus post-crawl output generation."""
        # Use config flag to control actual crawling
        do_crawl = self.config.get('crawling', {}).get('crawl', True)
        if do_crawl:
            self.crawl_site()
        else:
            print("Skipping crawling stage due to crawling:crawl = false in config.")
        # Only output llms.txt if enabled
        if self.config.get('output', {}).get('output_llms_txt', False):
            self.output_manager.create_llms_txt()
        successful_pages_count = len([c for c in self.scraped_content if c.get('success')])
        failed_pages_count = len(self.scraped_content) - successful_pages_count
        self.output_manager.save_crawl_summary(
            base_url=self.base_url,
            pages_crawled=len(self.visited_urls),
            successful_pages=successful_pages_count,
            failed_pages=failed_pages_count,
            config_used=self.config
        )

    def _get_allowed_domains(self) -> List[str]:
        """Get the list of allowed domains for crawling."""
        allowed_domains = set()

        # Add the domain from url_prefix if it exists
        if self.url_prefix:
            try:
                url_prefix_domain = urlparse(self.url_prefix).netloc
                if url_prefix_domain:
                    allowed_domains.add(url_prefix_domain)
            except Exception as e:
                logger.warning(f"Failed to parse url_prefix domain: {e}")

        # Add the domain from the site URL
        try:
            site_domain = urlparse(self.base_url).netloc
            if site_domain:
                allowed_domains.add(site_domain)
        except Exception as e:
            logger.warning(f"Failed to parse site_url domain: {e}")

        # If the site URL is from GitHub, add GitHub raw domain
        if 'github.com' in allowed_domains:
            allowed_domains.add('raw.githubusercontent.com')

        # Add any extra allowed domains from config
        extra_domains = self.config.get('site', {}).get('allowed_domains', [])
        allowed_domains.update(extra_domains)

        return list(allowed_domains)

    def _get_crawler_settings(self) -> Dict:
        """Get Scrapy crawler settings from config."""
        settings = {
            'USER_AGENT': self.config['crawling'].get('headers', {}).get('User-Agent', 'Mozilla/5.0'),
            'DOWNLOAD_DELAY': self.delay,
            'CONCURRENT_REQUESTS': self.num_threads,
            'DOWNLOAD_TIMEOUT': self.config['crawling'].get('timeout', 10),
            'LOG_LEVEL': 'INFO',
            'COOKIES_ENABLED': False,
            'ROBOTSTXT_OBEY': True,
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            }
        }
        return settings

    def _is_allowed_url(self, url: str) -> bool:
        """Check if a URL is allowed to be crawled based on domain restrictions."""
        try:
            parsed_url = urlparse(url)
            url_domain = parsed_url.netloc

            # Always allow the initial URL
            if url == self.base_url:
                return True

            # Check if the URL is from an allowed domain
            return url_domain in self.allowed_domains
        except Exception as e:
            logger.warning(f"Failed to check if URL is allowed: {e}")
            return False

# Removed load_config and create_sample_config functions as they are now in config_manager.py

def main():
    parser = argparse.ArgumentParser(description='Crawl documentation sites for LLM consumption')
    parser.add_argument('--config', '-c', help='Configuration file path')
    parser.add_argument('--create-config', action='store_true', help='Create a sample configuration file')
    parser.add_argument('--config-name', default='crawler_config.yaml', help='Name for the sample config file')

    args = parser.parse_args()

    if args.create_config:
        create_sample_config(args.config_name)
        return

    if not args.config:
        print("Error: Please provide a config file with --config or create one with --create-config")
        print("\nExample usage:")
        print("  python doc_crawler.py --create-config")
        print("  python doc_crawler.py --config crawler_config.yaml")
        return

    required_packages = ['requests', 'beautifulsoup4', 'html2text', 'pyyaml']
    print("Required packages:", ', '.join(required_packages))
    print("Install with: pip install", ' '.join(required_packages))
    print()

    try:
        config = load_config(args.config)
        crawler = DocCrawler(config)
        crawler.crawl()
    except Exception as e:
        import traceback
        print("Full traceback:")
        print(traceback.format_exc())
        # print(f"Error: {e}")

if __name__ == "__main__":
    main()
