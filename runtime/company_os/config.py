from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

_RUNTIME_DIR = Path(__file__).resolve().parent.parent
load_dotenv(_RUNTIME_DIR / ".env")


@lru_cache
def repo_root() -> Path:
    override = os.getenv("REPO_ROOT")
    if override:
        return Path(override).resolve()
    return _RUNTIME_DIR.parent.resolve()


def llm_provider() -> str:
    """openai | openrouter (default: openrouter)."""
    return os.getenv("LLM_PROVIDER", "openrouter").strip().lower()


def has_live_api_key() -> bool:
    provider = llm_provider()
    if provider == "openrouter":
        return bool(os.getenv("OPENROUTER_API_KEY"))
    if provider == "openai":
        return bool(os.getenv("OPENAI_API_KEY"))
    return bool(os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY"))


def mock_llm() -> bool:
    flag = os.getenv("MOCK_LLM", "").lower()
    if flag in {"1", "true", "yes"}:
        return True
    if flag in {"0", "false", "no"}:
        return False
    return not has_live_api_key()


def chat_model_name() -> str:
    """
    OpenRouter model IDs look like: openai/gpt-4o-mini, anthropic/claude-sonnet-4
    OpenAI direct: gpt-4o-mini
    """
    if llm_provider() == "openrouter":
        return os.getenv("OPENROUTER_MODEL") or os.getenv(
            "OPENAI_MODEL", "openai/gpt-4o-mini"
        )
    return os.getenv("OPENAI_MODEL", "gpt-4o-mini")


def openrouter_base_url() -> str:
    return os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")


def openrouter_headers() -> dict[str, str]:
    headers: dict[str, str] = {
        "X-Title": os.getenv("OPENROUTER_APP_NAME", "AI Company Task Manager"),
    }
    referer = os.getenv("OPENROUTER_HTTP_REFERER")
    if referer:
        headers["HTTP-Referer"] = referer
    return headers


def langsmith_enabled() -> bool:
    return os.getenv("LANGCHAIN_TRACING_V2", "").lower() in {"1", "true", "yes"}


def configure_langsmith(run_name: str | None = None, tags: list[str] | None = None) -> dict:
    os.environ.setdefault("LANGCHAIN_PROJECT", "ai-company-task-manager")
    cfg: dict = {}
    if run_name:
        cfg["run_name"] = run_name
    if tags:
        cfg["tags"] = tags
    return cfg
