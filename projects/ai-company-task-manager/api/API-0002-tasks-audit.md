# API Spec: Tasks + Audit Logs

| Field | Value |
|-------|-------|
| Spec ID | API-0002 |
| Version | v0.1.0 |
| Status | Draft |
| Owner | Backend |
| Related | projects/ai-company-task-manager/prd/PRD-0002-task-status-audit.md / projects/ai-company-task-manager/architecture/ARCH-0002-task-status-audit.md |

## Endpoints

### POST /api/v1/tasks
Creates task with status=todo.

### PATCH /api/v1/tasks/{id}/status
Body: `{"status":"in_progress"|"done", "actor":"..."}`
Illegal transition → 409.

### GET /api/v1/tasks/{id}/audit-logs
Returns append-only events: actor, from, to, timestamp.


### Audit event schema
actor: string (required)
