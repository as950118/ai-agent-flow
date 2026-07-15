from __future__ import annotations

from langchain_core.tools import tool

from company_os.repo import read_text, write_text


@tool
def read_repo_file(relative_path: str) -> str:
    """Read a Markdown/text file from the Company OS repository by relative path."""
    try:
        content = read_text(relative_path)
    except FileNotFoundError as exc:
        return f"ERROR: {exc}"
    # Keep tool payloads bounded for context windows
    if len(content) > 8000:
        content = content[:8000] + "\n\n...[truncated]..."
    return f"PATH: {relative_path}\n\n{content}"


@tool
def write_repo_file(relative_path: str, content: str) -> str:
    """Write a text file under the Company OS repository (relative path)."""
    if relative_path.startswith(".") or relative_path.startswith("/"):
        return "ERROR: relative_path must be a repo-relative path without leading slash"
    forbidden = (".env", "credentials", "secret")
    lower = relative_path.lower()
    if any(x in lower for x in forbidden):
        return "ERROR: refusing to write potential secret files"
    path = write_text(relative_path, content)
    return f"WROTE: {path}"


DOC_TOOLS = [read_repo_file, write_repo_file]
