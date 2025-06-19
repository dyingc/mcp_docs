#!/usr/bin/env python3
"""
Documentation Crawler for llms.txt
Crawls documentation sites and converts them to markdown files for LLM consumption.
Uses configuration files for flexible site management.
"""

import requests
import re
import time
import os
import json
import logging
import threading
import argparse
from pathlib import Path
from typing import Set, List, Dict, Optional
from collections import deque
from urllib.parse import urljoin, urlparse, urlunparse

from openrouter_client import get_llm
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage

from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider

from config_manager import load_config, create_sample_config
from html_processor import HtmlProcessor
from output_manager import OutputManager

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

class GitHubUrlHelper:
    """
    Utility class for all GitHub URL inspection and transform logic.
    """
    def __init__(self, base_url: str):
        self.owner = None
        self.repo = None
        self.branch = 'main'
        self.base_url = base_url
        self._parse_github_url(base_url)

    def is_github_domain(self, domain: str) -> bool:
        return domain in ['github.com', 'raw.githubusercontent.com']

    def is_github_url(self, url: str) -> bool:
        parsed = urlparse(url)
        return self.is_github_domain(parsed.netloc)

    def is_github_file_url(self, url: str) -> bool:
        if not self.is_github_url(url):
            return False
        parts = [p for p in urlparse(url).path.split('/') if p]
        return len(parts) >= 5 and parts[2] == 'blob'

    def is_github_tree_url(self, url: str) -> bool:
        if not self.is_github_url(url):
            return False
        parts = [p for p in urlparse(url).path.split('/') if p]
        return len(parts) >= 4 and parts[2] == 'tree'

    def get_github_raw_url(self, file_url: str) -> str:
        """
        Convert github.com file URL to the corresponding raw.githubusercontent.com URL.
        """
        parts = [p for p in urlparse(file_url).path.split('/') if p]
        if len(parts) >= 5 and parts[2] == 'blob':
            branch = parts[3]
            file_path = '/'.join(parts[4:])
            return f"https://raw.githubusercontent.com/{self.owner}/{self.repo}/refs/heads/{branch}/{file_path}"
        return file_url

    def get_github_file_path(self, url: str) -> Optional[str]:
        if not self.is_github_file_url(url):
            return None
        parts = [p for p in urlparse(url).path.split('/') if p]
        if len(parts) >= 5:
            return '/'.join(parts[4:])
        return None

    def _parse_github_url(self, url: str) -> None:
        parsed = urlparse(url)
        parts = [p for p in parsed.path.split('/') if p]
        if len(parts) >= 2:
            self.owner = parts[0]
            self.repo = parts[1]
            if len(parts) >= 4 and parts[2] in ['blob', 'tree']:
                self.branch = parts[3]

class DocSpider(Spider):
    name = 'doc_spider'

    def __init__(
        self, start_urls=None, allowed_domains=None, url_prefix=None,
        content_selectors=None, link_selectors=None, remove_selectors=None,
        title_selectors=None, exclude_patterns=None, include_patterns=None,
        skip_extensions=None, file_extensions=None, max_depth=None,
        max_pages=None, delay=None, timeout=None, headers=None,
        output_manager=None, should_crawl_url=None, doc_crawler=None, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
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
        self.html_processor = output_manager.html_processor if output_manager else None
        self.should_crawl_url = should_crawl_url
        self.doc_crawler = doc_crawler

    def parse(self, response):
        with self.lock:
            if self.pages_crawled >= self.max_pages and self.max_pages != -1:
                return
            self.pages_crawled += 1
            current_url = response.url
            if current_url in self.visited_urls:
                return
            self.visited_urls.add(current_url)

        current_url = response.url
        is_github_blob = False
        is_github_tree = False
        github_helper = None
        if self.doc_crawler and self.doc_crawler.github_helper:
            github_helper = self.doc_crawler.github_helper
            is_github_blob = github_helper.is_github_file_url(current_url)
            is_github_tree = github_helper.is_github_tree_url(current_url)

        # Scrapy 官方会在 Request.meta['depth'] 维护递归深度
        depth = response.meta.get('depth', 0)

        if is_github_blob:
            extracted = self.doc_crawler.extract_content(current_url, depth, self.delay if self.delay else 0)
            content = extracted.get('content', '')
            title = extracted.get('title', os.path.basename(current_url))
            links = extracted.get('links', [])
            if content:
                logger.info(f"Extracted content from {current_url} via extract_content")
                content_data = {
                    'url': current_url,
                    'title': title,
                    'content': content,
                    'success': True,
                    'depth': depth,
                    'thread_name': threading.current_thread().name
                }
                self.output_manager.save_markdown_file(
                    content_data=content_data,
                    lock=self.lock,
                    stop_crawl_event=self.stop_crawl,
                    current_visited_count=len(self.visited_urls),
                    thread_name=threading.current_thread().name
                )
            else:
                logger.warning(f"No content extracted from {current_url}")
                if self.output_manager:
                    self.output_manager.add_failed_page(current_url)
            return

        if is_github_tree:
            logger.info(f"Processing github tree page (not saving): {current_url}")
            html = response.text
            links = []
            if self.html_processor:
                processed = self.html_processor.parse_and_extract_html_content(
                    html, current_url, self.visited_urls
                )
                links = processed['links']
            for link in links:
                # 不设置 meta，Scrapy 会自动 +1 传递 depth
                if link not in self.visited_urls and (self.should_crawl_url is None or self.should_crawl_url(link, depth+1)):
                    logger.info(f"Following link: {link}")
                    yield response.follow(link, self.parse)
            return

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

        if content:
            logger.info(f"Extracted content from {current_url}")
            content_data = {
                'url': current_url,
                'title': title,
                'content': content,
                'success': True,
                'depth': depth,
                'thread_name': threading.current_thread().name
            }
            self.output_manager.save_markdown_file(
                content_data=content_data,
                lock=self.lock,
                stop_crawl_event=self.stop_crawl,
                current_visited_count=len(self.visited_urls),
                thread_name=threading.current_thread().name
            )
        else:
            logger.warning(f"No content extracted from {current_url}")
            if self.output_manager:
                self.output_manager.add_failed_page(current_url)

        for link in links:
            if link not in self.visited_urls and (self.should_crawl_url is None or self.should_crawl_url(link, depth+1)):
                logger.info(f"Following link: {link}")
                yield response.follow(link, self.parse)

class DocCrawler:
    def __init__(self, config: Dict):
        self.config = config
        self.base_url = config['site']['url'].rstrip('/')
        self.failed_pages = 0  # Count of failed pages
        self.domain = urlparse(self.base_url).netloc
        self.output_dir = Path(config['output']['directory'])
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay = config['crawling']['delay']
        self.max_pages = config['crawling']['max_pages']
        self.max_depth = config['crawling'].get('max_depth', 1)
        self.url_prefix = config.get('link_processing', {}).get('url_prefix', '') or self.base_url
        self.url_prefix = self.url_prefix.rstrip('/')
        self.num_threads = config['crawling'].get('num_threads', 10)
        self.llm_concurrency = config['output'].get('llm_concurrency', 1)
        self.lock = threading.Lock()
        self.stop_crawl = threading.Event()
        self.is_github = 'github.com' in self.domain or 'raw.githubusercontent.com' in self.domain
        self.github_helper = GitHubUrlHelper(self.base_url) if self.is_github else None
        self.allowed_domains = self._get_allowed_domains()
        self.html_processor = HtmlProcessor(
            site_config=config['site'],
            crawling_config=config['crawling'],
            output_config=config['output'],
            base_domain=self.domain
        )
        self.output_manager = OutputManager(
            output_config=config['output'],
            output_dir=self.output_dir,
            max_pages=self.max_pages,
            content_metadata_tool_func=content_metadata_tool,
            get_llm_func=get_llm
        )
        self.output_manager.html_processor = self.html_processor
        self.session = requests.Session()
        self.session.headers.update(
            config['crawling'].get('headers', {
                'User-Agent': 'Mozilla/5.0 (compatible; DocCrawler/1.0; +https://example.com/bot)'
            })
        )
        logger.info(f"Initialized crawler with base URL: {self.base_url}")
        logger.info(f"Output directory: {self.output_dir}")
        logger.info(f"Number of threads: {self.num_threads}")
        logger.info(f"Max depth: {self.max_depth}")
        logger.info(f"URL prefix: {self.url_prefix}")
        logger.info(f"LLM concurrency: {self.llm_concurrency}")
        logger.info(f"Allowed domains: {self.allowed_domains}")
        if self.is_github:
            logger.info(f"GitHub mode enabled for {self.github_helper.owner}/{self.github_helper.repo} -> {self.github_helper.branch}")

    def _normalize_url(self, url: str) -> str:
        parsed = urlparse(url)
        return urlunparse((
            parsed.scheme,
            parsed.netloc,
            parsed.path.rstrip('/'),
            '',
            '',
            ''
        ))

    def _url_matches_prefix(self, url: str) -> bool:
        normalized_url = self._normalize_url(url)
        normalized_prefix = self._normalize_url(self.url_prefix)
        return normalized_url.startswith(normalized_prefix)

    def should_crawl_url(self, url: str, depth: int) -> bool:
        # Only apply max_depth when >=0. If max_depth < 0, allow unlimited depth.
        if self.max_depth >= 0 and depth > self.max_depth:
            return False
        parsed_url = urlparse(url)
        if parsed_url.netloc not in self.allowed_domains:
            return False
        if depth == 0:
            return True
        if self.is_github and self.github_helper:
            if self.github_helper.is_github_file_url(url):
                file_path = self.github_helper.get_github_file_path(url)
                if file_path:
                    ext = os.path.splitext(file_path)[1].lower()
                    return ext in self.config['crawling'].get('file_extensions', [])
            return self._url_matches_prefix(url)
        else:
            return self._url_matches_prefix(url)

    def extract_content(self, url: str, depth: int, delay: float) -> Dict:
        try:
            logger.info(f"Crawling: {url} (depth: {depth})")
            time.sleep(delay)
            if self.is_github and self.github_helper and self.github_helper.is_github_file_url(url):
                raw_url = self.github_helper.get_github_raw_url(url)
                response = self.session.get(raw_url, timeout=self.config['crawling'].get('timeout', 10))
                response.raise_for_status()
                content = response.text
                title = os.path.basename(url)
                return {
                    'url': url,
                    'title': title,
                    'content': content,
                    'links': [],
                    'depth': depth,
                    'success': True,
                    'thread_name': threading.current_thread().name
                }
            else:
                response = self.session.get(url, timeout=self.config['crawling'].get('timeout', 10))
                response.raise_for_status()
                processed_data = self.html_processor.parse_and_extract_html_content(
                    response.text, url, set()
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
            logger.error(f"Request error crawling {url}: {str(e)}")
            return {
                'url': url,
                'title': 'Request Error',
                'content': f"Failed to fetch page: {str(e)}",
                'links': [],
                'depth': depth,
                'success': False
            }
        except Exception as e:
            logger.error(f"Error processing content for {url}: {str(e)}", exc_info=True)
            return {
                'url': url,
                'title': 'Error',
                'content': f"Failed to crawl: {str(e)}",
                'depth': depth,
                'success': False
            }

    def _get_start_urls(self) -> List[str]:
        start_urls = set()
        if self.base_url:
            start_urls.add(self.base_url)
        config_start_urls = self.config.get('site', {}).get('start_urls', [])
        start_urls.update(config_start_urls)
        return list(start_urls)

    def crawl_site(self):
        try:
            start_urls = self._get_start_urls()
            if not start_urls:
                raise ValueError("No start URLs configured")
            allowed_domains = self._get_allowed_domains()
            self.crawler = CrawlerProcess(self._get_crawler_settings())
            self.crawler.crawl(
                DocSpider,
                start_urls=start_urls,
                allowed_domains=allowed_domains,
                url_prefix=self.url_prefix,
                content_selectors=self.config['site'].get('content_selectors', []),
                link_selectors=self.config['site'].get('link_selectors', []),
                remove_selectors=self.config['site'].get('remove_selectors', []),
                title_selectors=self.config['site'].get('title_selectors', []),
                exclude_patterns=self.config['site'].get('exclude_patterns', []),
                include_patterns=self.config['site'].get('include_patterns', []),
                skip_extensions=self.config['crawling'].get('skip_extensions', []),
                file_extensions=self.config['crawling'].get('file_extensions', []),
                max_depth=self.max_depth,
                max_pages=self.max_pages,
                delay=self.delay,
                timeout=self.config['crawling'].get('timeout', 10),
                headers=self.config['crawling'].get('headers', {}),
                output_manager=self.output_manager,
                should_crawl_url=self.should_crawl_url,
                doc_crawler=self
            )
            self.crawler.start()
        except Exception as e:
            logger.error(f"Error during crawling: {e}", exc_info=True)
            raise

    def crawl(self):
        do_crawl = self.config.get('crawling', {}).get('crawl', True)
        if do_crawl:
            self.crawl_site()
        else:
            logger.info("Skipping crawling stage due to crawling:crawl = false in config.")
        if self.config.get('output', {}).get('output_llms_txt', False):
            self.output_manager.create_llms_txt()
        self.output_manager.save_crawl_summary(
            base_url=self.base_url,
            pages_crawled=self.max_pages,
            successful_pages=self.max_pages,
            failed_pages=self.output_manager.get_failed_pages_count(),
            config_used=self.config
        )

    def _get_allowed_domains(self) -> List[str]:
        allowed_domains = set()
        if self.url_prefix:
            try:
                url_prefix_domain = urlparse(self.url_prefix).netloc
                if url_prefix_domain:
                    allowed_domains.add(url_prefix_domain)
            except Exception as e:
                logger.warning(f"Failed to parse url_prefix domain: {e}")
        try:
            site_domain = urlparse(self.base_url).netloc
            if site_domain:
                allowed_domains.add(site_domain)
        except Exception as e:
            logger.warning(f"Failed to parse site_url domain: {e}")
        if 'github.com' in allowed_domains:
            allowed_domains.add('raw.githubusercontent.com')
        extra_domains = self.config.get('site', {}).get('allowed_domains', [])
        allowed_domains.update(extra_domains)
        return list(allowed_domains)

    def _get_crawler_settings(self) -> Dict:
        return {
            'USER_AGENT': self.config['crawling'].get('headers', {}).get('User-Agent', 'Mozilla/5.0'),
            'DOWNLOAD_DELAY': self.delay,
            'CONCURRENT_REQUESTS': self.num_threads,
            'DOWNLOAD_TIMEOUT': self.config['crawling'].get('timeout', 10),
            'LOG_LEVEL': 'INFO',
            'COOKIES_ENABLED': False,
            'ROBOTSTXT_OBEY': False,
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            }
        }

    def _is_allowed_url(self, url: str) -> bool:
        try:
            parsed_url = urlparse(url)
            url_domain = parsed_url.netloc
            if url == self.base_url:
                return True
            return url_domain in self.allowed_domains
        except Exception as e:
            logger.warning(f"Failed to check if URL is allowed: {e}")
            return False

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

if __name__ == "__main__":
    main()
