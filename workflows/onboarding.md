# Workflow: onboarding

## Trigger

- New Human Operator joins
- New Agent Role/Skill added to Company OS
- New Project bootstrapped under `projects/`

## Participants

| Stage | Role |
|-------|------|
| Facilitate | Technical Writer + PM |
| Access/Env | DevOps |
| Architecture briefing | Architect |
| Priority context | CEO |
| Practice task | Backend/QA (sample) |

## Inputs

- New member/agent profile
- Company OS docs (`company/`, `roles/`, `workflows/`)
- Project README
- Sandbox credentials (out of band)

## Outputs

- Onboarding Checklist completion record
- Access granted confirmation (no secrets in git)
- First Practice Task result
- Doc gap tickets (if any)
- Updated Glossary if new terms

## Approval Rules

| Gate | Approver |
|------|----------|
| Production access | DevOps + CEO/Operator |
| Agent enabled in prod graphs | Architect + CEO |
| Onboarding complete | PM sign-off |

## Escalation Rules

| Condition | Escalate To |
|-----------|-------------|
| Missing critical docs | Technical Writer → owners |
| Access blocked | DevOps → CEO |
| Role ambiguity | CEO |

## Completion Conditions

- [ ] Read: vision, mission, values, org-chart, glossary
- [ ] Read: assigned Role + primary Workflows/Skills
- [ ] Completed Practice Task without guessing (asked or used Memory)
- [ ] Knows Escalation path
- [ ] Checklist stored under project or memory

## Onboarding Checklist (Human / Agent)

1. Clone repo and open `README.md`
2. Read `company/*`
3. Read own `roles/*.md`
4. Skim `workflows/create-feature.md` and `fix-bug.md`
5. Open active project under `projects/`
6. Find one ADR in decision-memory
7. Run/observe a dry-run graph if available
8. Submit Onboarding Note: questions + doc gaps
