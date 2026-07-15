from __future__ import annotations

import uuid
from datetime import date
from typing import Literal

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from company_os.artifacts import build_architecture, build_prd, count_acceptance_criteria
from company_os.repo import FEATURE_REQUEST, write_text
from company_os.state import FeatureState


def _msg(state: FeatureState, text: str) -> list[str]:
    return [f"[{state.get('status', '?')}] {text}"]


def intake(state: FeatureState) -> dict:
    run_id = state.get("run_id") or f"run-{uuid.uuid4().hex[:8]}"
    return {
        "run_id": run_id,
        "project_id": "proj-ai-company-task-manager",
        "feature_request": state.get("feature_request") or FEATURE_REQUEST,
        "priority": state.get("priority") or "P1",
        "status": "prd",
        "review_cycles": 0,
        "force_review_changes_once": state.get("force_review_changes_once", True),
        "needs_frontend": False,
        "release_requested": False,
        "breaking_change": bool(state.get("breaking_change", False)),
        "ceo_approved": state.get("ceo_approved"),
        "adr_paths": [],
        "task_paths": [],
        "open_questions": [],
        "blockers": [],
        "messages": _msg({**state, "status": "intake"}, f"Intake accepted run_id={run_id}"),
    }


def write_prd(state: FeatureState) -> dict:
    path = build_prd(state.get("feature_request"))
    ac = count_acceptance_criteria(path)
    open_q: list[str] = []
    # Lab4 clarify path: if caller forces thin PRD via priority marker (testing)
    if state.get("priority") == "CLARIFY_TEST":
        open_q = ["Need actor identity source before design"]
    return {
        "prd_path": path,
        "status": "design" if ac >= 3 and not open_q else "clarify",
        "open_questions": open_q,
        "messages": _msg(state, f"PM wrote PRD → {path} (AC={ac})"),
    }


def clarify_pm(state: FeatureState) -> dict:
    # Resolve open questions deterministically for lab continuity
    return {
        "open_questions": [],
        "priority": "P1",
        "status": "prd",
        "messages": _msg(state, "PM resolved open questions; returning to PRD"),
    }


def design(state: FeatureState) -> dict:
    if not state.get("prd_path"):
        return {
            "blockers": ["Design blocked: missing prd_path"],
            "status": "clarify",
            "messages": _msg(state, "Architect refused design without PRD"),
        }
    if state.get("breaking_change") and state.get("ceo_approved") is not True:
        return {
            "status": "escalate",
            "escalation": {
                "to": "ceo",
                "reason": "breaking_change requires CEO approval",
                "packet": state.get("prd_path"),
            },
            "messages": _msg(state, "Architect flagged breaking_change → escalate"),
        }
    arch_path, adr_path = build_architecture(state["prd_path"])
    return {
        "architecture_path": arch_path,
        "adr_paths": [adr_path],
        "status": "implement",
        "messages": _msg(state, f"Architect Design Pack → {arch_path}, {adr_path}"),
    }


def implement_backend(state: FeatureState) -> dict:
    if not state.get("architecture_path"):
        return {
            "blockers": ["Implement blocked: missing architecture"],
            "status": "design",
            "messages": _msg(state, "Backend refused implement without architecture"),
        }
    today = date.today().isoformat()
    api = f"""# API Spec: Tasks + Audit Logs

| Field | Value |
|-------|-------|
| Spec ID | API-0002 |
| Version | v0.1.0 |
| Status | Draft |
| Owner | Backend |
| Related | {state.get('prd_path')} / {state.get('architecture_path')} |

## Endpoints

### POST /api/v1/tasks
Creates task with status=todo.

### PATCH /api/v1/tasks/{{id}}/status
Body: `{{"status":"in_progress"|"done", "actor":"..."}}`
Illegal transition → 409.

### GET /api/v1/tasks/{{id}}/audit-logs
Returns append-only events: actor, from, to, timestamp.
"""
    # Intentionally omit actor on first cycle to trigger review changes once
    notes = f"""# Implementation Notes (Mock)

Date: {today}
Run: {state.get('run_id')}

## Done
- Transition table coded (mock)
- Audit writer drafted

## Seed Defect for Lab5
- First review cycle: actor field missing in audit payload (intentional)
"""
    if state.get("review_cycles", 0) >= 1:
        notes += "\n## Fix applied\n- actor now required and persisted.\n"
        api += "\n\n### Audit event schema\nactor: string (required)\n"

    api_path = write_text(
        "projects/ai-company-task-manager/api/API-0002-tasks-audit.md", api
    )
    notes_path = write_text(
        f"projects/ai-company-task-manager/api/IMPL-NOTES-{state.get('run_id', 'local')}.md",
        notes,
    )
    task_path = write_text(
        "tasks/TASK-0002-task-status-audit.md",
        f"""# Task: Task Status + Audit Log

| Field | Value |
|-------|-------|
| Task ID | TASK-0002 |
| Status | In Review |
| Workflow | create-feature |
| PRD | {state.get('prd_path')} |
| Architecture | {state.get('architecture_path')} |

## Outputs
- API Spec: {api_path}
- Impl Notes: {notes_path}
""",
    )
    return {
        "api_spec_path": api_path,
        "impl_notes_path": notes_path,
        "task_paths": [task_path],
        "status": "review",
        "messages": _msg(state, f"Backend mock impl → {api_path}"),
    }


def review(state: FeatureState) -> dict:
    cycles = int(state.get("review_cycles") or 0)
    force = state.get("force_review_changes_once", True)
    api = state.get("api_spec_path") or ""
    notes = state.get("impl_notes_path") or ""
    body = ""
    try:
        from company_os.repo import read_text

        body = read_text(api) + "\n" + read_text(notes)
    except Exception:
        body = ""

    if force and cycles == 0 and "actor now required" not in body:
        report = write_text(
            f"projects/ai-company-task-manager/api/REVIEW-{state.get('run_id')}-1.md",
            """# Review Report

Decision: changes_requested
Findings:
- Major: audit payload missing required `actor` (AC-3)
""",
        )
        return {
            "review_decision": "changes_requested",
            "review_report_path": report,
            "review_cycles": cycles + 1,
            "status": "implement",
            "messages": _msg(state, "Reviewer: changes_requested (actor missing)"),
        }

    report = write_text(
        f"projects/ai-company-task-manager/api/REVIEW-{state.get('run_id')}-approve.md",
        """# Review Report

Decision: approve
Findings: none blocking
""",
    )
    return {
        "review_decision": "approve",
        "review_report_path": report,
        "review_cycles": cycles,
        "status": "qa",
        "messages": _msg(state, "Reviewer: approve"),
    }


def qa(state: FeatureState) -> dict:
    if state.get("review_decision") != "approve":
        return {
            "qa_decision": "fail",
            "status": "review",
            "messages": _msg(state, "QA refused: no Reviewer approve"),
        }
    report = write_text(
        f"projects/ai-company-task-manager/api/QA-{state.get('run_id')}.md",
        """# QA Report

Decision: pass
AC Coverage: AC-1..AC-5 mapped to mock evidence
""",
    )
    return {
        "qa_decision": "pass",
        "qa_report_path": report,
        "status": "finalize",
        "messages": _msg(state, "QA: pass"),
    }


def escalate(state: FeatureState) -> dict:
    """CEO gate — interrupt for human approval when breaking_change."""
    decision = interrupt(
        {
            "prompt": "CEO approval required for breaking_change. Approve?",
            "prd_path": state.get("prd_path"),
            "escalation": state.get("escalation"),
        }
    )
    approved = bool(decision.get("approved")) if isinstance(decision, dict) else bool(decision)
    note = write_text(
        "memory/decision-memory/CEO-DECISION-breaking-change.md",
        f"""# CEO Decision Note

Date: {date.today().isoformat()}
Run: {state.get('run_id')}
Approved: {approved}
Reason: breaking_change gate in FeatureGraph Lab6
""",
    )
    if approved:
        return {
            "ceo_approved": True,
            "breaking_change": True,
            "status": "design",
            "messages": _msg(state, f"CEO approved → {note}"),
        }
    return {
        "ceo_approved": False,
        "status": "escalated",
        "blockers": ["CEO rejected breaking change"],
        "messages": _msg(state, f"CEO rejected → {note}"),
    }


def finalize(state: FeatureState) -> dict:
    write_text(
        "memory/task-memory/README.md",
        f"""# Task Memory

## Active

| Task ID | Title | Status | Assignee | Updated | Path |
|---------|-------|--------|----------|---------|------|
| TASK-0001 | Bootstrap Company OS repository | Done | Architect | 2026-07-15 | `tasks/TASK-0001-bootstrap-company-os.md` |
| TASK-0002 | Task Status + Audit Log | Done | Backend | {date.today().isoformat()} | `tasks/TASK-0002-task-status-audit.md` |

## Latest Lab Run

- run_id: {state.get('run_id')}
- prd: {state.get('prd_path')}
- architecture: {state.get('architecture_path')}
- review: {state.get('review_decision')} (cycles={state.get('review_cycles')})
- qa: {state.get('qa_decision')}
""",
    )
    return {
        "status": "done",
        "messages": _msg(state, "FeatureGraph finalize → done"),
    }


def route_after_prd(state: FeatureState) -> Literal["design", "clarify_pm"]:
    if state.get("open_questions"):
        return "clarify_pm"
    if state.get("prd_path") and count_acceptance_criteria(state["prd_path"]) >= 3:
        return "design"
    return "clarify_pm"


def route_after_design(state: FeatureState) -> Literal["implement_backend", "escalate", "clarify_pm"]:
    if state.get("status") == "escalate":
        return "escalate"
    if state.get("status") == "clarify":
        return "clarify_pm"
    if state.get("architecture_path"):
        return "implement_backend"
    return "clarify_pm"


def route_after_review(state: FeatureState) -> Literal["implement_backend", "qa"]:
    if state.get("review_decision") == "approve":
        return "qa"
    return "implement_backend"


def route_after_escalate(state: FeatureState) -> Literal["design", "finalize"]:
    if state.get("ceo_approved") is True:
        return "design"
    return "finalize"


def build_feature_graph(checkpointer: MemorySaver | None = None):
    g = StateGraph(FeatureState)
    g.add_node("intake", intake)
    g.add_node("write_prd", write_prd)
    g.add_node("clarify_pm", clarify_pm)
    g.add_node("design", design)
    g.add_node("implement_backend", implement_backend)
    g.add_node("review", review)
    g.add_node("qa", qa)
    g.add_node("escalate", escalate)
    g.add_node("finalize", finalize)

    g.add_edge(START, "intake")
    g.add_edge("intake", "write_prd")
    g.add_conditional_edges("write_prd", route_after_prd, ["design", "clarify_pm"])
    g.add_edge("clarify_pm", "write_prd")
    g.add_conditional_edges(
        "design", route_after_design, ["implement_backend", "escalate", "clarify_pm"]
    )
    g.add_edge("implement_backend", "review")
    g.add_conditional_edges("review", route_after_review, ["implement_backend", "qa"])
    g.add_edge("qa", "finalize")
    g.add_conditional_edges("escalate", route_after_escalate, ["design", "finalize"])
    g.add_edge("finalize", END)

    return g.compile(checkpointer=checkpointer or MemorySaver())


def run_feature(
    *,
    feature_request: str | None = None,
    breaking_change: bool = False,
    thread_id: str | None = None,
    resume: dict | None = None,
) -> FeatureState:
    graph = build_feature_graph()
    tid = thread_id or f"thread-{uuid.uuid4().hex[:8]}"
    config = {"configurable": {"thread_id": tid}}
    if resume is not None:
        return graph.invoke(Command(resume=resume), config=config)
    return graph.invoke(
        {
            "feature_request": feature_request or FEATURE_REQUEST,
            "breaking_change": breaking_change,
            "force_review_changes_once": True,
        },
        config=config,
    )
