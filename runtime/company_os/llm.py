from __future__ import annotations

from typing import Any

from langchain_core.language_models.fake_chat_models import FakeListChatModel
from langchain_core.messages import AIMessage

from company_os.config import (
    chat_model_name,
    llm_provider,
    mock_llm,
    openrouter_base_url,
    openrouter_headers,
)


class ScriptedChatModel(FakeListChatModel):
    """Offline stand-in that still exercises LangChain runnables."""

    @property
    def _llm_type(self) -> str:
        return "scripted-chat-model"


def get_chat_model(responses: list[str] | None = None) -> Any:
    """
    Return a chat model.
    - MOCK_LLM / no key → FakeListChatModel
    - LLM_PROVIDER=openrouter (default) → ChatOpenAI against OpenRouter
    - LLM_PROVIDER=openai → ChatOpenAI / OpenAI API
    """
    if mock_llm():
        canned = responses or [
            "MOCK: Company OS runtime is online. Cite docs; do not guess.",
        ]
        return ScriptedChatModel(responses=canned)

    from langchain_openai import ChatOpenAI

    model = chat_model_name()
    provider = llm_provider()

    if provider == "openrouter":
        import os

        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise RuntimeError("OPENROUTER_API_KEY is required when MOCK_LLM=false")
        return ChatOpenAI(
            model=model,
            api_key=api_key,
            base_url=openrouter_base_url(),
            default_headers=openrouter_headers(),
            temperature=0,
        )

    if provider == "openai":
        import os

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is required when LLM_PROVIDER=openai")
        return ChatOpenAI(model=model, api_key=api_key, temperature=0)

    raise RuntimeError(f"Unsupported LLM_PROVIDER={provider!r} (use openrouter|openai)")


def invoke_hello(message: str = "ping") -> str:
    model = get_chat_model(
        responses=[
            "Hello from AI Company Task Manager runtime (MOCK_LLM). "
            "Set OPENROUTER_API_KEY and MOCK_LLM=false for OpenRouter. "
            "Enable LANGCHAIN_TRACING_V2 + LANGCHAIN_API_KEY for LangSmith."
        ]
    )
    result = model.invoke(message)
    if isinstance(result, AIMessage):
        return str(result.content)
    return str(result)
