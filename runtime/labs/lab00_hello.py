from __future__ import annotations

from datetime import datetime

from company_os.config import configure_langsmith, langsmith_enabled, mock_llm
from company_os.llm import invoke_hello


def main() -> None:
    print("=== Lab 0: Bootstrap & First Trace ===")
    print(f"MOCK_LLM={mock_llm()} LANGSMITH_TRACING={langsmith_enabled()}")
    run_name = f"lab00-hello:{datetime.now().strftime('%Y%m%d-%H%M')}"
    cfg = configure_langsmith(run_name=run_name, tags=["lab:0", "role:runtime"])
    text = invoke_hello("Say hello from AI Company Task Manager runtime.")
    print("response:", text)
    print("langsmith_config:", cfg)
    if not langsmith_enabled():
        print(
            "NOTE: Set LANGCHAIN_TRACING_V2=true and LANGCHAIN_API_KEY in runtime/.env "
            "to see this run in LangSmith project ai-company-task-manager."
        )
    print("DoD: hello runnable OK")


if __name__ == "__main__":
    main()
