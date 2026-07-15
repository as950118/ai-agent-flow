# Project Memory: AI Company Task Manager

| Field | Value |
|-------|-------|
| Project ID | proj-ai-company-task-manager |
| Status | Founding |
| Owners | CEO, PM, Architect |

## Context

Multi-Agent Task Management System. Agents collaborate via LangGraph across PRD → Design → Implement → Review → QA → Release.

## Constraints

- Knowledge SSOT = this Git repository (Markdown)
- Stack defaults = `company/tech-stack.md`
- No production secrets in git

## Agreements

| Date | Agreement | Parties |
|------|-----------|---------|
| 2026-07-15 | Company OS docs bootstrap before runtime code | Architect, CEO |
| 2026-07-15 | Canonical pipeline PM→Architect→Backend→Reviewer→QA→Release | All roles |

## Active Risks

| Risk | Mitigation |
|------|------------|
| Doc/runtime drift | Markdown designs remain SoT until Python graphs land |
| Over-agent sprawl | Stick to defined roles; new role requires CEO+ADR |

## Links

- Project folder: `projects/ai-company-task-manager/`
- Decision index: `memory/decision-memory/`
