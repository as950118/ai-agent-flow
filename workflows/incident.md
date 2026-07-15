# Workflow: incident

## Trigger

- Monitoring alert / user report of service degradation
- Failed release with user impact
- Security event
- Manual Incident Declaration by DevOps/CEO

## Participants

| Stage | Role |
|-------|------|
| Commander | DevOps |
| Comms | PM (external/operator), CEO (SEV-1) |
| Mitigators | Backend, Frontend, DevOps |
| Analysis | Architect (design), QA (verification) |
| Docs | Technical Writer (postmortem polish) |

## Inputs

- Alert / symptom description
- Impact assessment
- Recent Deployments
- Runbooks / lessons-learned-memory

## Outputs

- Incident Ticket + Severity
- Timeline
- Mitigation actions
- Postmortem
- Action Items (Tasks)
- Lessons Learned Memory entry

## Approval Rules

| Action | Approver |
|--------|----------|
| Declare SEV-1 | DevOps + notify CEO/Operator immediately |
| Production Rollback | DevOps (SEV-1: inform CEO) |
| Public/Operator comms | PM (+ CEO if SEV-1) |
| Close Incident | DevOps + QA verify mitigation |

## Escalation Rules

| Condition | Escalate To |
|-----------|-------------|
| SEV-1 or unknown blast radius | CEO / Human Operator |
| Data loss / security breach | CEO + security owner |
| Mitigation ineffective in SLO window | CEO + Architect |
| Needs code fix for stable recovery | fix-bug Workflow after mitigate |

## Completion Conditions

- [ ] Impact mitigated or accepted with explicit owner
- [ ] Timeline + root cause (or contributing factors) documented
- [ ] Action Items created with owners/dates
- [ ] Lessons Learned filed
- [ ] Monitoring confirms stability window
