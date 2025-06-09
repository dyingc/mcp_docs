import yaml
import json
from pathlib import Path
from typing import Dict
from datetime import datetime

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
    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')

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
            'max_pages': 10, # Allow unlimited if max_pages is -1
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
            'output_llms_txt': False,
            'llms_doc_prefix': 'n8n',
            'ignore_links': False,
            'ignore_images': False,
            'dest_github_repo': 'git@github.com:dyingc/mcp_docs.git',
            'frontmatter': {
                'source': 'n8n-docs',
                'crawled_date': f'{str(current_date)}'
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
