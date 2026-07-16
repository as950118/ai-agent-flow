from __future__ import annotations

from datetime import date

from company_os.repo import FEATURE_REQUEST, read_text, write_text


def build_prd(feature_request: str | None = None, prd_id: str = "PRD-0002") -> str:
    """Deterministic PRD writer aligned with docs/prd-template.md (Lab 2 / mock)."""
    req = feature_request or FEATURE_REQUEST
    template = read_text("docs/prd-template.md")
    _ = template  # ensure template is readable (Skill precondition)
    memory = read_text("memory/project-memory/README.md")
    today = date.today().isoformat()
    content = f"""# PRD: Task Status Transitions + Audit Log

| Field | Value |
|-------|-------|
| PRD ID | {prd_id} |
| Status | Approved |
| Author | PM |
| Approver | CEO |
| Created | {today} |
| Updated | {today} |
| Project | AI Company Task Manager |
| Priority | P1 |

## 1. Problem Statement

{req}

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
- [ ] AC-4: `GET /api/v1/tasks/{{id}}/audit-logs`로 시간순 조회가 가능하다.
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
  - length={len(memory)} chars loaded

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
"""
    path = f"projects/ai-company-task-manager/prd/{prd_id}-task-status-audit.md"
    write_text(path, content)
    return path


def build_architecture(prd_path: str) -> tuple[str, str]:
    today = date.today().isoformat()
    arch = f"""# Architecture: Task Status + Audit Log

| Field | Value |
|-------|-------|
| Doc ID | ARCH-0002 |
| Status | Approved |
| Author | Architect |
| Related PRD | {prd_path} |
| Created | {today} |

## 1. Context

Implement Task status transitions with immutable audit log entries, per approved PRD.

## 2. Proposed Architecture

```text
Operator → API (FastAPI) → TaskService → PostgreSQL
                              ↘ AuditLogWriter
LangGraph FeatureGraph orchestrates PM→…→QA docs, not runtime API path.
```

## 3. Components

| Component | Responsibility | Owner Role |
|-----------|----------------|------------|
| Task API | HTTP boundary | Backend |
| TaskService | transitions | Backend |
| AuditLog | append-only events | Backend |
| FeatureGraph | company workflow | Architect |

## 4. Data Model

- tasks(id, title, status, created_at, updated_at)
- task_audit_logs(id, task_id, actor, from_status, to_status, timestamp)

## 5. API Boundaries

- `POST /api/v1/tasks`
- `PATCH /api/v1/tasks/{{id}}/status`
- `GET /api/v1/tasks/{{id}}/audit-logs`

## 6. NFR

- Authn required; validate transition table; append-only audit rows.

## 7. ADRs

- ADR-0003 runtime package layout (capstone)
- ADR-0004 audit log append-only

## 8. Implementation Constraints

1. Do not mutate audit rows.
2. Reject illegal transitions with 409.
3. Follow `skills/create-api.md`.
"""
    adr = f"""# ADR-0004: Append-only Task Audit Log

| Field | Value |
|-------|-------|
| Status | Accepted |
| Date | {today} |
| Deciders | Architect |
| Related | {prd_path} |

## Context

Status changes must be accountable for Operators and Auditors.

## Decision

Store audit events in append-only `task_audit_logs` table. No updates/deletes in app layer.

## Consequences

### Positive
- Clear accountability trail

### Negative
- Storage grows with churn; add retention later via ADR

## Rejected Alternatives

| Option | Why Rejected |
|--------|--------------|
| Overscribe status on task only | Loses history |
| Soft-delete mutable history | Audit integrity weak |
"""
    arch_path = write_text(
        "projects/ai-company-task-manager/architecture/ARCH-0002-task-status-audit.md",
        arch,
    )
    adr_path = write_text(
        "projects/ai-company-task-manager/adr/ADR-0004-append-only-audit-log.md",
        adr,
    )
    write_text(
        "memory/decision-memory/ADR-0004-append-only-audit-log.md",
        adr,
    )
    return arch_path, adr_path


def count_acceptance_criteria(prd_path: str) -> int:
    text = read_text(prd_path)
    return sum(1 for line in text.splitlines() if line.strip().startswith("- [ ] AC-"))
