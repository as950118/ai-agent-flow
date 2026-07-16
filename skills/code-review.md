# Skill: code-review

## Goal

PR Pack이 Coding Principles, Architecture, ADR, Security, Test Adequacy를 충족하는지 검증한다.

## Preconditions

- PR Pack 존재 (diff, tests, notes, linked Task/PRD/Architecture)
- Reviewer Role로 실행
- 동일 변경의 주 작성자가 아닌 독립 Review

## Inputs

| Input | Source |
|-------|--------|
| Diff / PR | VCS |
| Task + AC | `tasks/` |
| Architecture + ADR | docs / decision-memory |
| coding-principles.md | `company/` |

## Procedure

1. Scope 확인: PR intent가 Task와 일치하는가.
2. Correctness: AC/edge case 처리 여부.
3. Architecture alignment: silent redesign 여부.
4. Security: secrets, injection, authz bypass.
5. Tests: 실패 가능 경로와 회귀 커버.
6. Maintainability: naming, duplication, dead code.
7. Findings를 Blocker/Major/Minor/Nit로 분류.
8. Decision: Approve / Changes Requested / Block — 근거를 Review Report에 기록.

## Outputs

- Review Report
- Decision + required follow-ups

## Failure Handling

| Failure | Action |
|---------|--------|
| Incomplete PR Pack | Request missing artifacts; do not Approve |
| Design drift | Block + Architect Drift Report |
| Secret found | Immediate Block + rotate guidance to DevOps |
| Disagreement on taste-only nits | Do not Block; leave Nit |

## Examples

- Blocker: production secret in commit
- Major: no tests for new business rule
- Minor: inconsistent error message format
