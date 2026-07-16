# Skill: release-service

## Goal

승인된 변경을 대상 환경에 안전히 배포하고, 검증·기록·필요 시 Rollback까지 완수한다.

## Preconditions

- QA Sign-off (또는 Emergency Path 승인)
- Approval Rules 충족 (workflows/release.md)
- Changelog / Release Notes draft
- Rollback plan 존재

## Inputs

| Input | Source |
|-------|--------|
| Artifact version | CI build |
| QA Sign-off | QA |
| Migration notes | Backend/Architect |
| Feature flags | config |

## Procedure

1. Pre-flight: CI green, migrations reviewed, secrets present in vault (not git).
2. Deploy to staging → smoke checks.
3. Production Approval Gate 확인.
4. Deploy production (canary/rolling if defined).
5. Post-deploy verification (health, golden transactions, error rate).
6. Tag release + write Deployment Record.
7. 이상 시 Rollback Procedure 실행 후 Incident 연계.
8. Lessons/observations를 project-memory에 요약.

## Outputs

- Deployment Record
- Release Tag / Notes
- Verification Evidence
- Rollback Record (if any)

## Failure Handling

| Failure | Action |
|---------|--------|
| Smoke fail on staging | Abort prod; return to Backend/QA |
| Prod SLO breach | Rollback → incident-analysis |
| Migration fail | Stop; restore per runbook; escalate Architect |
| Missing approval | Do not deploy |

## Examples

- Minor release: patch task API → staging smoke → prod rolling → verify GET/POST tasks
