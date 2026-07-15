# PRD: Task Status Transitions + Audit Log

| Field | Value |
|-------|-------|
| PRD ID | PRD-EVAL-security |
| Status | Approved |
| Author | PM |
| Approver | CEO |
| Created | 2026-07-15 |
| Updated | 2026-07-15 |
| Project | AI Company Task Manager |
| Priority | P1 |

## 1. Problem Statement

Operator가 Task를 생성하고 상태(todo → in_progress → done)를 변경할 수 있어야 한다. 변경 시 actor, from, to, timestamp가 감사 로그로 남아 조회 가능해야 한다. 인증/인가와 보안 NFR도 필수.

Operator는 작업 진행 상태를 신뢰할 수 있게 추적해야 하며, 상태 변경의 감사 가능성이 필요하다.

## 2. Goals

- Goal 1: Task CRUD 및 상태 전이 API 제공
- Goal 2: 상태 변경 감사 로그(actor, from, to, timestamp) 저장 및 조회
- Goal 3: 산출물을 Company OS 문서 워크플로우로 추적

## 3. Non-Goals

- 복잡한 RBAC UI
- 실시간 협업 커서/웹소켓
- 외부 이슈트래커 양방향 동기화

## 4. Users & Personas

| Persona | Need |
|---------|------|
| Operator | Task 생성/상태 변경 |
| Auditor | 변경 이력 조회 |
| Agent System | Task Memory 연동 |

## 5. User Stories

1. As an Operator, I want to create a task, so that work is tracked.
2. As an Operator, I want to change task status along allowed transitions, so that progress is accurate.
3. As an Auditor, I want to list audit logs for a task, so that accountability is preserved.

## 6. Acceptance Criteria

- [ ] AC-1: `POST /api/v1/tasks`로 Task를 생성하면 `id`, `title`, `status=todo`가 반환된다.
- [ ] AC-2: 허용 전이(`todo→in_progress`, `in_progress→done`)만 성공하고 그 외는 409를 반환한다.
- [ ] AC-3: 상태 변경 시 audit log에 actor, from, to, timestamp가 저장된다.
- [ ] AC-4: `GET /api/v1/tasks/{id}/audit-logs`로 시간순 조회가 가능하다.
- [ ] AC-5: PRD/Architecture/ADR 없이 구현을 시작하지 않는다 (Company OS 규칙).

## 7. Scope

### In Scope

- Task 리소스 및 상태 전이
- Audit log persistence + read API

### Out of Scope

- Frontend Operator Console (Phase 2)
- Pagination advanced filters

## 8. Assumptions

- actor는 인증된 Operator ID 문자열이다.
- 단일 리전 PostgreSQL을 사용한다.

## 9. Non-Functional Requirements (Draft)

| NFR | Target | Notes |
|-----|--------|-------|
| Latency | p95 < 300ms | status change |
| Security | auth required | no public write |
| Observability | structured logs | include task_id |

## 10. Dependencies

- `company/tech-stack.md`
- `workflows/create-feature.md`
- Project memory excerpt:
  - length=1028 chars loaded

## 11. Open Questions

| # | Question | Owner | Due |
|---|----------|-------|-----|
| 1 | actor claim source (JWT sub vs API key name)? | Architect | TBD |

## 12. Success Metrics

| Metric | Baseline | Target |
|--------|----------|--------|
| Status change audit coverage | 0% | 100% |

## 13. References

- Collaboration: `docs/agent-collaboration-rules.md`
- Skill: `skills/write-prd.md`
- Template: `docs/prd-template.md`
