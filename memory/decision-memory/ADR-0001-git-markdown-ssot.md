# ADR-0001: Adopt Git-Markdown Company OS as SSOT

| Field | Value |
|-------|-------|
| Status | Accepted |
| Date | 2026-07-15 |
| Deciders | Architect, CEO |

## Context

Multi-Agent 시스템이 암묵지에 의존하면 환각·재작업·감사불능이 발생한다. 실제 회사는 문서·티켓·결정 기록으로 운영된다.

## Decision

모든 회사 지식(Role, Skill, Workflow, Memory, Spec)의 Single Source of Truth를 Git Repository 내 Markdown으로 둔다.

## Consequences

### Positive

- Agent가 동일 근거를 공유
- 리뷰·감사가 diff로 가능
- Onboarding 비용 감소

### Negative

- 문서 갱신 규율이 필요
- 대규모 검색을 위한 인덱싱/툴링이 필요할 수 있음

## Rejected Alternatives

| Option | Why Rejected |
|--------|--------------|
| Wiki-only outside git | 코드/에이전트 설정과 drift |
| DB-only knowledge | 리뷰·브랜치·PR 워크플로와 단절 |
| Prompt-only memory | 비영구·비감사 |
