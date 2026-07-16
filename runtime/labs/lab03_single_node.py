from __future__ import annotations

import uuid

from langgraph.graph import END, START, StateGraph

from company_os.artifacts import build_prd
from company_os.repo import FEATURE_REQUEST
from company_os.state import FeatureState


def write_prd_node(state: FeatureState) -> dict:
    path = build_prd(state.get("feature_request") or FEATURE_REQUEST)
    return {
        "prd_path": path,
        "status": "prd_done",
        "run_id": state.get("run_id") or f"lab03-{uuid.uuid4().hex[:6]}",
        "messages": [f"single-node wrote {path}"],
    }


def main() -> None:
    print("=== Lab 3: Single-node FeatureState Graph ===")
    g = StateGraph(FeatureState)
    g.add_node("write_prd", write_prd_node)
    g.add_edge(START, "write_prd")
    g.add_edge("write_prd", END)
    app = g.compile()
    result = app.invoke({"feature_request": FEATURE_REQUEST})
    print("status:", result.get("status"))
    print("prd_path:", result.get("prd_path"))
    assert result.get("prd_path")
    print("DoD: State + 1 node compile/invoke OK")


if __name__ == "__main__":
    main()
