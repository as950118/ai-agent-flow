# Skill: incident-analysis

## Goal

장애를 신속히 완화하고, Timeline·Root Cause·Action Items를 남겨 재발을 방지한다.

## Preconditions

- Incident가 선언됨 (증상 + 영향 범위)
- DevOps가 Coordinator (SEV-1은 CEO/Operator 참여)
- 로그/메트릭/최근 배포 정보에 접근 가능

## Inputs

| Input | Source |
|-------|--------|
| Symptoms & reports | users / monitors |
| Recent changes | Release records |
| Runbooks | docs / memory |
| Logs/metrics/traces | observability |

## Procedure

1. Severity를 분류한다 (SEV-1..4) 및 커뮤니케이션 채널을 연다.
2. User Impact를 고정한다 (누가, 무엇이, 얼마나).
3. Mitigate first: rollback, feature flag, traffic shed.
4. Timeline을 분 단위로 기록한다.
5. Hypotheses를 세우고 증거로 확인/기각한다.
6. Root Cause (트리거 + 잠재 결함)를 분리한다.
7. Action Items를 예방/탐지/복구로 분류해 Task화한다.
8. Postmortem을 lessons-learned-memory에 저장한다.

## Outputs

- Incident Report
- Mitigation Record
- Postmortem + Lessons Learned
- Follow-up Tasks

## Failure Handling

| Failure | Action |
|---------|--------|
| Cannot mitigate quickly | Escalate SEV, engage CEO/Operator |
| Unknown root cause within window | Document contributing factors; keep investigation open |
| Recurring same class | Priority bump + Architecture review |

## Examples

- SEV-2: API 5xx spike after release → rollback → bad null handling in new endpoint
