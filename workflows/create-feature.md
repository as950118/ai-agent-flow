# Workflow: create-feature

## Trigger

- CEO Priority Directive 또는 Operator Feature Request
- PM이 PRD 작성을 시작하기로 결정
- LangGraph `FeatureGraph` 시작 이벤트

## Participants

| Stage | Role |
|-------|------|
| Scope | PM |
| Design | Architect |
| Implement | Backend, Frontend (필요 시) |
| Review | Reviewer |
| Verify | QA |
| Release | DevOps |
| Oversight | CEO (strategic / high-risk) |
| Docs | Technical Writer (지원) |

## Inputs

- Feature Request / Priority Directive
- Project Memory
- Templates: PRD, Architecture, ADR, Task

## Outputs

- PRD, Architecture, ADR(s)
- Tasks, Code, Tests, API Spec
- Review Report, QA Sign-off
- (optional) Release via release workflow
- Memory updates

## Approval Rules

| Gate | Approver | Required Artifact |
|------|----------|-------------------|
| PRD Ready | PM (+ CEO if strategic) | PRD complete |
| Design Ready | Architect (+ CEO if high-risk ADR) | Architecture + ADR |
| Code Ready | Reviewer | Approve |
| Quality Ready | QA | Sign-off |
| Prod Release | DevOps + rules in `release` | QA Sign-off |

## Escalation Rules

| Condition | Escalate To |
|-----------|-------------|
| Scope conflict / priority clash | CEO |
| Feasibility or NFR unmet | Architect → PM → (CEO if needed) |
| Security blocker | Reviewer → Architect → CEO |
| AC ambiguity blocking QA | PM |
| >2 review cycles unresolved | Architect |

## Completion Conditions

- [ ] All Acceptance Criteria verified by QA
- [ ] Reviewer Approve recorded
- [ ] Docs (API/ADR/PRD) synced
- [ ] Task status = Done
- [ ] Relevant Memory updated
- [ ] If production intended: release workflow completed or explicitly deferred

## Stage I/O Summary

```
PM        → PRD + Design Request
Architect → Architecture + ADR + Design Pack
Backend/FE→ Code + Tests + Spec + PR Pack
Reviewer  → Approval Record
QA        → Test Report + Sign-off
DevOps    → Deployment Record (if releasing)
```
