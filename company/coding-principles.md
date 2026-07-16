# Coding Principles

## Source of Truth

코드와 함께 `docs/`, `tasks/`, ADR이 Single Source of Truth이다. 코드만 존재하고 문서가 없으면 Incomplete로 간주한다.

## Principles

### 1. Read Before Write

구현 전 반드시 확인:
- Task 문서
- PRD / Architecture / ADR
- 관련 Memory (decision, lessons-learned)
- Role Restrictions

### 2. Small, Reviewable Diffs

- PR은 하나의 의도(intent)만 담는다.
- Feature와 Refactor를 섞지 않는다.
- 테스트 없는 구현 PR을 금지한다 (spike 제외, spike는 명시).

### 3. Explicit Interfaces

- API는 OpenAPI/API Spec 문서 우선.
- Breaking Change는 ADR + Migration Plan 필수.
- 암묵적 계약(hidden side effect) 금지.

### 4. Fail Loud, Recover Gracefully

- 예외를 삼키지 않는다.
- 사용자/시스템에 영향 있는 실패는 Incident Workflow를 따른다.
- 재시도·타임아웃·멱등성을 기본으로 설계한다.

### 5. Test Pyramid

- Unit: 비즈니스 규칙
- Integration: 경계(API, DB, Queue)
- E2E: 핵심 Happy Path만
- QA Gate 통과 전 Release 금지

### 6. Security by Default

- Secret을 Repository에 커밋하지 않는다.
- Least Privilege
- Input Validation은 Boundary에서

### 7. Observability

- 핵심 경로에 structured log, metric, trace 고려
- Release 후 SLO/Alert 확인은 DevOps 책임

### 8. Language & Style

- 프로젝트 `tech-stack.md`와 모듈별 style guide를 따른다.
- 추측으로 새 패턴을 도입하지 않는다. 필요 시 ADR 작성 후 적용.

## Definition of Done (Code)

- [ ] Task Acceptance Criteria 충족
- [ ] 관련 테스트 통과
- [ ] Reviewer Approve
- [ ] QA Sign-off
- [ ] 문서(API Spec / ADR / README) 최신화
- [ ] Memory 갱신 (해당 시)
