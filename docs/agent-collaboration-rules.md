# Agent Collaboration Rules

## Canonical Pipeline

```
PM → Architect → Backend → Reviewer → QA → Release(DevOps)
```

Frontend는 UI 범위가 있을 때 Backend와 병렬 가능하나, **API Contract Approved** 이후에 Integration을 확정한다.

## Stage Contracts

| Stage | Actor | Input Documents | Output Documents | Next |
|-------|-------|-----------------|------------------|------|
| 1. Discover & Scope | PM | Request, Priority Directive, Project Memory | PRD, Task stubs, Design Request | Architect |
| 2. Design | Architect | PRD, tech-stack, decision-memory | Architecture, ADR(s), Design Pack, API Outline | Backend (/Frontend) |
| 3. Implement | Backend (/Frontend) | Design Pack, Tasks, Skills | Code, Tests, API Spec, Implementation Notes, PR Pack | Reviewer |
| 4. Review | Reviewer | PR Pack, Architecture, ADR, coding-principles | Review Report + Approve/Changes/Block | QA (if Approve) or Implementers |
| 5. QA | QA | Approved build, PRD AC, NFR | Test Plan/Report, Bugs or Sign-off | DevOps (if Sign-off) |
| 6. Release | DevOps | Sign-off, Release Notes, Rollback Plan | Deployment Record, Tag | Done / Incident |

## Document Ownership

| Document | Owner | Contributors |
|----------|-------|--------------|
| PRD | PM | CEO, TW |
| Architecture | Architect | Backend, DevOps |
| ADR | Architect | CEO (approve high-risk) |
| API Spec | Backend | Architect, Frontend |
| Task | Creating Role | Assignee |
| Review Report | Reviewer | — |
| Test Report | QA | — |
| Deployment Record | DevOps | — |
| Postmortem | DevOps | Architect, PM, TW |

## Rules of Engagement

1. **No skipping gates** without documented emergency path.
2. **No silent scope change** — PM owns scope; Architect owns technical boundary.
3. **Handoff without required artifact = invalid**.
4. **Questions over guesses** — missing info → Clarification Request.
5. **Memory write-back** — decisions, incidents, lessons must be filed.
6. **Self-approve forbidden** for Reviewer on own primary authorship.

## Parallelism Matrix

| Parallel OK? | Pairs |
|--------------|-------|
| Yes | Backend ‖ Frontend (after API Outline) |
| Yes | TW doc polish ‖ Implementation |
| No | QA before Reviewer Approve |
| No | Prod Release before QA Sign-off (except CEO emergency) |
| No | Implementation before Architecture Approve (except spike) |
