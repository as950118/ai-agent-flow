# Project: AI Company Task Manager

## Overview

회사처럼 동작하는 Multi-Agent Task Management System.
LangGraph 기반으로 Agent가 PRD → 설계 → 구현 → 리뷰 → QA → 배포를 협업 수행한다.

## Status

| Field | Value |
|-------|-------|
| Phase | Foundation (Company OS) |
| Runtime | Designed (Markdown), Implementation pending |
| Primary Workflow | create-feature |

## Directory Layout (project-local)

```text
projects/ai-company-task-manager/
  README.md
  prd/
  architecture/
  adr/
  api/
```

## Current Focus

1. Company OS documents (complete in repo root)
2. LangGraph design docs (complete)
3. Next: Python runtime bootstrap + Operator API

## Key Links

- Collaboration rules: `docs/agent-collaboration-rules.md`
- Feature graph: `langgraph/feature-graph.md`
- Project memory: `memory/project-memory/README.md`
- Tech stack: `company/tech-stack.md`
