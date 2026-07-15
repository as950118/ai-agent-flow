# Skill: create-api

## Goal

Architecture와 Task AC에 맞는 API를 설계·구현하고 OpenAPI/API Spec과 코드를 동기화한다.

## Preconditions

- Approved Architecture / ADR 존재
- Task 문서에 endpoint 범위가 명시됨
- tech-stack.md의 API 스타일(REST + OpenAPI) 확인
- 유사 기존 API 구현 최소 2개 분석 완료

## Inputs

| Input | Source |
|-------|--------|
| Task Pack | `tasks/` |
| Architecture | project docs |
| API Spec Outline | Architect / existing spec |
| Domain model notes | Architecture |

## Procedure

1. Endpoint 목록과 Resource를 Task/Architecture에서 추출한다.
2. `docs/api-spec-template.md`로 Spec Draft를 작성한다 (path, method, request/response, errors).
3. Validation, authz, idempotency, pagination 규칙을 Boundary에 정의한다.
4. 기존 모듈 패턴에 맞춰 handler/service/repository를 구현한다.
5. Unit + Integration Test를 추가한다 (`write-test` Skill 연계).
6. Spec과 구현 Diff를 대조하고 drift가 없으면 PR Pack을 만든다.
7. Breaking Change면 중단하고 Architect에게 ADR을 요청한다.

## Outputs

- Updated API Spec
- Implementation code + tests
- Implementation Notes (assumptions, deviations)

## Failure Handling

| Failure | Action |
|---------|--------|
| AC/Architecture conflict | Stop → Architect/PM Clarification |
| Spec-code drift | Fix before Reviewer handoff |
| Auth/security unclear | Escalate to Architect |
| Missing similar pattern | Document new pattern + propose ADR |

## Examples

- `POST /tasks` 생성 API: validation errors 400, unauthorized 401, created 201
- `GET /tasks/{id}`: not found 404 with standard error envelope
