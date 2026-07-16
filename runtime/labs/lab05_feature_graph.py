from __future__ import annotations

from company_os.feature_graph import build_feature_graph
from company_os.repo import FEATURE_REQUEST, read_text


def main() -> None:
    print("=== Lab 5: Full FeatureGraph (mock impl + review loop) ===")
    graph = build_feature_graph()
    result = graph.invoke(
        {
            "feature_request": FEATURE_REQUEST,
            "force_review_changes_once": True,
            "breaking_change": False,
        },
        config={"configurable": {"thread_id": "lab05"}},
    )
    print("status:", result.get("status"))
    print("review_cycles:", result.get("review_cycles"))
    print("review_decision:", result.get("review_decision"))
    print("qa_decision:", result.get("qa_decision"))
    for m in result.get("messages", []):
        print(" -", m)

    assert result.get("status") == "done"
    assert int(result.get("review_cycles") or 0) >= 1
    assert result.get("qa_decision") == "pass"
    mem = read_text("memory/task-memory/README.md")
    assert "TASK-0002" in mem
    print("DoD: review re-entry >=1 and finalize done")


if __name__ == "__main__":
    main()
