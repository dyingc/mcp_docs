import urllib.parse
import re
from typing import List, Dict, Set
from bs4 import BeautifulSoup
import html2text
import logging

logger = logging.getLogger(__name__)

class HtmlProcessor:
    def __init__(self, site_config: Dict, crawling_config: Dict, output_config: Dict, base_domain: str):
        self.site_config = site_config
        self.crawling_config = crawling_config
        self.output_config = output_config
        self.base_domain = base_domain

        # Configure html2text for better markdown conversion
        self.h = html2text.HTML2Text()
        self.h.ignore_links = output_config.get('ignore_links', False)
        self.h.ignore_images = output_config.get('ignore_images', False)
        self.h.ignore_emphasis = False
        self.h.body_width = 0  # Don't wrap lines
        # Ensure the instance persists by storing a reference
        self._html2text_instance = self.h

    def is_valid_url(self, url: str, visited_urls: Set[str]) -> bool:
        """Check if URL is valid for crawling."""
        parsed = urllib.parse.urlparse(url)

        # Allow empty netloc (relative links), or netloc in allowed_domains/base_domain/www.base_domain
        allowed_domains = set(self.site_config.get('allowed_domains', []))
        allowed_domains.add(self.base_domain)
        allowed_domains.add('www.' + self.base_domain)
        if parsed.netloc and parsed.netloc not in allowed_domains:
            return False

        # Skip certain file types
        skip_extensions = set(self.crawling_config.get('skip_extensions', [
            '.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.svg', '.ico'
        ]))
        if any(url.lower().endswith(ext) for ext in skip_extensions):
            return False

        # Skip URLs matching exclude patterns
        exclude_patterns = self.crawling_config.get('exclude_patterns', [])
        for pattern in exclude_patterns:
            if re.search(pattern, url):
                return False

        # Only include URLs matching include patterns (if specified)
        include_patterns = self.crawling_config.get('include_patterns', [])
        if include_patterns:
            if not any(re.search(pattern, url) for pattern in include_patterns):
                return False

        # Skip anchor links to same page or already visited URLs
        if url in visited_urls:
            return False

        return True

    def normalize_url(self, url: str, base_url: str) -> str:
        """
        Normalize and resolve relative URLs.
        - For URLs starting with '/', combine with the scheme and netloc of base_url
        - In other cases, use urljoin(base_url, url)
        """
        url = url.split('#')[0]
        parsed_base = urllib.parse.urlparse(base_url)
        if url.startswith('/'):
            # Combine with the scheme and netloc of base_url
            return f"{parsed_base.scheme}://{parsed_base.netloc}{url}"
        else:
            return urllib.parse.urljoin(base_url, url)

    def extract_links(self, soup: BeautifulSoup, current_url: str, visited_urls: Set[str]) -> List[str]:
        """Extract all valid links from the page."""
        links = []
        link_selectors = self.site_config.get('link_selectors', ['a'])

        for selector in link_selectors:
            for link_element in soup.select(selector):
                href = link_element.get('href')
                if href:
                    full_url = self.normalize_url(href, current_url)
                    # is_valid_url now needs visited_urls
                    if self.is_valid_url(full_url, visited_urls):
                        logger.info(f'[HtmlProcessor] Found link: {href} -> {full_url} --> Valid!')
                        if full_url not in links:
                            links.append(full_url)
                    else:
                        logger.warning(f'[HtmlProcessor] Found link: {href} -> {full_url} --> Invalid!')
        return links

    def clean_content_html(self, soup: BeautifulSoup) -> BeautifulSoup:
        """Remove navigation, ads, and other non-content elements from BeautifulSoup object."""
        # Create a copy of the soup to avoid modifying the original
        cleaned_soup = BeautifulSoup(str(soup), 'html.parser')

        remove_selectors = self.site_config.get('remove_selectors', [
            'nav', 'header', 'footer', '.navbar', '.nav', '.navigation',
            '.sidebar', '.menu', '.breadcrumb', '.pagination',
            '.advertisement', '.ads', '.social-share', '.comments',
            'script', 'style', 'noscript', '.search-box'
        ])

        for selector in remove_selectors:
            for element in cleaned_soup.select(selector):
                element.decompose()
        return cleaned_soup

    def parse_and_extract_html_content(self, html_content: str, current_url: str, visited_urls: Set[str]) -> Dict:
        """Parses HTML, extracts title, content, and links."""
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract title using configured selectors
        title = "Untitled"
        title_selectors = self.site_config.get('title_selectors', ['title', 'h1'])
        for selector in title_selectors:
            element = soup.select_one(selector)
            if element:
                title = element.get_text().strip()
                break

        # Clean the HTML before extracting main content and links
        cleaned_soup_for_content = self.clean_content_html(BeautifulSoup(str(soup), 'html.parser')) # Create a proper copy

        # Try to find main content area using configured selectors
        content_selectors = self.site_config.get('content_selectors', [
            'main', 'article', '.content', '.main-content', '.documentation'
        ])
        main_content_element = cleaned_soup_for_content # Default to the whole cleaned body
        for selector in content_selectors:
            element = cleaned_soup_for_content.select_one(selector)
            if element:
                main_content_element = element
                break

        try:
            # Use the configured html2text instance
            markdown_content = self.h.handle(str(main_content_element))
            markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content).strip()
        except Exception as e:
            # Add detailed debug information
            logger.error(f"Error during markdown conversion: {str(e)}")
            logger.error(f"HTML2Text instance: {type(self.h)}")
            logger.error(f"Main content element type: {type(main_content_element)}")
            if hasattr(self.h, 'handle'):
                logger.error(f"HTML2Text.handle type: {type(self.h.handle)}")
            else:
                logger.error("HTML2Text has no 'handle' method")
            raise

        # Extract links from the original soup (before content-specific cleaning, but after general cleaning if any)
        # Or, extract from a less aggressively cleaned soup if necessary. For now, using the initial soup.
        links = self.extract_links(soup, current_url, visited_urls)

        return {
            'title': title,
            'content': markdown_content,
            'links': links
        }
