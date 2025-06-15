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

    def crawl_site(self):
        """Perform only the crawling portion. Returns when crawling is complete."""
        print("Starting crawl process...")

        # Always crawl the initial page first
        print(f"Crawling initial page: {self.base_url}")
        initial_content = self.extract_content(self.base_url, 0, self.delay)
        if initial_content:
            self.scraped_content.append(initial_content)
            self.output_manager.save_markdown_file(
                initial_content, self.lock, self.stop_crawl, len(self.visited_urls),
                thread_name=initial_content.get('thread_name')
            )
            if initial_content.get('success') and not self.stop_crawl.is_set():
                with self.lock:
                    if not self.stop_crawl.is_set():
                        for link in initial_content['links']:
                            if link not in self.visited_urls and link not in [u for u, _ in self.urls_to_visit]:
                                print(f'[CRAWLER] Enqueue: {link} (depth=1)')
                                self.urls_to_visit.append((link, 1))

        # Then proceed with the rest of the crawling
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = {}
            while (self.urls_to_visit or futures) and not self.stop_crawl.is_set():
                while len(futures) < self.num_threads and self.urls_to_visit and not self.stop_crawl.is_set():
                    url, depth = self.urls_to_visit.popleft()
                    print(f'[CRAWLER] To crawl: {url} (depth={depth})')
                    if url not in self.visited_urls and self.should_crawl_url(url, depth):
                        self.visited_urls.add(url)
                        self.url_depths[url] = depth
                        print(f"Submitting {url} for crawling (depth: {depth}). Saved: {self.output_manager.get_saved_file_count()}/{self.max_pages}")
                        futures[executor.submit(self.extract_content, url, depth, self.delay)] = (url, depth)
                if not futures:
                    break
                for future in as_completed(list(futures.keys())):
                    url, depth = futures.pop(future, None)
                    if url is None:
                        continue
                    try:
                        content_data = future.result()
                        if content_data:
                            self.scraped_content.append(content_data)
                            self.output_manager.save_markdown_file(
                                content_data, self.lock, self.stop_crawl, len(self.visited_urls),
                                thread_name=content_data.get('thread_name')
                            )
                            if content_data.get('success') and not self.stop_crawl.is_set():
                                with self.lock:
                                    if not self.stop_crawl.is_set():
                                        for link in content_data['links']:
                                            if link not in self.visited_urls and link not in [u for u, _ in self.urls_to_visit]:
                                                print(f'[CRAWLER] Enqueue: {link} (depth={depth+1})')
                                                self.urls_to_visit.append((link, depth + 1))
                                    else:
                                        pass
                            elif self.stop_crawl.is_set() and content_data.get('success'):
                                pass
                    except Exception as e:
                        print(f"Error processing result for {url}: {e}")
        print(f"Crawling complete! Processed {len(self.visited_urls)} pages.")

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
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
