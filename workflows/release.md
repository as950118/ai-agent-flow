# Workflow: release

## Trigger

- QA Sign-off for a releasable increment
- Scheduled release train
- Hotfix after fix-bug / incident mitigation
- LangGraph `ReleaseGraph` 시작

## Participants

| Stage | Role |
|-------|------|
| Prep | PM (notes), Backend (migrations), DevOps |
| Approve | QA, Architect (migrations/breaking), CEO (major/prod risk) |
| Execute | DevOps |
| Verify | QA + DevOps |
| Communicate | PM / Technical Writer |

## Inputs

- Change list / version
- QA Sign-off
- Migration & Rollback plan
- Feature flag state
- Release Notes draft

## Outputs

- Deployment Record
- Git Tag / Changelog
- Verification Evidence
- Rollback Record (if executed)
- Project Memory update

## Approval Rules

| Environment | Approvers |
|-------------|-----------|
| Staging | DevOps (CI green) |
| Production Minor | DevOps + QA Sign-off |
| Production Major / Breaking | DevOps + QA + Architect + CEO |
| Emergency Hotfix | DevOps + CEO (QA parallel verify) |

## Escalation Rules

| Condition | Escalate To |
|-----------|-------------|
| Missing Sign-off | QA / PM |
| Migration risk unclear | Architect |
| Post-deploy SLO breach | Incident Workflow |
| Approval deadlock | CEO |

## Completion Conditions

- [ ] Target env healthy against release checklist
- [ ] Tag + Deployment Record stored
- [ ] Stakeholders notified
- [ ] Deferred items ticketed
- [ ] No open SEV-1 introduced by release (or incident opened)
