from __future__ import annotations

import operator
from typing import Annotated, Any, TypedDict


class FeatureState(TypedDict, total=False):
    run_id: str
    project_id: str
    feature_request: str
    priority: str
    prd_path: str
    architecture_path: str
    adr_paths: Annotated[list[str], operator.add]
    task_paths: Annotated[list[str], operator.add]
    api_spec_path: str
    impl_notes_path: str
    review_decision: str
    review_report_path: str
    review_cycles: int
    qa_decision: str
    qa_report_path: str
    open_questions: list[str]
    blockers: list[str]
    artifacts: dict[str, str]
    escalation: dict[str, Any]
    status: str
    needs_frontend: bool
    release_requested: bool
    breaking_change: bool
    ceo_approved: bool | None
    force_review_changes_once: bool
    messages: Annotated[list[str], operator.add]


class BugFixState(TypedDict, total=False):
    run_id: str
    project_id: str
    bug_summary: str
    severity: str
    priority: str
    reproducible: bool
    root_cause: str
    task_path: str
    fix_notes_path: str
    review_decision: str
    qa_decision: str
    hotfix: bool
    status: str
    messages: Annotated[list[str], operator.add]
