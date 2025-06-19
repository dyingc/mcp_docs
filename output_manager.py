import json
import re
import urllib.parse
from pathlib import Path
from typing import Dict, List, Callable, Any, Optional
import threading
import subprocess
import os

# To avoid circular dependency if get_llm or content_metadata_tool were here.
# These will be passed in from doc_crawler.py.

class OutputManager:
    def __init__(self, output_config: Dict, output_dir: Path, max_pages: int,
                 content_metadata_tool_func: Callable, get_llm_func: Callable):
        self.output_config = output_config
        self.output_dir = output_dir
        self.max_pages = max_pages
        self.content_metadata_tool_func = content_metadata_tool_func
        self.get_llm_func = get_llm_func
        self.saved_file_count = 0
        self.summary_path = self.output_dir / "crawl_summary.json"
        # Load existing summary if it exists
        self.summary = self._load_summary()
        # Initialize html_processor
        self.html_processor = None  # Will be set by DocCrawler

        # Store failed pages for counting (added for failed page stat tracking)
        self.failed_pages_list = []

    def _load_summary(self) -> Dict:
        """Load existing summary from JSON file if it exists."""
        if self.summary_path.exists():
            try:
                with open(self.summary_path, 'r', encoding='utf-8') as f:
                    summary = json.load(f)
                    # Ensure saved_files exists
                    if 'saved_files' not in summary:
                        summary['saved_files'] = []
                    return summary
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading summary file: {e}")
                # Return default summary if file is corrupted
                return self._get_default_summary()
        return self._get_default_summary()

    def _get_default_summary(self) -> Dict:
        """Return a default summary dictionary."""
        return {
            'base_url': '',
            'pages_crawled': 0,
            'successful_pages': 0,
            'failed_pages': 0,
            'saved_files': [],
            'config_used': {}
        }

    def _save_summary(self):
        """Save current summary to JSON file."""
        # Ensure saved_files exists before saving
        if 'saved_files' not in self.summary:
            self.summary['saved_files'] = []
        with open(self.summary_path, 'w', encoding='utf-8') as f:
            json.dump(self.summary, f, indent=2)

    def save_markdown_file(self, content_data: Dict, lock: threading.Lock, stop_crawl_event: threading.Event, current_visited_count: int, thread_name: Optional[str] = None) -> bool:
        """
        Save content as a markdown file.
        Returns True if the file was attempted to be saved (or saved), False if skipped due to no content/success.
        Manages saved_file_count and sets stop_crawl_event.
        """
        if not content_data.get('success') or not content_data.get('content', '').strip():
            return False # Skipped saving

        parsed_url = urllib.parse.urlparse(content_data['url'])
        if 'CLAUDE.md' in parsed_url.path:
            pass
        path_parts = [part for part in parsed_url.path.split('/') if part]
        relative_path = '/'.join(path_parts)
        # filename = relative_path if relative_path.endswith(".md") else f"{relative_path}.md"
        filename = relative_path if os.path.splitext(relative_path)[1] else f"{relative_path}.md"
        filepath = self.output_dir / filename

        filepath.parent.mkdir(parents=True, exist_ok=True)
        markdown_content = f"# {content_data['title']}\n\n{content_data['content']}"
        minimal_size = self.output_config.get('minimal_size', 0)

        file_saved_this_call = False
        if len(markdown_content.encode('utf-8')) >= minimal_size:
            with lock:
                if stop_crawl_event.is_set():
                    print(f"Skipped saving {filepath} as stop signal is active (OutputManager).")
                    return True # Attempted, but stopped

                if self.saved_file_count < self.max_pages or self.max_pages == -1: # Allow unlimited if max_pages is -1
                    self.saved_file_count += 1
                    file_saved_this_call = True
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)

                    # Add file info to summary
                    file_info = {
                        'url': content_data['url'],
                        'title': content_data['title'],
                        'filepath': str(filepath.relative_to(self.output_dir)),
                        'size': len(markdown_content.encode('utf-8')),
                        'depth': content_data.get('depth', 0)
                    }
                    self.summary['saved_files'].append(file_info)
                    self._save_summary()

                    # Use current_visited_count for the print statement
                    thread_id_to_print = thread_name if thread_name else threading.current_thread().name
                    print(f"Saved ({self.saved_file_count}/{current_visited_count}) [Thread: {thread_id_to_print}]: {filepath}")

                    if self.saved_file_count >= self.max_pages and self.max_pages != -1:
                        stop_crawl_event.set()
                        print(f"Max pages limit ({self.max_pages}) reached. Signaling threads to stop (OutputManager).")
                else:
                    print(f"Max pages limit reached. Skipped saving {filepath} (OutputManager).")
                    if not stop_crawl_event.is_set():
                        stop_crawl_event.set() # Ensure it's set
                        print("Max pages limit reached. Signaling threads to stop (redundant check in OutputManager).")
                return True # Attempted saving
        else:
            print(f"Skipped: {filepath} (too small)")
            return False # Skipped due to size

    def get_saved_file_count(self) -> int:
        return self.saved_file_count

    def get_failed_pages_count(self):
        """Return the number of failed pages recorded."""
        return len(self.failed_pages_list)

    def get_github_raw_url(self, username, repo, branch, file_path):
        return f"https://raw.githubusercontent.com/{username}/{repo}/{branch}/{file_path}"

    def get_current_git_branch(self) -> Optional[str]:
        """
        Return the current git branch name for the output_dir.
        Returns None if it can't determine the branch.
        """
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                cwd=str(self.output_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            branch = result.stdout.strip()
            if branch:
                return branch
        except Exception as e:
            print(f"Could not get current git branch: {e}")
        return None

    def create_llms_txt(self):
        """Create llms.txt file listing all markdown files with summaries."""
        llms_doc_prefix = self.output_config.get('llms_doc_prefix', '')
        llms_doc_prefix = llms_doc_prefix + "_" if llms_doc_prefix else ''

        print("\n\nCreating llms.txt index (OutputManager)...")

        llms_txt_path = self.output_dir / f"{llms_doc_prefix}llms.txt"

        # Read saved files from summary
        if not self.summary_path.exists():
            print("No crawl summary found. Please run the crawler first.")
            return

        with open(self.summary_path, 'r', encoding='utf-8') as f:
            summary = json.load(f)

        saved_files = summary.get('saved_files', [])
        if not saved_files:
            print("No saved files found in crawl summary.")
            return

        lines = []
        tool_list = [self.content_metadata_tool_func]
        llm = self.get_llm_func().bind_tools(tool_list)

        dest_github_repo = self.output_config.get('dest_github_repo')
        git_branch = self.get_current_git_branch() if dest_github_repo else None
        llm_concurrency = self.output_config.get('llm_concurrency', 1)

        def process_file(file_info):
            filepath = self.output_dir / file_info['filepath']
            if filepath.name == f"{llms_doc_prefix}llms.txt":
                return None

            print(f"Processing for llms.txt: {filepath}", end='')

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            title, desc = self._summarize_and_title_for_llms(llm, content, filepath.name)

            if dest_github_repo and git_branch:
                # Extract username and repo from dest_github_repo string
                match = re.search(r"(?:github.com[/:])([^/]+)/([^/.]+)", dest_github_repo)
                if match:
                    username, repo = match.group(1), match.group(2)
                    file_url = self.get_github_raw_url(username, repo, git_branch, str(filepath))
                else:
                    file_url = str(filepath)
            else:
                file_url = str(filepath)

            print(": Done")
            return f"- [{title}]({file_url}): {desc}"

        # Process files concurrently if llm_concurrency > 1
        if llm_concurrency > 1:
            from concurrent.futures import ThreadPoolExecutor
            with ThreadPoolExecutor(max_workers=llm_concurrency) as executor:
                futures = [executor.submit(process_file, file_info) for file_info in saved_files]
                for future in futures:
                    result = future.result()
                    if result:
                        lines.append(result)
        else:
            # Sequential processing
            for file_info in saved_files:
                result = process_file(file_info)
                if result:
                    lines.append(result)

        with open(llms_txt_path, 'w', encoding='utf-8') as f:
            f.write("# Document Index\n")
            for line in lines:
                f.write(line + '\n')
        print(f"Created {llms_txt_path.name} with {len(lines)} entries (OutputManager).")

    def _summarize_and_title_for_llms(self, llm: Any, content: str, filename: str):
        """Helper for summarize_and_title, specific to llms.txt creation context."""
        # This logic is identical to what was in DocCrawler.summarize_and_title
        # We need to import SystemMessage and HumanMessage if they are not available globally
        # For now, assuming they are available or get_llm_func handles this context.
        # If not, they need to be imported here or passed.
        # For simplicity, I'll assume they are available via the llm object's invocation.
        # This might require `from langchain_core.messages import SystemMessage, HumanMessage` at the top.
        # Let's add the import for now.
        from langchain_core.messages import SystemMessage, HumanMessage

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
                if call.get("name") == "content_metadata_tool": # Tool name should match
                    args = call.get("args", {})
                    title = args.get("title")
                    description = args.get("description")
                    break
        if not title:
            title = filename.rsplit('.', 1)[0].replace('_', ' ').replace('-', ' ').title()
        if not description:
            description = f"A summary for {filename}."
        return title, description

    def save_crawl_summary(self, base_url: str, pages_crawled: int, successful_pages: int, failed_pages: int, config_used: Dict):
        """Save crawl summary to a JSON file."""
        self.summary.update({
            'base_url': base_url,
            'pages_crawled': pages_crawled,
            'successful_pages': successful_pages,
            'failed_pages': failed_pages,
            'config_used': config_used
        })
        self._save_summary()
        print(f"Saved crawl summary to {self.summary_path} (OutputManager).")
