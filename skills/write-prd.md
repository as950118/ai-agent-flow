# Skill: write-prd

## Goal

모호함 없는 PRD를 작성하여 Architect/구현 Agent가 추측 없이 진행하게 한다.

## Preconditions

- Priority Directive 또는 승인된 요청 존재
- prd-template.md 사용
- 관련 Project Memory / 기존 Feature 문서 열람

## Inputs

| Input | Source |
|-------|--------|
| Problem statement | Operator / CEO / Issue |
| Users & goals | research / memory |
| Constraints | tech-stack, compliance |
| Open questions | stakeholder |

## Procedure

1. Problem / Why Now를 한 단락으로 정의한다.
2. Goals / Non-Goals를 분리한다.
3. User Stories + Acceptance Criteria(검증 가능)를 작성한다.
4. In Scope / Out of Scope / Assumptions을 명시한다.
5. NFR 초안(성능, 보안, 가용성)을 기입하고 Architect 검토용으로 표시한다.
6. Open Questions에 owner와 due를 붙인다.
7. PM 자체 체크 후 Design Request로 Architect에 Handoff한다.

## Outputs

- PRD document
- Design Request summary
- Linked Task stubs (optional)

## Failure Handling

| Failure | Action |
|---------|--------|
| Conflicting stakeholder goals | Escalate to CEO |
| Unknown user impact | Research spike task |
| Template fields empty | Do not hand off |

## Examples

- Feature: "Task 상태 변경 감사 로그"
- AC: "상태 변경 시 actor, from, to, timestamp가 저장되고 API로 조회 가능하다"
