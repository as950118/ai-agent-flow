# AI Company Task Manager — Company Operating System

실제 소프트웨어 회사를 모방한 **Multi-Agent Company OS** Repository다.  
모든 지식은 Git 내 Markdown으로 관리되며, Agent는 Role·Skill·Workflow·Memory를 읽고 추측 없이 협업한다.

## Quick Start

1. `company/vision.md` → `mission.md` → `values.md` → `org-chart.md` 읽기
2. 자신의 `roles/<role>.md` 읽기
3. `docs/agent-collaboration-rules.md`로 파이프라인 이해
4. `workflows/`에서 수행할 워크플로우 선택
5. `agents/<role>.yaml`을 runtime에 로드 (구현 단계)
6. `langgraph/*-graph.md`를 보고 Graph 실행

## Repository Tree

```text
ai-agent-flow/
├── README.md
├── company/
│   ├── vision.md
│   ├── mission.md
│   ├── values.md
│   ├── org-chart.md
│   ├── coding-principles.md
│   ├── tech-stack.md
│   └── glossary.md
├── roles/
│   ├── ceo.md
│   ├── pm.md
│   ├── architect.md
│   ├── backend.md
│   ├── frontend.md
│   ├── reviewer.md
│   ├── qa.md
│   ├── devops.md
│   └── technical-writer.md
├── skills/
│   ├── create-api.md
│   ├── code-review.md
│   ├── write-test.md
│   ├── write-prd.md
│   ├── write-adr.md
│   ├── incident-analysis.md
│   └── release-service.md
├── workflows/
│   ├── create-feature.md
│   ├── fix-bug.md
│   ├── release.md
│   ├── incident.md
│   └── onboarding.md
├── docs/
│   ├── prd-template.md
│   ├── architecture-template.md
│   ├── adr-template.md
│   ├── api-spec-template.md
│   ├── task-template.md
│   └── agent-collaboration-rules.md
├── projects/
│   └── ai-company-task-manager/
│       ├── README.md
│       └── prd/
│           └── PRD-0001-foundation.md
├── tasks/
│   ├── README.md
│   └── TASK-0001-bootstrap-company-os.md
├── memory/
│   ├── README.md
│   ├── company-memory/
│   ├── project-memory/
│   ├── decision-memory/
│   │   ├── ADR-0001-git-markdown-ssot.md
│   │   └── ADR-0002-langgraph-orchestration.md
│   ├── task-memory/
│   └── lessons-learned-memory/
├── agents/
│   ├── ceo.yaml
│   ├── pm.yaml
│   ├── architect.yaml
│   ├── backend.yaml
│   ├── reviewer.yaml
│   └── qa.yaml
└── langgraph/
    ├── README.md
    ├── feature-graph.md
    ├── bugfix-graph.md
    └── release-graph.md
```

## Canonical Collaboration Pipeline

```text
PM → Architect → Backend → Reviewer → QA → Release(DevOps)
```

단계별 입출력은 [`docs/agent-collaboration-rules.md`](docs/agent-collaboration-rules.md)를 따른다.

## Agent Relationship

```text
                 CEO
              /   |   \
           PM  Architect  DevOps
            \   /    \      |
           Backend  Frontend|
               \    /       |
              Reviewer      |
                  \         |
                   QA ------+
                    \
                 Release
```

## LangGraph

| Graph | Doc |
|-------|-----|
| FeatureGraph | `langgraph/feature-graph.md` |
| BugFixGraph | `langgraph/bugfix-graph.md` |
| ReleaseGraph | `langgraph/release-graph.md` |

## Core Principles

1. Knowledge in Git Markdown
2. Clear Roles & R&R
3. Workflow-driven work
4. Decisions in ADR
5. Read docs — do not guess
6. Accumulate Memory
7. Collaborate like a real company

## Labs (LangChain / LangGraph / LangSmith)

시나리오: [`labs/LEARNING-SCENARIO.md`](labs/LEARNING-SCENARIO.md)  
실행 코드: [`runtime/README.md`](runtime/README.md)

```bash
cd runtime
cp .env.example .env   # OPENROUTER_API_KEY 설정
uv sync
uv run python -m labs.run_all
```

기본은 `MOCK_LLM=true`로 API 키 없이 Lab 0–10이 동작한다.  
**실모델은 OpenRouter 기준**: `.env`에 `OPENROUTER_API_KEY`를 넣고 `MOCK_LLM=false`로 전환.  
LangSmith는 `LANGCHAIN_TRACING_V2=true` + `LANGCHAIN_API_KEY`.

## Next Extensions

- Live LLM tool-calling agents (replace mock nodes)
- Operator API (FastAPI) + Task DB
- Frontend Operator Console
- CI gates binding Reviewer/QA approvals
- Vector retrieval over Memory
- Additional agents: frontend.yaml, devops.yaml, technical-writer.yaml
