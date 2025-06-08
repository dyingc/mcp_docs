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

class DocCrawler:
    def __init__(self, config: Dict):
        self.config = config
        self.base_url = config['site']['url'].rstrip('/')
        self.domain = urllib.parse.urlparse(self.base_url).netloc
        self.output_dir = Path(config['output']['directory'])
        self.output_dir.mkdir(exist_ok=True)
        self.delay = config['crawling']['delay']
        self.max_pages = config['crawling']['max_pages']
        self.visited_urls: Set[str] = set()
        self.scraped_content: List[Dict] = []
        
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

    def is_valid_url(self, url: str) -> bool:
        """Check if URL is valid for crawling."""
        parsed = urllib.parse.urlparse(url)
        
        # Only crawl URLs from allowed domains
        allowed_domains = self.config['site'].get('allowed_domains', [self.domain])
        if parsed.netloc not in allowed_domains:
            return False
            
        # Skip certain file types
        skip_extensions = set(self.config['crawling'].get('skip_extensions', [
            '.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.svg', '.ico'
        ]))
        if any(url.lower().endswith(ext) for ext in skip_extensions):
            return False
            
        # Skip URLs matching exclude patterns
        exclude_patterns = self.config['crawling'].get('exclude_patterns', [])
        for pattern in exclude_patterns:
            if re.search(pattern, url):
                return False
                
        # Only include URLs matching include patterns (if specified)
        include_patterns = self.config['crawling'].get('include_patterns', [])
        if include_patterns:
            if not any(re.search(pattern, url) for pattern in include_patterns):
                return False
            
        # Skip anchor links to same page
        if url in self.visited_urls:
            return False
            
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
            
        # Create filename from URL
        parsed_url = urllib.parse.urlparse(content_data['url'])
        path_parts = [part for part in parsed_url.path.split('/') if part]
        
        if not path_parts:
            filename = "index.md"
        else:
            filename = "_".join(path_parts) + ".md"
            
        # Clean filename
        filename = re.sub(r'[^\w\-_.]', '_', filename)
        filename = re.sub(r'_+', '_', filename)
        
        filepath = self.output_dir / filename
        
        # Prepare content with metadata
        frontmatter = self.config['output'].get('frontmatter', {})
        
        markdown_content = "---\n"
        markdown_content += f"title: {content_data['title']}\n"
        markdown_content += f"url: {content_data['url']}\n"
        
        # Add custom frontmatter fields
        for key, value in frontmatter.items():
            if key not in ['title', 'url']:
                markdown_content += f"{key}: {value}\n"
                
        markdown_content += "---\n\n"
        markdown_content += f"# {content_data['title']}\n\n"
        markdown_content += content_data['content']
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
            
        print(f"Saved: {filepath}")

    def create_llms_txt(self):
        """Create llms.txt file listing all markdown files."""
        llms_txt_path = self.output_dir / "llms.txt"
        
        # Get all markdown files
        md_files = list(self.output_dir.glob("*.md"))
        
        llms_config = self.config['output'].get('llms_txt', {})
        
        with open(llms_txt_path, 'w', encoding='utf-8') as f:
            f.write(f"# {llms_config.get('title', f'Documentation for {self.domain}')}\n\n")
            f.write(f"{llms_config.get('description', f'This directory contains documentation scraped from {self.base_url}')}\n\n")
            
            if llms_config.get('include_urls', True):
                f.write(f"Source: {self.base_url}\n\n")
            
            for md_file in sorted(md_files):
                if md_file.name != "llms.txt":
                    f.write(f"{md_file.name}\n")
                    
        print(f"Created llms.txt with {len(md_files)} files")

    def crawl(self):
        """Main crawling function."""
        urls_to_visit = [self.base_url]
        pages_crawled = 0
        
        # Add additional start URLs if configured
        start_urls = self.config['site'].get('start_urls', [])
        urls_to_visit.extend(start_urls)
        
        while urls_to_visit and pages_crawled < self.max_pages:
            current_url = urls_to_visit.pop(0)
            
            if current_url in self.visited_urls:
                continue
                
            self.visited_urls.add(current_url)
            
            # Extract content
            content_data = self.extract_content(current_url)
            self.scraped_content.append(content_data)
            
            # Save as markdown file
            self.save_markdown_file(content_data)
            
            # Add new links to visit
            if content_data['success']:
                for link in content_data['links']:
                    if link not in self.visited_urls and link not in urls_to_visit:
                        urls_to_visit.append(link)
            
            pages_crawled += 1
            
            # Be nice to the server
            time.sleep(self.delay)
            
        print(f"\nCrawling complete! Processed {pages_crawled} pages.")
        
        # Create llms.txt file
        self.create_llms_txt()
        
        # Save crawl summary
        summary = {
            'base_url': self.base_url,
            'pages_crawled': pages_crawled,
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
            'headers': {
                'User-Agent': 'Mozilla/5.0 (compatible; DocCrawler/1.0; +https://example.com/bot)'
            },
            'skip_extensions': ['.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.svg', '.ico'],
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
            'directory': 'docs_output',
            'ignore_links': False,
            'ignore_images': False,
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