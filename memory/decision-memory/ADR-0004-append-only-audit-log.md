# ADR-0004: Append-only Task Audit Log

| Field | Value |
|-------|-------|
| Status | Accepted |
| Date | 2026-07-15 |
| Deciders | Architect |
| Related | projects/ai-company-task-manager/prd/PRD-0002-task-status-audit.md |

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
