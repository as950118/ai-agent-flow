# API Spec: {{TITLE}}

| Field | Value |
|-------|-------|
| Spec ID | API-{{NNNN}} |
| Version | v0.1.0 |
| Status | Draft / Approved |
| Owner | Backend |
| Related | PRD- / ARCH- / ADR- |
| Base URL | `/api/v1` |

## 1. Conventions

- Format: JSON
- Auth: `Authorization: Bearer <token>` (or API Key)
- Error envelope:

```json
{
  "error": {
    "code": "STRING_CODE",
    "message": "Human readable",
    "details": []
  }
}
```

- Pagination: `limit`, `cursor` (or `page`)

## 2. Endpoints

### 2.1 {{METHOD}} {{PATH}}

| Item | Value |
|------|-------|
| Summary | |
| Auth | Required / Optional |
| Idempotent | Yes / No |

#### Request

Headers:

| Header | Required | Description |
|--------|----------|-------------|
| Content-Type | Yes | application/json |

Body:

```json
{
  "field": "type"
}
```

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| | | | |

#### Responses

| Status | Meaning | Body |
|--------|---------|------|
| 200/201 | Success | |
| 400 | Validation | error envelope |
| 401 | Unauthorized | |
| 403 | Forbidden | |
| 404 | Not Found | |
| 409 | Conflict | |
| 500 | Server Error | |

#### Example

```http
POST /api/v1/tasks HTTP/1.1
Content-Type: application/json

{"title":"Example"}
```

```json
{
  "id": "tsk_123",
  "title": "Example",
  "status": "todo"
}
```

## 3. Schemas

### Task

| Field | Type | Description |
|-------|------|-------------|
| id | string | |
| title | string | |
| status | enum | todo, in_progress, blocked, done, cancelled |
| assignee_role | string | |
| created_at | datetime | |
| updated_at | datetime | |

## 4. Changelog

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | | Initial |
