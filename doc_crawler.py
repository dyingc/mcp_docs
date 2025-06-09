#!/usr/bin/env python3
"""
Documentation Crawler for llms.txt
Crawls documentation sites and converts them to markdown files for LLM consumption.
Uses configuration files for flexible site management.
"""

import requests
# from bs4 import BeautifulSoup # No longer directly used here
# import os # Appears unused
import re
import time
import urllib.parse
from pathlib import Path
import json
# import yaml # Removed, as it's now in config_manager.py
from typing import Set, List, Dict, Optional
# import html2text # No longer directly used here
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
        # self.saved_file_count = 0 # Moved to OutputManager
        self.base_url = config['site']['url'].rstrip('/')
        self.domain = urllib.parse.urlparse(self.base_url).netloc
        self.output_dir = Path(config['output']['directory'])
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay = config['crawling']['delay']
        self.max_pages = config['crawling']['max_pages']
        self.num_threads = config['crawling'].get('num_threads', 10)
        self.visited_urls: Set[str] = set()
        self.scraped_content: List[Dict] = []
        self.urls_to_visit = deque([self.base_url])
        self.lock = threading.Lock()  # Lock for thread safety
        self.stop_crawl = threading.Event()  # Event to signal stopping the crawl

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
            content_metadata_tool_func=content_metadata_tool, # Pass the function
            get_llm_func=get_llm # Pass the function
        )

        # Session for connection reuse
        self.session = requests.Session()
        self.session.headers.update(config['crawling'].get('headers', {
            'User-Agent': 'Mozilla/5.0 (compatible; DocCrawler/1.0; +https://example.com/bot)'
        }))

        # Add additional start URLs if configured
        start_urls = self.config['site'].get('start_urls', [])
        for url in start_urls:
            self.urls_to_visit.append(url)

        print(f"Initialized crawler with base URL: {self.base_url}")
        print(f"Output directory: {self.output_dir}")
        print(f"Number of threads: {self.num_threads}")

    # Methods is_valid_url, normalize_url, extract_links, clean_content are moved to HtmlProcessor

    def extract_content(self, url: str, delay: float) -> Dict:
        """Fetch page content and use HtmlProcessor to extract and convert it."""
        try:
            print(f"Crawling: {url}")
            time.sleep(delay) # Apply delay per thread before making the request
            response = self.session.get(url, timeout=self.config['crawling'].get('timeout', 10))
            response.raise_for_status() # Raise HTTPError for bad responses (4XX or 5XX)

            # Use HtmlProcessor to parse and extract content
            # Pass self.visited_urls to html_processor methods that need it for link validation
            processed_data = self.html_processor.parse_and_extract_html_content(
                response.text, url, self.visited_urls
            )

            return {
                'url': url,
                'title': processed_data['title'],
                'content': processed_data['content'],
                'links': processed_data['links'],
                'success': True,
                'thread_name': threading.current_thread().name # Add thread name
            }

        except requests.exceptions.RequestException as e: # More specific exception handling
            print(f"Request error crawling {url}: {str(e)}")
            return {
                'url': url,
                'title': 'Request Error',
                'content': f"Failed to fetch page: {str(e)}",
                'links': [],
                'success': False
            }
        except Exception as e: # Catch other potential errors during processing
            import traceback
            print(f"Error processing content for {url}: {str(e)}")
            print("Full traceback:")
            print(traceback.format_exc())
            return {
                'url': url,
                'title': 'Error',
                'content': f"Failed to crawl: {str(e)}",
                'links': [],
                'success': False
            }

    # Methods save_markdown_file, create_llms_txt, summarize_and_title are moved to OutputManager

    def crawl(self):
        """Main crawling function with multi-threading."""
        print("Starting crawl process...")
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = {}
            # Main loop: continue if there are URLs to visit or active futures, and stop_crawl is not set
            while (self.urls_to_visit or futures) and not self.stop_crawl.is_set():
                # Submit new tasks
                while len(futures) < self.num_threads and self.urls_to_visit and not self.stop_crawl.is_set():
                    url = self.urls_to_visit.popleft()
                    if url not in self.visited_urls:
                        self.visited_urls.add(url)
                        # Use output_manager's count for the print statement
                        print(f"Submitting {url} for crawling. Saved: {self.output_manager.get_saved_file_count()}/{self.max_pages}")
                        futures[executor.submit(self.extract_content, url, self.delay)] = url

                if not futures: # No active tasks, and no new tasks were submitted (e.g. urls_to_visit is empty or stop_crawl is set)
                    break

                # Process completed tasks
                for future in as_completed(list(futures.keys())): # Iterate over a copy of keys for safe deletion
                    # If stop_crawl is set, we still process the already completed futures
                    # but new tasks won't be submitted by the outer loops.
                    # Individual tasks (extract_content) will also check stop_crawl.

                    url = futures.pop(future, None) # Remove future, use None if already removed (should not happen with list(futures.keys()))
                    if url is None: # Should not happen if logic is correct
                        continue

                    try:
                        content_data = future.result()
                        if content_data: # Ensure content_data is not None
                            self.scraped_content.append(content_data)
                            # Call OutputManager to save the file
                            # It will handle saved_file_count and stop_crawl event
                            self.output_manager.save_markdown_file(
                                content_data, self.lock, self.stop_crawl, len(self.visited_urls),
                                thread_name=content_data.get('thread_name') # Pass the thread name
                            )

                            # Add new links to visit only if crawl is not stopped and content was successfully processed
                            if content_data.get('success') and not self.stop_crawl.is_set():
                                with self.lock: # Lock for accessing shared urls_to_visit and visited_urls
                                    # Double check stop_crawl inside lock, as it might be set by save_markdown_file
                                    if not self.stop_crawl.is_set():
                                        for link in content_data['links']:
                                            if link not in self.visited_urls and link not in self.urls_to_visit:
                                                self.urls_to_visit.append(link)
                                                # print(f"Added {link} to URLs to visit")
                                    else:
                                        # This print might be noisy if many threads hit this after stop_crawl is set
                                        # print("Stop signal active after saving. Not adding new URLs.")
                                        pass # Silently stop adding URLs
                            elif self.stop_crawl.is_set() and content_data.get('success'):
                                # print(f"Stop signal active. Not adding new URLs from {url}.")
                                pass # Silently stop adding URLs
                    except Exception as e:
                        print(f"Error processing result for {url}: {e}")
                    # No finally block needed to delete future as it's popped before try


        print(f"Crawling complete! Processed {len(self.visited_urls)} pages.")

        # Create llms.txt file using OutputManager
        self.output_manager.create_llms_txt()

        # Save crawl summary using OutputManager
        successful_pages_count = len([c for c in self.scraped_content if c.get('success')])
        failed_pages_count = len(self.scraped_content) - successful_pages_count # More robust count
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

    # Install required packages message
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
