"""Run labs with OpenRouter + LangSmith tracing enabled."""

from __future__ import annotations

import sys
from datetime import datetime

from company_os.config import (
    configure_langsmith,
    enable_langsmith,
    langsmith_api_key,
    langsmith_enabled,
    langsmith_project,
    langsmith_project_url,
    mock_llm,
)
from company_os.feature_graph import build_feature_graph
from company_os.llm import invoke_hello
from company_os.pm_agent import answer_next_role
from company_os.repo import FEATURE_REQUEST


def main() -> int:
    print("=== Company OS traced demo ===")
    print(f"MOCK_LLM={mock_llm()}")

    if not enable_langsmith():
        print(
            "\n[!] LangSmith API key missing.\n"
            "Add one of these to runtime/.env (gitignored):\n"
            "  LANGSMITH_API_KEY=lsv_...\n"
            "  # or LANGCHAIN_API_KEY=lsv_...\n"
            "  LANGCHAIN_TRACING_V2=true\n"
            "  LANGCHAIN_PROJECT=ai-company-task-manager\n\n"
            "Create a key at: https://smith.langchain.com/settings\n"
            "OpenRouter alone cannot visualize graphs in LangSmith.\n"
        )
        return 2

    print(f"LangSmith tracing ON project={langsmith_project()}")
    print(f"Dashboard: {langsmith_project_url()}")
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # 1) LLM hello (appears as chat run)
    hello_cfg = configure_langsmith(
        run_name=f"demo:hello:{stamp}", tags=["demo", "lab:0", "role:runtime"]
    )
    print("\n-- hello --")
    print(invoke_hello("Say hello from AI Company Task Manager (LangSmith demo)."))
    print("config:", hello_cfg)

    # 2) Role-grounded PM call
    print("\n-- pm role --")
    pm_cfg = configure_langsmith(
        run_name=f"demo:pm:{stamp}", tags=["demo", "lab:1", "role:pm"]
    )
    _ = pm_cfg
    print(answer_next_role("이 Feature의 다음 담당 Role은 누구인가? 근거 문서를 인용해."))

    # 3) FeatureGraph (node waterfall in LangSmith)
    print("\n-- feature graph --")
    graph = build_feature_graph()
    result = graph.invoke(
        {
            "feature_request": FEATURE_REQUEST,
            "force_review_changes_once": True,
        },
        config={
            "configurable": {"thread_id": f"demo-{stamp}"},
            **configure_langsmith(
                run_name=f"featuregraph:demo:{stamp}",
                tags=["demo", "lab:5", "graph:feature", "gate:review"],
            ),
        },
    )
    print("status:", result.get("status"))
    print("review_cycles:", result.get("review_cycles"))
    for m in result.get("messages", []):
        print(" -", m)

    print("\nOpen LangSmith UI:")
    print(f"  {langsmith_project_url()}")
    print("Filter by tag: demo  or run_name prefix: featuregraph:demo:")
    assert langsmith_enabled()
    return 0


if __name__ == "__main__":
    sys.exit(main())
