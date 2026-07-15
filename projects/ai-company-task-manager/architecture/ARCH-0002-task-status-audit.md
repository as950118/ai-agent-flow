# Architecture: Task Status + Audit Log

| Field | Value |
|-------|-------|
| Doc ID | ARCH-0002 |
| Status | Approved |
| Author | Architect |
| Related PRD | projects/ai-company-task-manager/prd/PRD-0002-task-status-audit.md |
| Created | 2026-07-15 |

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
- `PATCH /api/v1/tasks/{id}/status`
- `GET /api/v1/tasks/{id}/audit-logs`

## 6. NFR

- Authn required; validate transition table; append-only audit rows.

## 7. ADRs

- ADR-0003 runtime package layout (capstone)
- ADR-0004 audit log append-only

## 8. Implementation Constraints

1. Do not mutate audit rows.
2. Reject illegal transitions with 409.
3. Follow `skills/create-api.md`.
