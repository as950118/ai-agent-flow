# Skill: write-test

## Goal

변경된 동작에 대해 실패를 재현·방지하는 자동 테스트를 작성한다.

## Preconditions

- 테스트 대상 동작이 AC 또는 Bug Report로 명시됨
- 실행 환경/프레임워크가 tech-stack과 일치
- Spike가 아닌 경우 DoD에 테스트 포함

## Inputs

| Input | Source |
|-------|--------|
| Behavior under test | PRD AC / Bug / Architecture NFR |
| Existing test patterns | codebase |
| Risk areas | Reviewer/QA notes |

## Procedure

1. 검증할 동작을 Given/When/Then으로 고정한다.
2. 테스트 레벨을 선택한다 (Unit / Integration / E2E).
3. 기존 fixture/mock 패턴을 재사용한다.
4. Happy path + 최소 1개의 실패/경계 경로를 작성한다.
5. 테스트를 실행하고 녹색을 확인한다.
6. Flaky 가능성이 있으면 원인 제거 또는 명시적 skip + ticket.
7. QA Test Plan에 매핑되는 항목을 기록한다.

## Outputs

- Test code
- Test execution evidence (log/summary)
- Gaps list (자동화 불가 항목)

## Failure Handling

| Failure | Action |
|---------|--------|
| Untestable design | Architect에 testability issue |
| Env dependency failure | DevOps에 환경 이슈 |
| Flaky test | Quarantine + root cause task |
| AC ambiguous | PM Clarification — do not invent asserts |

## Examples

- Unit: task status transition invalid → domain error
- Integration: `POST /tasks` persists and returns 201
