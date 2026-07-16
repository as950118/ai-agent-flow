# Glossary

| Term | Definition |
|------|------------|
| **Company OS** | Git Repository 내 Role, Skill, Workflow, Memory, Agent 설정의 집합. 회사 운영의 Single Source of Truth. |
| **Role** | Agent의 책임·권한·제한·handoff를 정의한 문서 (`roles/`). |
| **Skill** | 재사용 가능한 작업 절차 단위 (`skills/`). Role이 Skill을 호출한다. |
| **Workflow** | Trigger부터 Completion까지 Agent 협업 순서와 승인 규칙 (`workflows/`). |
| **Agent** | Role을 수행하는 실행 단위. YAML config + System Prompt로 구성 (`agents/`). |
| **Handoff** | 한 Agent가 산출물을 다음 Agent에게 전달하는 공식 전환. |
| **ADR** | Architecture Decision Record. 기술/구조 결정의 Why를 기록. |
| **PRD** | Product Requirements Document. 무엇을 왜 만드는지 정의. |
| **Task** | 추적 가능한 작업 단위. Template 기반 Markdown (`tasks/`). |
| **Memory** | 시간이 지나도 재사용되는 지식 저장소 (`memory/`). |
| **Company Memory** | Vision, Values, 정책 수준 지식. |
| **Project Memory** | 특정 프로젝트의 컨텍스트·제약·합의. |
| **Decision Memory** | ADR 인덱스 및 결정 요약. |
| **Task Memory** | Task 진행 중 상태·블로커·산출물 링크. |
| **Lessons Learned Memory** | 실패/성공에서 추출한 재사용 교훈. |
| **LangGraph** | Stateful Multi-Agent graph 오케스트레이션 프레임워크. |
| **FeatureGraph** | Feature 개발 end-to-end Graph. |
| **BugFixGraph** | Bug 수정 Graph. |
| **ReleaseGraph** | 배포·릴리즈 Graph. |
| **Approval Gate** | Workflow 진행을 막는 공식 승인 지점. |
| **Escalation** | 권한/정보가 부족할 때 상위 Role 또는 Human으로 이관. |
| **Operator** | 인간 운영자. Strategic 승인 및 SEV-1 대응. |
| **DoD** | Definition of Done. 완료 조건 체크리스트. |
| **NFR** | Non-Functional Requirement (성능, 보안, 가용성 등). |
| **SEV** | Incident Severity (SEV-1 Critical ~ SEV-4 Low). |
| **Spike** | 학습/검증용 단기 조사 Task. 구현 DoD와 분리. |
| **SSOТ** | Single Source of Truth. 이 Repo의 Markdown + Git. |
