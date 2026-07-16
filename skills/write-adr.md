# Skill: write-adr

## Goal

기술/구조 결정을 재현 가능하고 거부 대안이 포함된 ADR로 남긴다.

## Preconditions

- 결정이 필요한 Context가 존재 (PRD constraint, incident, debt)
- adr-template.md 사용
- 관련 Decision Memory 검색 완료 (중복 결정 방지)

## Inputs

| Input | Source |
|-------|--------|
| Context & forces | Architecture discussion |
| Options | research / spike |
| Constraints | tech-stack, security, cost |

## Procedure

1. Decision Memory에서 유사 ADR을 검색한다.
2. Context와 Decision Drivers를 작성한다.
3. Options ≥ 2를 비교한다 (trade-offs).
4. Decision과 Consequences(긍정/부정)를 기록한다.
5. Rejected Alternatives와 이유를 남긴다.
6. Status(Proposed/Accepted/Deprecated)와 Approver를 명시한다.
7. decision-memory 인덱스에 링크를 추가한다.
8. 영향받는 Architecture/Task 문서를 갱신한다.

## Outputs

- ADR Markdown
- Decision Memory index update
- Links from Architecture Doc

## Failure Handling

| Failure | Action |
|---------|--------|
| Only one option listed | Expand analysis before Accept |
| High-risk without CEO/Operator | Hold on Proposed |
| Conflicts existing ADR | Explicitly supersede or reconcile |

## Examples

- ADR-001: LangGraph를 Orchestration 표준으로 채택
- ADR-002: Task 상태를 enum + transition table로 관리
