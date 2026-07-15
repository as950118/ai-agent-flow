# Tech Stack

## Product: AI Company Task Manager

회사처럼 동작하는 Multi-Agent Task Management System.

## Core Runtime

| Layer | Technology | Purpose |
|-------|------------|---------|
| Agent Orchestration | LangGraph | Multi-Agent Workflow Graph |
| Agent Framework | LangChain (optional helpers) | Tool / Prompt utilities |
| LLM Provider | **OpenRouter** (default) / OpenAI | Reasoning via OpenAI-compatible API |
| Language | Python 3.11+ | Agent runtime & services |
| API | FastAPI | External / Operator API |
| Data Store | PostgreSQL | Tasks, Projects, Audit |
| Cache / Queue | Redis | State, pub/sub, locks |
| Vector Memory (optional) | pgvector / Chroma | Semantic memory retrieval |
| Packaging | Poetry / uv | Dependency management |

## Documentation & Knowledge

| Asset | Format | Location |
|-------|--------|----------|
| Company OS | Markdown | `company/`, `roles/`, `skills/`, `workflows/` |
| Specs | Markdown | `docs/`, `projects/` |
| Decisions | ADR Markdown | `docs/adr/` or `memory/decision-memory/` |
| Agent Config | YAML | `agents/` |
| Graphs | Python + Markdown design | `langgraph/` |

## Engineering Defaults

| Concern | Default |
|---------|---------|
| API Style | REST + OpenAPI 3 |
| Auth (Operator) | API Key / OAuth2 (env-based) |
| Config | Environment variables + `.env.example` |
| CI | GitHub Actions / GitLab CI |
| Container | Docker |
| IaC (later) | Terraform (when multi-env) |
| Observability | OpenTelemetry + structured JSON logs |

## Frontend (Operator Console — Phase 2)

| Layer | Technology |
|-------|------------|
| Framework | Next.js / React |
| Styling | Project-defined CSS variables |
| State | Server-driven + light client state |

## Forbidden / Avoid Unless ADR

- Undocumented third-party SaaS for core workflow
- Storing secrets in git
- Skipping Reviewer/QA in production paths
- Introducing a second orchestration framework alongside LangGraph without ADR

## Version Policy

- Pin major versions in lockfile
- Upgrade via explicit task + ADR when breaking
