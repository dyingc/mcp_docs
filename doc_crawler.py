#!/usr/bin/env python3
"""
Documentation Crawler for llms.txt
Crawls documentation sites and converts them to markdown files for LLM consumption.
Uses configuration files for flexible site management.
"""

import requests
from bs4 import BeautifulSoup
import os
import re
import time
import urllib.parse
from pathlib import Path
import json
import yaml
from typing import Set, List, Dict, Optional
import html2text
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from openrouter_client import get_llm
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from collections import deque

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
        self.saved_file_count = 0
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

        # Configure html2text for better markdown conversion
        self.h = html2text.HTML2Text()
        self.h.ignore_links = config['output'].get('ignore_links', False)
        self.h.ignore_images = config['output'].get('ignore_images', False)
        self.h.ignore_emphasis = False
        self.h.body_width = 0  # Don't wrap lines

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

    def is_valid_url(self, url: str) -> bool:
        """Check if URL is valid for crawling."""
        print(f"Checking validity of URL: {url}")
        parsed = urllib.parse.urlparse(url)

        # Only crawl URLs from allowed domains
        allowed_domains = self.config['site'].get('allowed_domains', [self.domain])
        if parsed.netloc not in allowed_domains:
            print(f"URL {url} is not in allowed domains: {allowed_domains}")
            return False

        # Skip certain file types
        skip_extensions = set(self.config['crawling'].get('skip_extensions', [
            '.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.svg', '.ico'
        ]))
        if any(url.lower().endswith(ext) for ext in skip_extensions):
            print(f"URL {url} ends with a skipped extension: {skip_extensions}")
            return False

        # Skip URLs matching exclude patterns
        exclude_patterns = self.config['crawling'].get('exclude_patterns', [])
        for pattern in exclude_patterns:
            if re.search(pattern, url):
                print(f"URL {url} matches exclude pattern: {pattern}")
                return False

        # Only include URLs matching include patterns (if specified)
        include_patterns = self.config['crawling'].get('include_patterns', [])
        if include_patterns:
            if not any(re.search(pattern, url) for pattern in include_patterns):
                print(f"URL {url} does not match any include patterns: {include_patterns}")
                return False

        # Skip anchor links to same page
        if url in self.visited_urls:
            print(f"URL {url} has already been visited")
            return False

        print(f"URL {url} is valid for crawling")
        return True

    def normalize_url(self, url: str, base_url: str) -> str:
        """Normalize and resolve relative URLs."""
        # Remove fragments
        url = url.split('#')[0]

        # Resolve relative URLs
        return urllib.parse.urljoin(base_url, url)

    def extract_links(self, soup: BeautifulSoup, current_url: str) -> List[str]:
        """Extract all valid links from the page."""
        links = []

        link_selectors = self.config['site'].get('link_selectors', ['a'])

        for selector in link_selectors:
            for link in soup.select(selector):
                href = link.get('href')
                if href:
                    full_url = self.normalize_url(href, current_url)
                    if self.is_valid_url(full_url):
                        links.append(full_url)

        return links

    def clean_content(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Remove navigation, ads, and other non-content elements."""
        # Get selectors from config
        remove_selectors = self.config['site'].get('remove_selectors', [
            'nav', 'header', 'footer', '.navbar', '.nav', '.navigation',
            '.sidebar', '.menu', '.breadcrumb', '.pagination',
            '.advertisement', '.ads', '.social-share', '.comments',
            'script', 'style', 'noscript', '.search-box'
        ])

        for selector in remove_selectors:
            for element in soup.select(selector):
                element.decompose()

        return soup

    def extract_content(self, url: str) -> Dict:
        """Extract and convert page content to markdown."""
        try:
            print(f"Crawling: {url}")
            response = self.session.get(url, timeout=self.config['crawling'].get('timeout', 10))
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract title using configured selectors
            title = "Untitled"
            title_selectors = self.config['site'].get('title_selectors', ['title', 'h1'])

            for selector in title_selectors:
                element = soup.select_one(selector)
                if element:
                    title = element.get_text().strip()
                    break

            # Clean the content
            soup = self.clean_content(soup)

            # Try to find main content area using configured selectors
            content_selectors = self.config['site'].get('content_selectors', [
                'main', 'article', '.content', '.main-content', '.documentation'
            ])

            main_content = soup
            for selector in content_selectors:
                element = soup.select_one(selector)
                if element:
                    main_content = element
                    break

            # Convert to markdown
            markdown_content = self.h.handle(str(main_content))

            # Clean up the markdown
            markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)  # Remove excessive newlines
            markdown_content = markdown_content.strip()

            # Extract links for further crawling
            links = self.extract_links(soup, url)

            return {
                'url': url,
                'title': title,
                'content': markdown_content,
                'links': links,
                'success': True
            }

        except Exception as e:
            print(f"Error crawling {url}: {str(e)}")
            return {
                'url': url,
                'title': 'Error',
                'content': f"Failed to crawl: {str(e)}",
                'links': [],
                'success': False
            }

    def save_markdown_file(self, content_data: Dict):
        """Save content as a markdown file."""
        if not content_data['success'] or not content_data['content'].strip():
            return

        # Create filepath from URL
        parsed_url = urllib.parse.urlparse(content_data['url'])
        path_parts = [part for part in parsed_url.path.split('/') if part]

        relative_path = '/'.join(path_parts)
        if not relative_path:
            filepath = self.output_dir / "index.md"
        else:
            filepath = self.output_dir / f"{relative_path}.md"

        # Create directory if it doesn't exist
        filepath.parent.mkdir(parents=True, exist_ok=True)

        markdown_content = f"# {content_data['title']}\n\n"
        markdown_content += content_data['content']

        minimal_size = self.config['output'].get('minimal_size', 0)
        if len(markdown_content.encode('utf-8')) >= minimal_size:
            with self.lock:  # Acquire lock before checking and incrementing saved_file_count
                if self.stop_crawl.is_set():
                    print(f"Skipped saving {filepath} as stop signal is active.")
                    return

                if self.saved_file_count < self.max_pages:
                    self.saved_file_count += 1
                    # Write file
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                    print(f"Saved ({self.saved_file_count}/{len(self.visited_urls)}): {filepath}")

                    if self.saved_file_count >= self.max_pages:
                        self.stop_crawl.set()
                        print(f"Max pages limit ({self.max_pages}) reached. Signaling threads to stop.")
                else: # This case should ideally not be hit if stop_crawl is set promptly
                    print(f"Max pages limit reached. Skipped saving {filepath}.")
                    if not self.stop_crawl.is_set(): # Ensure stop_crawl is set if somehow missed
                        self.stop_crawl.set()
                        print("Max pages limit reached. Signaling threads to stop (redundant check).")

        else:
            print(f"Skipped: {filepath} (too small)")

    def create_llms_txt(self):
        """Create llms.txt file listing all markdown files with summaries."""
        print("\n\nCreating llms.txt index...")
        doc_prefix = self.config['output'].get('doc_prefix', 'llms')
        llms_txt_path = self.output_dir / f"{doc_prefix}_llms.txt"

        # Get all markdown files recursively
        md_files = list(self.output_dir.rglob("*.md"))

        llms_config = self.config['output'].get('llms_txt', {})

        lines = []
        tool_list = [content_metadata_tool]
        llm = get_llm().bind_tools(tool_list)

        dest_github_repo = self.config['output'].get('dest_github_repo')
        if dest_github_repo:
            dest_github_repo = dest_github_repo.replace('git@github.com:', 'https://raw.githubusercontent.com/')
            dest_github_repo = dest_github_repo.replace('.git', '')
            branch = 'main'  # Assuming main branch, adjust if needed
            raw_url_prefix = f"{dest_github_repo}/{branch}"

        for md_file in sorted(md_files):
            if md_file.name != f"{doc_prefix}_llms.txt":
                print(f"Processing: {md_file}", end='')
                relative_path = md_file.relative_to(self.output_dir)
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                title, desc = self.summarize_and_title(llm, content, md_file.name)
                if dest_github_repo:
                    raw_url = f"{raw_url_prefix}/{relative_path}"
                    lines.append(f"- [{title}]({raw_url}): {desc}")
                else:
                    lines.append(f"- [{title}]({relative_path}): {desc}")
                print(": Done")

        with open(llms_txt_path, 'w', encoding='utf-8') as f:
            f.write("# Document Index\n")
            for line in lines:
                f.write(line + '\n')

        print(f"Created {llms_txt_path.name} with {len(lines)} entries.")

    def summarize_and_title(self, llm, content, filename):
        """
        Use the LLM with tool calling to produce a title and description.
        """
        system_prompt = (
            f"You are an expert document summarizer. Call the 'content_metadata_tool' with:\n"
            f' - title: a human-readable title for the file (omit extension)\n'
            f' - description: a no_more_than_five-sentence summary suitable for indexing\n'
            f"Respond ONLY by calling the tool with the best arguments.\n"
        )
        human_prompt = (
            f"File name: {filename}\n"
            f"File content:\n<file_content>\n{content[:8000]}\n</file_content>\n"
        )
        response = llm.invoke(
            [
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]
        )

        tool_calls = getattr(response, "tool_calls", None)
        title, description = None, None
        if tool_calls:
            for call in tool_calls:
                if call.get("name") == "content_metadata_tool":
                    args = call.get("args", {})
                    title = args.get("title")
                    description = args.get("description")
                    break
        if not title:
            title = filename.rsplit('.', 1)[0].replace('_', ' ').replace('-', ' ').title()
        if not description:
            description = f"A summary for {filename}."
        return title, description

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
                        print(f"Submitting {url} for crawling. Saved: {self.saved_file_count}/{self.max_pages}")
                        futures[executor.submit(self.extract_content, url)] = url

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
                        if content_data: # Ensure content_data is not None (e.g. if task was cancelled early by stop_crawl)
                            self.scraped_content.append(content_data)
                            # save_markdown_file will check stop_crawl and might set it
                            self.save_markdown_file(content_data)

                            # Add new links to visit only if crawl is not stopped and content was successfully processed
                            if content_data['success'] and not self.stop_crawl.is_set():
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
                            elif self.stop_crawl.is_set() and content_data['success']:
                                # print(f"Stop signal active. Not adding new URLs from {url}.")
                                pass # Silently stop adding URLs
                    except Exception as e:
                        print(f"Error processing result for {url}: {e}")
                    # No finally block needed to delete future as it's popped before try

                    # Be nice to the server, but only if we are still actively crawling
                    if not self.stop_crawl.is_set():
                        time.sleep(self.delay)
                    else: # If stopping, process remaining completed futures faster
                        pass


        print(f"Crawling complete! Processed {len(self.visited_urls)} pages.")

        # Create llms.txt file
        self.create_llms_txt()

        # Save crawl summary
        summary = {
            'base_url': self.base_url,
            'pages_crawled': len(self.visited_urls),
            'successful_pages': len([c for c in self.scraped_content if c['success']]),
            'failed_pages': len([c for c in self.scraped_content if not c['success']]),
            'config_used': self.config
        }

        with open(self.output_dir / "crawl_summary.json", 'w') as f:
            json.dump(summary, f, indent=2)

def load_config(config_path: str) -> Dict:
    """Load configuration from YAML or JSON file."""
    config_file = Path(config_path)

    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_file, 'r', encoding='utf-8') as f:
        if config_path.endswith('.yaml') or config_path.endswith('.yml'):
            return yaml.safe_load(f)
        else:
            return json.load(f)

def create_sample_config(filename: str = "crawler_config.yaml"):
    """Create a sample configuration file."""
    sample_config = {
        'site': {
            'url': 'https://docs.n8n.io/',
            'name': 'n8n Documentation',
            'allowed_domains': ['docs.n8n.io'],
            'start_urls': [],
            'title_selectors': ['title', 'h1', '.page-title'],
            'content_selectors': ['main', 'article', '.content', '.documentation'],
            'link_selectors': ['a[href]'],
            'remove_selectors': [
                'nav', 'header', 'footer', '.navbar', '.nav',
                '.sidebar', '.menu', '.breadcrumb', '.pagination',
                'script', 'style', 'noscript', '.search-box'
            ]
        },
        'crawling': {
            'max_pages': 10,
            'delay': 1.0,
            'timeout': 10,
            'num_threads': 10,
            'headers': {
                'User-Agent': 'Mozilla/5.0 (compatible; DocCrawler/1.0; +https://example.com/bot)'
            },
            'skip_extensions': ['.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.svg', '.ico', '.json', '.xml', '.yaml'],
            'exclude_patterns': [
                r'/api/',
                r'/search',
                r'\.xml$',
                r'/login',
                r'/logout'
            ],
            'include_patterns': []
        },
        'output': {
            'directory': 'docs_output/n8n',
            'minimal_size': 1024,
            'doc_prefix': 'n8n',
            'ignore_links': False,
            'ignore_images': False,
            'dest_github_repo': 'git@github.com:dyingc/mcp_docs.git',
            'frontmatter': {
                'source': 'n8n-docs',
                'crawled_date': '2024-01-01'
            },
            'llms_txt': {
                'title': 'n8n Documentation',
                'description': 'Complete n8n documentation for AI assistance',
                'include_urls': True
            }
        }
    }

    with open(filename, 'w', encoding='utf-8') as f:
        yaml.dump(sample_config, f, default_flow_style=False, indent=2)

    print(f"Created sample config file: {filename}")
    return filename

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
