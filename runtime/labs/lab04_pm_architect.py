from __future__ import annotations

from company_os.feature_graph import (
    clarify_pm,
    design,
    intake,
    route_after_design,
    route_after_prd,
    write_prd,
)
from company_os.repo import FEATURE_REQUEST, read_text
from company_os.state import FeatureState
from langgraph.graph import END, START, StateGraph


def main() -> None:
    print("=== Lab 4: PM → Architect with gates ===")

    # Happy path subgraph
    g = StateGraph(FeatureState)
    g.add_node("intake", intake)
    g.add_node("write_prd", write_prd)
    g.add_node("clarify_pm", clarify_pm)
    g.add_node("design", design)
    g.add_edge(START, "intake")
    g.add_edge("intake", "write_prd")
    g.add_conditional_edges("write_prd", route_after_prd, ["design", "clarify_pm"])
    g.add_edge("clarify_pm", "write_prd")
    g.add_conditional_edges("design", route_after_design, {
        "implement_backend": END,
        "escalate": END,
        "clarify_pm": "clarify_pm",
    })
    app = g.compile()

    happy = app.invoke({"feature_request": FEATURE_REQUEST, "priority": "P1"})
    print("happy status:", happy.get("status"), "arch:", happy.get("architecture_path"))
    assert happy.get("architecture_path")
    assert happy.get("adr_paths")
    adr = read_text(happy["adr_paths"][0])
    assert "Rejected Alternatives" in adr

    # Clarify path
    clarify = app.invoke({"feature_request": FEATURE_REQUEST, "priority": "CLARIFY_TEST"})
    print("clarify→resolved status:", clarify.get("status"), "prd:", clarify.get("prd_path"))
    assert clarify.get("architecture_path") or clarify.get("prd_path")
    print("DoD: happy + clarify paths OK")


if __name__ == "__main__":
    main()
