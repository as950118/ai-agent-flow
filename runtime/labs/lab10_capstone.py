from __future__ import annotations

from datetime import date

from company_os.bugfix_graph import run_bugfix
from company_os.feature_graph import build_feature_graph
from company_os.repo import FEATURE_REQUEST, write_text


def main() -> None:
    print("=== Lab 10: Capstone Demo ===")
    feature = build_feature_graph().invoke(
        {
            "feature_request": FEATURE_REQUEST,
            "force_review_changes_once": True,
        },
        config={"configurable": {"thread_id": "capstone-feature"}},
    )
    bug = run_bugfix("감사 로그에 actor 누락")

    adr = write_text(
        "memory/decision-memory/ADR-0003-runtime-package-layout.md",
        f"""# ADR-0003: Runtime Package Layout

| Field | Value |
|-------|-------|
| Status | Accepted |
| Date | {date.today().isoformat()} |
| Deciders | Architect |

## Context

Labs need an executable Python package beside Markdown Company OS docs.

## Decision

Place runtime under `runtime/` with `company_os/` library and `labs/` entrypoints, managed by `uv`.

## Consequences

### Positive
- Clear separation of docs vs executable labs
- Reusable FeatureGraph/BugFixGraph modules

### Negative
- Dual mental model (Markdown SoT + Python runtime)

## Rejected Alternatives

| Option | Why Rejected |
|--------|--------------|
| Scripts scattered at repo root | Hard to package/test |
| Notebooks only | Weak CI / weak graph reuse |
""",
    )

    notes = write_text(
        "labs/notes/capstone.md",
        f"""# Capstone Demo Notes

Date: {date.today().isoformat()}

## FeatureGraph
- status: {feature.get('status')}
- prd: {feature.get('prd_path')}
- architecture: {feature.get('architecture_path')}
- review_cycles: {feature.get('review_cycles')}
- qa: {feature.get('qa_decision')}

## BugFixGraph
- status: {bug.get('status')}
- fix: {bug.get('fix_notes_path')}

## ADR
- {adr}

## Demo Script
1. Show Feature Request
2. Walk messages (PM→Arch→Backend→Review→QA)
3. Show review reject once then approve
4. Show BugFix path for actor missing
5. Open LangSmith if keys configured
""",
    )
    print("feature:", feature.get("status"), feature.get("prd_path"))
    print("bug:", bug.get("status"), bug.get("fix_notes_path"))
    print("adr:", adr)
    print("notes:", notes)
    assert feature.get("status") == "done" and bug.get("status") == "done"
    print("DoD: Capstone artifacts written")


if __name__ == "__main__":
    main()
