import json
import re
import urllib.parse
from pathlib import Path
from typing import Dict, List, Callable, Any, Optional
import threading

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

    def save_markdown_file(self, content_data: Dict, lock: threading.Lock, stop_crawl_event: threading.Event, current_visited_count: int, thread_name: Optional[str] = None) -> bool:
        """
        Save content as a markdown file.
        Returns True if the file was attempted to be saved (or saved), False if skipped due to no content/success.
        Manages saved_file_count and sets stop_crawl_event.
        """
        if not content_data.get('success') or not content_data.get('content', '').strip():
            return False # Skipped saving

        parsed_url = urllib.parse.urlparse(content_data['url'])
        path_parts = [part for part in parsed_url.path.split('/') if part]
        relative_path = '/'.join(path_parts)
        filepath = self.output_dir / f"{relative_path}.md" if relative_path else self.output_dir / "index.md"

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

    def create_llms_txt(self):
        """Create llms.txt file listing all markdown files with summaries."""
        llms_doc_prefix = self.output_config.get('llms_doc_prefix', '')
        llms_doc_prefix = llms_doc_prefix + "_" if llms_doc_prefix else ''

        print("\n\nCreating llms.txt index (OutputManager)...")

        llms_txt_path = self.output_dir / f"{llms_doc_prefix}llms.txt"
        md_files = list(self.output_dir.rglob("*.md"))
        lines = []
        tool_list = [self.content_metadata_tool_func] # Use the passed-in function
        llm = self.get_llm_func().bind_tools(tool_list) # Use the passed-in function

        dest_github_repo = self.output_config.get('dest_github_repo')
        raw_url_prefix = None
        if dest_github_repo:
            dest_github_repo = dest_github_repo.replace('git@github.com:', 'https://raw.githubusercontent.com/')
            dest_github_repo = dest_github_repo.replace('.git', '')
            branch = 'main'  # Assuming main branch
            raw_url_prefix = f"{dest_github_repo}/{branch}"

        for md_file in sorted(md_files):
            if md_file.name == f"{llms_doc_prefix}llms.txt":
                continue

            print(f"Processing for llms.txt: {md_file}", end='')
            relative_path = md_file.relative_to(self.output_dir)
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            title, desc = self._summarize_and_title_for_llms(llm, content, md_file.name)

            if raw_url_prefix:
                file_url = f"{raw_url_prefix}/{relative_path}"
            else:
                file_url = str(relative_path) # Keep as relative path if no repo
            lines.append(f"- [{title}]({file_url}): {desc}")
            print(": Done")

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
        summary = {
            'base_url': base_url,
            'pages_crawled': pages_crawled,
            'successful_pages': successful_pages,
            'failed_pages': failed_pages,
            'config_used': config_used
        }
        summary_path = self.output_dir / "crawl_summary.json"
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        print(f"Saved crawl summary to {summary_path} (OutputManager).")
