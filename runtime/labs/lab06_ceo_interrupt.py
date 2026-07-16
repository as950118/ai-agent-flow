from __future__ import annotations

import uuid

from langgraph.types import Command

from company_os.feature_graph import build_feature_graph
from company_os.repo import FEATURE_REQUEST, read_text


def main() -> None:
    print("=== Lab 6: CEO Human-in-the-loop interrupt ===")
    graph = build_feature_graph()
    thread_id = f"lab06-{uuid.uuid4().hex[:6]}"
    config = {"configurable": {"thread_id": thread_id}}

    interrupted = graph.invoke(
        {
            "feature_request": FEATURE_REQUEST,
            "breaking_change": True,
            "ceo_approved": None,
            "force_review_changes_once": True,
        },
        config=config,
    )
    print("interrupted keys:", list(interrupted.keys()) if isinstance(interrupted, dict) else type(interrupted))
    # When interrupted, state may be incomplete; resume with approval
    resumed = graph.invoke(Command(resume={"approved": True}), config=config)
    print("resumed status:", resumed.get("status"))
    print("ceo_approved:", resumed.get("ceo_approved"))
    print("architecture:", resumed.get("architecture_path"))
    for m in resumed.get("messages", [])[-8:]:
        print(" -", m)

    assert resumed.get("ceo_approved") is True
    assert resumed.get("status") == "done"
    note = read_text("memory/decision-memory/CEO-DECISION-breaking-change.md")
    assert "Approved: True" in note
    print("DoD: interrupt + resume + CEO decision note OK")


if __name__ == "__main__":
    main()
