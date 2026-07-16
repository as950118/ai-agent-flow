from __future__ import annotations

import uuid
from datetime import date
from langgraph.graph import END, START, StateGraph

from company_os.repo import write_text
from company_os.state import BugFixState


def triage(state: BugFixState) -> dict:
    return {
        "run_id": state.get("run_id") or f"bug-{uuid.uuid4().hex[:8]}",
        "project_id": "proj-ai-company-task-manager",
        "bug_summary": state.get("bug_summary")
        or "감사 로그에 actor 누락",
        "severity": state.get("severity") or "S2",
        "priority": "P1",
        "hotfix": True,
        "status": "reproduce",
        "messages": [f"Triage accepted: {state.get('bug_summary', 'actor missing')}"],
    }


def reproduce(state: BugFixState) -> dict:
    return {
        "reproducible": True,
        "status": "analyze",
        "messages": ["Reproduced on mock API: audit event lacks actor"],
    }


def analyze(state: BugFixState) -> dict:
    return {
        "root_cause": "Audit writer omitted required actor field in first impl seed",
        "status": "fix",
        "messages": ["Root cause recorded"],
    }


def fix(state: BugFixState) -> dict:
    path = write_text(
        f"projects/ai-company-task-manager/api/BUGFIX-{state.get('run_id')}.md",
        f"""# Bug Fix Notes

Bug: {state.get('bug_summary')}
Root cause: {state.get('root_cause')}
Fix: require actor in PATCH status payload; persist on audit row
Regression test: assert actor present
Date: {date.today().isoformat()}
""",
    )
    task = write_text(
        "tasks/TASK-0003-audit-actor-missing.md",
        f"""# Task: Fix missing actor on audit log

| Field | Value |
|-------|-------|
| Task ID | TASK-0003 |
| Type | Bug |
| Status | In Review |
| Workflow | fix-bug |
| Severity | {state.get('severity')} |

## Links
- Fix notes: {path}
""",
    )
    return {
        "fix_notes_path": path,
        "task_path": task,
        "status": "review",
        "messages": [f"Fix notes → {path}"],
    }


def review(state: BugFixState) -> dict:
    return {
        "review_decision": "approve",
        "status": "verify",
        "messages": ["Reviewer approve bugfix"],
    }


def verify(state: BugFixState) -> dict:
    return {
        "qa_decision": "pass",
        "status": "done",
        "messages": ["QA verified actor present; bug closed"],
    }


def route_status(state: BugFixState) -> str:
    return state.get("status") or "done"


def build_bugfix_graph():
    g = StateGraph(BugFixState)
    g.add_node("triage", triage)
    g.add_node("reproduce", reproduce)
    g.add_node("analyze", analyze)
    g.add_node("fix", fix)
    g.add_node("review", review)
    g.add_node("verify", verify)

    g.add_edge(START, "triage")
    g.add_edge("triage", "reproduce")
    g.add_edge("reproduce", "analyze")
    g.add_edge("analyze", "fix")
    g.add_edge("fix", "review")
    g.add_edge("review", "verify")
    g.add_edge("verify", END)
    return g.compile()


def run_bugfix(bug_summary: str | None = None) -> BugFixState:
    graph = build_bugfix_graph()
    return graph.invoke({"bug_summary": bug_summary or "감사 로그에 actor 누락"})
