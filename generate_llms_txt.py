import sys
import re
import requests
from openrouter_client import get_llm
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.outputs import LLMResult

# Tool definition using LangChain's decorator
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

def parse_github_url(url):
    """
    Parse a GitHub tree URL to extract owner, repo, branch, and path.
    Ex: https://github.com/user/repo/tree/branch/some/path
    Returns (owner, repo, branch, prefix_path)
    """
    m = re.match(
        r"https://github.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/tree/(?P<branch>[^/]+)(?P<path>/.*)?",
        url)
    if not m:
        raise ValueError("Invalid GitHub tree URL: %s" % url)
    owner, repo, branch, path = m.group('owner'), m.group('repo'), m.group('branch'), m.group('path') or ''
    path = path.lstrip('/') if path else ''
    return owner, repo, branch, path

def get_raw_url(owner, repo, branch, path):
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"

def list_github_files(owner, repo, branch, prefix_path, allowed_extensions):
    """
    List all files with extensions in allowed_extensions recursively under the prefix_path using the GitHub API.
    allowed_extensions example: ['md', 'txt'] (do not include dots)
    Returns a list of dicts { 'path': ..., 'name': ... }, where 'path' is the absolute raw URL.
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    files = []
    allowed_extensions = set(ext.lower() for ext in allowed_extensions)
    while api_url:
        r = requests.get(api_url)
        r.raise_for_status()
        tree = r.json()['tree']
        for node in tree:
            rel_path = node['path']
            if not rel_path.startswith(prefix_path):
                continue
            if node['type'] == 'blob':
                ext = rel_path.rsplit('.', 1)[-1].lower() if '.' in rel_path else ''
                if ext in allowed_extensions:
                    abs_path = get_raw_url(owner, repo, branch, rel_path)
                    files.append({
                        'path': abs_path,
                        'name': rel_path.split('/')[-1]
                    })
        api_url = None  # Only need the top-level, since recursive=1 returns everything
    return files

def summarize_and_title(content, filename):
    """
    Use the LLM with tool calling to produce a title and description.
    """
    tool_list = [content_metadata_tool]
    llm = get_llm().bind_tools(tool_list)
    # LangChain's invoke with tools expects a HumanMessage and a tool argument
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
    # This usage assumes get_llm() supports the invoke() with tools parameter
    # If not, see LangChain docs for chaining with tools and LLMs and adapt accordingly
    response = llm.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=human_prompt)
        ]
    )

    # Extract tool_calls from response (LangChain standard: response.tool_calls)
    tool_calls = getattr(response, "tool_calls", None)
    title, description = None, None
    if tool_calls:
        for call in tool_calls:
            if call.get("name") == "content_metadata_tool":
                args = call.get("args", {})
                title = args.get("title")
                description = args.get("description")
                break
    # Fallback extraction or defaults
    if not title:
        title = filename.rsplit('.', 1)[0].replace('_', ' ').replace('-', ' ').title()
    if not description:
        description = f"A summary for {filename}."
    return title, description

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <GitHub tree URL> <product>")
        sys.exit(1)

    gh_url = sys.argv[1]
    product = sys.argv[2]
    owner, repo, branch, prefix_path = parse_github_url(gh_url)
    allowed_extensions = ['md', 'txt']
    all_files = list_github_files(owner, repo, branch, prefix_path, allowed_extensions)

    lines = []
    for file_info in all_files:
        abs_url = file_info['path']
        print(f"Fetching {abs_url} ...")
        resp = requests.get(abs_url)
        if resp.status_code != 200:
            print(f"Warning: failed to fetch {abs_url}")
            continue
        content = resp.text
        title, desc = summarize_and_title(content, file_info['name'])
        lines.append(f"- [{title}]({abs_url}): {desc}")

    output_file = f"{product}_llms.txt"
    with open(output_file, "w") as f:
        f.write("# Document Index\n")
        for line in lines:
            f.write(line + '\n')
    print(f"{output_file} generated with {len(lines)} entries.")

if __name__ == "__main__":
    main()
