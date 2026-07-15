# Company OS Runtime

LangChain / LangGraph / LangSmith 실습 코드.  
시나리오 SSOT: [`../labs/LEARNING-SCENARIO.md`](../labs/LEARNING-SCENARIO.md)

**LLM 기본 Provider: [OpenRouter](https://openrouter.ai/)**

## Setup

```bash
cd runtime
cp .env.example .env
# OPENROUTER_API_KEY=sk-or-... 입력 후
# MOCK_LLM=false
uv sync
```

## Environment

| Variable | Purpose |
|----------|---------|
| `LLM_PROVIDER` | `openrouter`(기본) \| `openai` |
| `OPENROUTER_API_KEY` | OpenRouter API key |
| `OPENROUTER_MODEL` | 예: `openai/gpt-4o-mini`, `anthropic/claude-sonnet-4` |
| `OPENROUTER_BASE_URL` | 기본 `https://openrouter.ai/api/v1` |
| `MOCK_LLM` | `true`면 API 없이 결정적 mock |
| `LANGCHAIN_TRACING_V2` | `true`면 LangSmith 트레이스 |
| `LANGCHAIN_API_KEY` | LangSmith API key |
| `LANGCHAIN_PROJECT` | 기본 `ai-company-task-manager` |

## Live (OpenRouter) quick start

```bash
# runtime/.env
MOCK_LLM=false
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-or-v1-...
OPENROUTER_MODEL=openai/gpt-4o-mini

uv run python -m labs.lab00_hello
```

모델 목록: https://openrouter.ai/models

## Run labs

```bash
cd runtime
uv run python -m labs.lab00_hello
uv run python -m labs.run_all
```

## Layout

```text
runtime/
  company_os/     # shared library
  labs/           # Lab entrypoints
  .env.example
```
