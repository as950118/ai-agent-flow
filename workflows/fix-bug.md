# Workflow: fix-bug

## Trigger

- QA/Operator/Monitoring이 Bug를 보고
- Production Defect 또는 Regression
- LangGraph `BugFixGraph` 시작

## Participants

| Stage | Role |
|-------|------|
| Triage | PM (+ QA) |
| Reproduce | QA / Backend |
| Fix | Backend and/or Frontend |
| Review | Reviewer |
| Verify | QA |
| Hotfix Release | DevOps |
| High SEV | CEO |

## Inputs

- Bug Report (repro, expected/actual, severity, env)
- Related PRD/ADR/Code links
- Incident link (if any)

## Outputs

- Bug Task
- Fix PR + Tests (regression)
- Review Approve
- QA Verification
- Deployment / Hotfix Record
- Lessons Learned (비정상 패턴 시)

## Approval Rules

| Gate | Approver | Notes |
|------|----------|-------|
| Severity & Priority | PM (SEV-1 with CEO) | Triage |
| Fix Merge | Reviewer | Required except documented emergency path |
| Verify | QA | Required |
| Prod Hotfix | DevOps + CEO if SEV-1 | Rollback plan required |

## Escalation Rules

| Condition | Escalate To |
|-----------|-------------|
| Cannot reproduce | QA + reporter; PM may defer |
| Root cause in design | Architect |
| SEV-1 user impact | CEO + Incident Workflow |
| Fix causes wider regression | Architect + DevOps rollback |

## Completion Conditions

- [ ] Repro confirmed fixed in target env
- [ ] Regression test added (unless justified waiver)
- [ ] Reviewer Approve (or emergency waiver documented)
- [ ] QA Pass
- [ ] Task closed + Memory note if systemic
