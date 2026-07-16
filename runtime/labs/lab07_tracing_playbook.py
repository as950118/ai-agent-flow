from __future__ import annotations

from datetime import datetime

from company_os.config import configure_langsmith, langsmith_enabled
from company_os.feature_graph import build_feature_graph
from company_os.repo import FEATURE_REQUEST, write_text


def main() -> None:
    print("=== Lab 7: Tracing Playbook ===")
    graph = build_feature_graph()
    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    results = []
    for i in range(2):
        run_name = f"featuregraph:lab07:{stamp}:r{i+1}"
        tags = ["lab:7", "role:pm", "gate:review", "graph:feature"]
        cfg = {
            "configurable": {"thread_id": f"lab07-{i}-{stamp}"},
            **configure_langsmith(run_name=run_name, tags=tags),
            "metadata": {
                "run_id": run_name,
                "model": "mock" if not langsmith_enabled() else "live",
            },
        }
        result = graph.invoke(
            {
                "feature_request": FEATURE_REQUEST,
                "force_review_changes_once": True,
            },
            config=cfg,
        )
        results.append(
            {
                "run_name": run_name,
                "status": result.get("status"),
                "prd_path": result.get("prd_path"),
                "review_cycles": result.get("review_cycles"),
                "messages": len(result.get("messages") or []),
            }
        )
        print(f"run{i+1}:", results[-1])

    note = write_text(
        "labs/notes/lab07-tracing.md",
        f"""# Lab7 Tracing Notes

LangSmith enabled: {langsmith_enabled()}
Project: ai-company-task-manager

## Runs
{results}

## Waterfall (logical)
intake → write_prd → design → implement_backend → review(changes) → implement_backend → review(approve) → qa → finalize

## Filter tips
- tag:`lab:7`
- tag:`gate:review`
- run_name prefix:`featuregraph:lab07:`
""",
    )
    print("notes:", note)
    print("DoD: two comparable runs recorded (enable LangSmith keys for cloud UI)")


if __name__ == "__main__":
    main()
