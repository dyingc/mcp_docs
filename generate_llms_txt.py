import sys
import re
import requests
from openrouter_client import ask_gemini

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

def list_github_files(owner, repo, branch, prefix_path, allowed_extensions):
    """
    List all files with extensions in allowed_extensions recursively under the prefix_path using the GitHub API.
    allowed_extensions example: ['md', 'txt'] (do not include dots)
    Returns a list of dicts { 'path': ..., 'name': ... }
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    files = []
    allowed_extensions = set(ext.lower() for ext in allowed_extensions)
    while api_url:
        r = requests.get(api_url)
        r.raise_for_status()
        tree = r.json()['tree']
        for node in tree:
            path = node['path']
            if not path.startswith(prefix_path):
                continue
            if node['type'] == 'blob':
                ext = path.rsplit('.', 1)[-1].lower() if '.' in path else ''
                if ext in allowed_extensions:
                    files.append({
                        'path': path,
                        'name': path.split('/')[-1]
                    })
        api_url = None  # Only need the top-level, since recursive=1 returns everything
    return files

def get_raw_url(owner, repo, branch, path):
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"

def summarize_and_title(content, filename):
    """
    Use the LLM to summarize the content and produce a human-friendly name.
    """
    prompt = (
        f"Given the following file named '{filename}':\n\n"
        "1. Output a suitable human-readable title for the file (for documentation, omit extension).\n"
        "2. Output a concise 1-sentence description of what this file is about, suitable for an LLM index.\n\n"
        "File Content (start):\n"
        f"{content[:4000]}\n"  # send first 4000 chars for context
        "\n---\n"
        "Respond using this format:\n"
        "Title: <title>\n"
        "Description: <description>\n"
    )
    response = ask_gemini(prompt)
    # crude parse
    title = None
    description = None
    for line in response.splitlines():
        if line.lower().startswith("title:"):
            title = line[len("title:"):].strip()
        if line.lower().startswith("description:"):
            description = line[len("description:"):].strip()
    if not title:
        title = filename.rsplit('.', 1)[0].replace('_', ' ').replace('-', ' ').title()
    if not description:
        description = f"A summary for {filename}."
    return title, description

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <GitHub tree URL>")
        sys.exit(1)

    gh_url = sys.argv[1]
    owner, repo, branch, prefix_path = parse_github_url(gh_url)
    allowed_extensions = ['md', 'txt']
    all_files = list_github_files(owner, repo, branch, prefix_path, allowed_extensions)

    lines = []
    for file_info in all_files:
        raw_url = get_raw_url(owner, repo, branch, file_info['path'])
        print(f"Fetching {raw_url} ...")
        resp = requests.get(raw_url)
        if resp.status_code != 200:
            print(f"Warning: failed to fetch {raw_url}")
            continue
        content = resp.text
        title, desc = summarize_and_title(content, file_info['name'])
        lines.append(f"- [{title}]({raw_url}): {desc}")

    with open("llms.txt", "w") as f:
        f.write("# Document Index\n")
        for line in lines:
            f.write(line + '\n')
    print(f"llms.txt generated with {len(lines)} entries.")

if __name__ == "__main__":
    main()
