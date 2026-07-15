# PRD-0001: AI Company Task Manager — Foundation

| Field | Value |
|-------|-------|
| PRD ID | PRD-0001 |
| Status | Approved |
| Author | PM |
| Approver | CEO |
| Created | 2026-07-15 |
| Project | AI Company Task Manager |
| Priority | P0 |

## 1. Problem Statement

소프트웨어 팀을 모방한 Multi-Agent 협업이 문서·역할·워크플로우 없이 진행되면 추측 기반 실행과 감사 불가능한 결정이 발생한다. 운영 가능한 Company OS가 필요하다.

## 2. Goals

- Git-Markdown 기반 Company OS 구축
- Role / Skill / Workflow / Memory / Agent / LangGraph 설계 완성
- 이후 Runtime 구현의 입력 명세로 사용 가능하게 한다

## 3. Non-Goals

- 이 PRD 범위에서 전체 Product UI 완성
- 다중 LLM Provider 추상화의 최종 구현

## 4. Acceptance Criteria

- [x] AC-1: company/roles/skills/workflows/docs/agents/langgraph/memory 구조가 존재한다
- [x] AC-2: 각 Role에 Purpose~System Prompt 섹션이 있다
- [x] AC-3: Feature/BugFix/Release Graph 설계 문서가 있다
- [x] AC-4: Collaboration pipeline 문서 I/O가 정의되어 있다
- [x] AC-5: 초기 ADR 2건이 decision-memory에 있다

## 5. References

- ADR-0001, ADR-0002
- `docs/agent-collaboration-rules.md`
