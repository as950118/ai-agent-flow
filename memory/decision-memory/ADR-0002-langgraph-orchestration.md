# ADR-0002: Use LangGraph for Multi-Agent Orchestration

| Field | Value |
|-------|-------|
| Status | Accepted |
| Date | 2026-07-15 |
| Deciders | Architect, CEO |

## Context

Feature/Bug/Release는 상태·승인 게이트·재시도가 있는 워크플로우이다. 단순 chain/prompt chaining으로는 gate와 escalation을 명확히 모델링하기 어렵다.

## Decision

Agent Orchestration 표준으로 LangGraph를 채택한다. FeatureGraph, BugFixGraph, ReleaseGraph를 1급 아티팩트로 설계·구현한다.

## Consequences

### Positive

- Explicit state & conditional edges
- Human-in-the-loop escalation nodes
- Workflow 문서와 그래프 구조 정렬 용이

### Negative

- 팀의 LangGraph 학습 비용
- 그래프 복잡도 관리 필요

## Rejected Alternatives

| Option | Why Rejected |
|--------|--------------|
| Ad-hoc Python scripts | 상태/게이트 비표준 |
| Pure Chat Orchestration | 재현·감사 취약 |
| Second framework in parallel | 운영 복잡도; 별도 ADR 없이 금지 |
