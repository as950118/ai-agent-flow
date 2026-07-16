# LangChain / LangGraph / LangSmith 실습 시나리오

Company OS(`roles/`, `workflows/`, `memory/`)를 **살아 있는 실습 교재**로 쓰고,  
도구는 아래 순서로 올린다.

```text
LangChain (단위 능력) → LangGraph (협업 오케스트레이션) → LangSmith (관측·평가)
```

---

## 0. 실습 목표 & 규칙

### 목표

1. LangChain으로 **단일 Role Agent**(도구·프롬프트·문서 RAG)를 만든다.
2. LangGraph로 **FeatureGraph**를 실행 가능한 상태로 만든다.
3. LangSmith로 **트레이스·게이트 실패·회귀 평가**를 본다.
4. 산출물은 항상 Git Markdown에 남긴다 (추측 금지 원칙).

### 실습용 제품 시나리오 (고정)

> **Feature Request**  
> “Operator가 Task를 생성하고 상태(`todo → in_progress → done`)를 변경할 수 있어야 한다.  
> 변경 시 `actor`, `from`, `to`, `timestamp`가 감사 로그로 남아 조회 가능해야 한다.”

| ID | Artifact |
|----|----------|
| Feature | `TASK Status + Audit Log` |
| Workflow | `create-feature` |
| Graph | `FeatureGraph` |
| Sample PRD seed | Lab 2에서 생성 |

### 공통 제약

- 모델/키는 `.env`만 사용 (Git 커밋 금지)
- Role System Prompt는 `roles/*.md` + `agents/*.yaml`을 소스 오브 트루스로 로드
- 단계 스킵 금지: PRD 없이 Design, Design 없이 Implement 불가
- 각 Lab 끝에 **Definition of Done** 체크

### 권장 환경

| 항목 | 권장 |
|------|------|
| Python | 3.11+ |
| Packaging | `uv` 또는 Poetry |
| Packages | `langchain`, `langgraph`, `langsmith`, provider SDK |
| Observability | LangSmith project: `ai-company-task-manager` |
| Runtime folder | `runtime/` (실습 코드) |

---

## Roadmap Overview

```text
Phase A  LangChain Foundations     Lab 0–2
Phase B  LangGraph Orchestration   Lab 3–6
Phase C  LangSmith Ops & Eval      Lab 7–9
Phase D  Capstone                  Lab 10
```

| Lab | Focus | Stack | Outcome |
|-----|-------|-------|---------|
| 0 | Env & Hello | LangChain | 트레이스 1건이 LangSmith에 보임 |
| 1 | Doc Loader + Role Prompt | LangChain | PM Agent가 `roles/pm.md`를 읽고 답함 |
| 2 | Tools: read/write markdown | LangChain | PRD 파일 생성 |
| 3 | Single-node Graph | LangGraph | State + 1 node 컴파일 |
| 4 | Linear FeatureGraph (PM→Arch) | LangGraph | 게이트 엣지 |
| 5 | Full FeatureGraph (mock impl) | LangGraph | Review/QA 루프 |
| 6 | Interrupt / Human gate | LangGraph | CEO 승인 interrupt |
| 7 | Tracing & datasets | LangSmith | Run 비교 |
| 8 | Evaluators | LangSmith | PRD completeness eval |
| 9 | Failure playbook | All | BugFixGraph mini |
| 10 | Capstone | All | E2E demo + ADR |

예상 소요: Lab당 1–3시간, Capstone 반나절.

---

## Phase A — LangChain Foundations

### Lab 0 — Bootstrap & First Trace

**목표:** 프로젝트 런타임 골격 + LangSmith 연결.

**할 일**
1. `runtime/` 생성, 의존성 설치, `.env.example` 작성
2. `ChatModel` hello prompt 1회 호출
3. `LANGCHAIN_TRACING_V2=true` 로 LangSmith에 run 확인

**DoD**
- [ ] LangSmith 프로젝트에 성공 run ≥ 1
- [ ] README에 환경 변수 목록 기록

**배우는 것:** LangChain runnable, LangSmith 기본 트레이스

---

### Lab 1 — Role-Grounded Agent (No Guessing)

**목표:** Agent가 Company OS 문서를 **읽고** 답하게 한다.

**시나리오**
- 입력: `"이 Feature의 다음 담당 Role은 누구인가? 근거 문서를 인용해."`
- Agent: PM (또는 Router stub)
- 반드시 `docs/agent-collaboration-rules.md`, `workflows/create-feature.md`를 로드

**할 일**
1. Markdown loader / 단순 file read tool
2. System prompt를 `agents/pm.yaml`의 `system_prompt`에서 로드
3. 답변에 **파일 경로 인용** 강제

**DoD**
- [ ] 근거 없는 답변 시 스스로 “문서 부족”을 말함
- [ ] LangSmith 트레이스에 tool call이 보임

**배우는 것:** Prompt template, tools, grounding

---

### Lab 2 — PRD Writer Skill (LangChain Tool Loop)

**목표:** `skills/write-prd.md` 절차로 PRD Markdown을 생성한다.

**시나리오 입력**
```text
Feature: Task status transitions + audit log
Priority: P1
Constraints: REST API, no secrets in git
```

**할 일**
1. Tools: `read_template(docs/prd-template.md)`, `read_memory(project-memory)`, `write_file(projects/.../prd/)`
2. PM Agent가 Open Questions가 있으면 질문하고, 없으면 PRD 작성
3. 산출물 경로를 State/로그에 기록

**DoD**
- [ ] `PRD-0002-task-status-audit.md` 생성
- [ ] Goals / Non-Goals / AC 섹션 존재
- [ ] Trace에서 tool 순서가 절차와 유사

**배우는 것:** AgentExecutor/tool-calling agent, Skill = procedure

---

## Phase B — LangGraph Orchestration

### Lab 3 — State & One Node

**목표:** `FeatureState` TypedDict + `write_prd` 노드 1개 Graph.

**할 일**
1. `langgraph/feature-graph.md`의 State를 `runtime/state.py`로 이식
2. Node: Lab2 PM Agent 호출 → `prd_path` 기록
3. `graph.invoke({feature_request: ...})`

**DoD**
- [ ] 종료 State에 `prd_path` 존재
- [ ] LangSmith에 graph run으로 표시 (가능 시)

**배우는 것:** StateGraph, node, compile, invoke

---

### Lab 4 — Linear Pipeline with Gate

**목표:** `PM → Architect` 직선 + 조건부 엣지.

```text
write_prd → (prd_ok?) → design
            (questions?) → clarify → write_prd
```

**할 일**
1. Architect node: `roles/architect.md` + `skills/write-adr.md`로 ARCH/ADR draft 생성
2. Gate: PRD에 AC가 3개 미만이면 `clarify`
3. 산출물: Architecture stub + ADR stub under `projects/...`

**DoD**
- [ ] Happy path / clarify path 둘 다 재현
- [ ] ADR에 Rejected Alternatives 최소 1개

**배우는 것:** conditional edges, cycle, artifact handoff

---

### Lab 5 — FeatureGraph (Mock Implementation Path)

**목표:** Backend → Reviewer → QA 루프까지.  
코드 생성은 **모의(mock)** 가능: “구현 노트 Markdown”으로 대체해도 됨.

```text
design → implement_backend → review ⇄ fix → qa ⇄ fix → finalize
```

**시나리오 규칙**
- Backend: API Spec outline + fake patch summary 작성
- Reviewer: `skills/code-review.md` 기준으로 Blocker/Major 분류 (LLM)
- QA: AC 체크리스트 Pass/Fail (LLM + 규칙 혼합)
- **첫 Review는 의도적으로 Changes Requested 1회** 유도 (학습용 seed)

**DoD**
- [ ] review 재진입 ≥ 1회가 Trace에 보임
- [ ] 최종 `status=done` + task-memory 요약 기록

**배우는 것:** multi-node graph, loops, role separation

---

### Lab 6 — Human-in-the-Loop (CEO Gate)

**목표:** High-risk 결정에서 Graph interrupt.

**시나리오**
- Architect가 Breaking Change 플래그를 켜면 `escalate` 노드로 이동
- `interrupt_before` / `Command(resume=...)`로 Human(당신) 승인

**DoD**
- [ ] resume 전후로 서로 다른 경로 실행
- [ ] decision-memory에 CEO Decision Note 1건

**배우는 것:** checkpointing, interrupt, human gate

---

## Phase C — LangSmith Ops & Eval

### Lab 7 — Tracing Playbook

**목표:** 실습 run을 분석 가능한 관측 자산으로 만든다.

**할 일**
1. Run name 규칙: `featuregraph:{lab}:{yyyyMMdd-HHmm}`
2. Tags: `role:pm`, `gate:review`, `outcome:pass|fail`
3. Metadata: `prd_path`, `run_id`, `model`
4. 동일 입력으로 Lab5를 2회 실행해 latency/token 비교

**DoD**
- [ ] Tag/metadata로 LangSmith에서 Lab5 runs 필터 가능
- [ ] 한 run의 tool/node waterfall 스크린샷 또는 노트 첨부 (`labs/notes/`)

**배우는 것:** tracing hygiene

---

### Lab 8 — Evaluators for Company OS Quality

**목표:** “문서 품질”을 자동 평가한다.

**Dataset (예시 5건)**
| Example | Input | Reference signal |
|---------|-------|------------------|
| 1 | 명확한 feature request | AC ≥ 3 |
| 2 | 모호한 request | open_questions ≥ 1 |
| 3 | 보안 관련 request | NFR security 언급 |
| 4 | scope creep 문장 포함 | Non-Goals 존재 |
| 5 | 기존 ADR 충돌 | decision-memory 인용 |

**Evaluators**
1. Heuristic: 섹션 헤더 존재 여부
2. LLM-as-judge: “추측 없이 근거를 인용했는가?”
3. Trajectory: 필수 tool(`read_template`) 호출 여부

**DoD**
- [ ] Dataset + Experiment 1회 기록
- [ ] Fail 케이스가 Lessons Learned에 1줄 요약

**배우는 것:** LangSmith datasets, evaluators, experiments

---

### Lab 9 — BugFixGraph Mini + Incident Trace

**목표:** 실패 경로를 두 번째 Graph로 연습한다.

**시나리오**
- QA Fail seed: “감사 로그에 actor 누락”
- `BugFixGraph`: triage → reproduce(mock) → fix → review → verify

**DoD**
- [ ] FeatureGraph와 BugFixGraph가 별도 graph로 compile
- [ ] LangSmith에서 graph 이름/태그로 구분
- [ ] `workflows/fix-bug.md` Completion Conditions 체크리스트 충족(문서상)

**배우는 것:** multi-graph ops, failure workflows

---

## Phase D — Capstone

### Lab 10 — Company Demo Day

**한 줄 목표:** Operator 입력 한 번으로 FeatureGraph가 돌고, LangSmith에서 全程이 보이며, Git에 산출물이 남는다.

**데모 스크립트 (10분)**
1. Feature request 입력
2. LangSmith에서 PM→Arch→Backend→Review→QA 노드 전환 라이브
3. Review 1회 reject → fix → approve
4. 최종 PRD/ADR/API Spec/Task Memory 경로 공개
5. Eval 점수 요약

**필수 산출물**
- [ ] `runtime/` 동작 코드
- [ ] `.env.example`
- [ ] Lab 노트 `labs/notes/capstone.md`
- [ ] ADR-0003: runtime 패키지 구조 결정
- [ ] README “How to run labs” 섹션

---

## 실습 진행 캘린더 (제안)

| Day | Labs | Focus |
|-----|------|-------|
| Day 1 | 0–2 | LangChain |
| Day 2 | 3–4 | Graph 기초 + 게이트 |
| Day 3 | 5–6 | Full pipeline + HITL |
| Day 4 | 7–8 | LangSmith |
| Day 5 | 9–10 | BugFix + Capstone |

---

## Cursor에서 실습할 때 운영 규칙

Cursor는 Graph runtime이 아니다. 실습 중에는 역할을 **세션 단위로 고정**한다.

| Lab | Cursor에게 줄 역할 |
|-----|-------------------|
| 0–2 | “Backend 구현자” (runtime 코드 작성) |
| 3–6 | “Architect + Backend” (Graph 설계 준수) |
| 7–8 | “QA/Observability” (트레이스·평가) |
| 9–10 | “DevOps + PM” (E2E·문서 마감) |

매 Lab 시작 시 프롬프트 예:

```text
Lab N을 진행한다. labs/LEARNING-SCENARIO.md의 DoD만 목표로 한다.
추측하지 말고 roles/, skills/, workflows/, langgraph/ 문서를 먼저 읽어라.
이번 세션 역할은 <ROLE>이다.
```

---

## 성공 지표 (전체)

| Metric | Target |
|--------|--------|
| Labs Done | 0–10 |
| FeatureGraph happy + reject path | 둘 다 재현 |
| LangSmith searchable runs | Tag 규칙 준수 |
| Doc artifacts committed | PRD/ADR/Spec/Memory |
| Gate skip incidents | 0 |

---

## 다음 액션 (실습 시작 시)

1. Lab 0용 `runtime/` 스caffolder 생성
2. `.env.example` + 의존성 선언
3. PRD-0002 시드 문구를 `projects/...`에 stub으로 준비

이 문서가 실습 SSOT다. Lab 진행 중 시나리오가 바뀌면 ADR + 이 파일 Changelog에 기록한다.

## Progress

| Lab | Status | Notes |
|-----|--------|-------|
| 0–10 | Done (MOCK_LLM) | `uv run python -m labs.run_all` 통과 |
| LangSmith cloud UI | Pending keys | `.env`에 `LANGCHAIN_API_KEY` 필요 |
| Live OpenAI agents | Pending keys | `MOCK_LLM=false` + `OPENAI_API_KEY` |

## Changelog

| Date | Change |
|------|--------|
| 2026-07-15 | 초안: Lab 0–10 시나리오 수립 |
| 2026-07-15 | runtime 구현 + Lab 0–10 MOCK 실행 완료 |
