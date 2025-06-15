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
        'crawling': {
            'crawl': True,
            'delay': 1,
            'exclude_patterns': [
                '/api/',
                '/search',
                '\\.xml$',
                '/login',
                '/logout'
            ],
            'headers': {
                'User-Agent': 'Mozilla/5.0 (compatible; DocCrawler/1.0; +https://example.com/bot)'
            },
            'include_patterns': [],
            'max_depth': 1,
            'max_pages': -1,
            'num_threads': 20,
            'skip_extensions': [
                '.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.svg', '.ico', '.json', '.xml', '.yaml'
            ],
            'timeout': 10,
            'file_extensions': [
                '.md', '.rst', '.txt', '.py', '.js', '.ts', '.html', '.css', '.json', '.yaml', '.yml'
            ]
        },
        'link_processing': {
            'url_prefix': 'https://github.com/modelcontextprotocol/python-sdk/blob/main'
        },
        'output': {
            'dest_github_repo': 'git@github.com:dyingc/mcp_docs.git',
            'directory': 'docs_output/mcp',
            'frontmatter': {
                'crawled_date': f'{str(current_date)}',
                'source': 'mcp-docs'
            },
            'ignore_images': False,
            'ignore_links': False,
            'llm_concurrency': 1,
            'llms_doc_prefix': 'mcp',
            'llms_txt': {
                'description': 'Complete MCP documentation for AI assistance',
                'include_urls': True,
                'title': 'MCP Documentation'
            },
            'minimal_size': 512,
            'output_llms_txt': False
        },
        'site': {
            'allowed_domains': [
                'github.com',
                'raw.githubusercontent.com'
            ],
            'content_selectors': [
                'main',
                'article',
                '.content',
                '.documentation'
            ],
            'link_selectors': [
                'a[href]'
            ],
            'name': 'MCP Documentation',
            'remove_selectors': [
                'nav',
                'header',
                'footer',
                '.navbar',
                '.nav',
                '.sidebar',
                '.menu',
                '.breadcrumb',
                '.pagination',
                'script',
                'style',
                'noscript',
                '.search-box'
            ],
            'start_urls': [],
            'title_selectors': [
                'title',
                'h1',
                '.page-title'
            ],
            'url': 'https://github.com/modelcontextprotocol/python-sdk'
        }
    }

    with open(filename, 'w', encoding='utf-8') as f:
        yaml.dump(sample_config, f, default_flow_style=False, indent=2)

    print(f"Created sample config file: {filename}")
    return filename
