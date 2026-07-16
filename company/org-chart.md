# Organization Chart

## Structure

```
                    ┌─────────┐
                    │   CEO   │
                    └────┬────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
     ┌────▼────┐   ┌─────▼─────┐  ┌────▼────┐
     │   PM    │   │ Architect │  │ DevOps  │
     └────┬────┘   └─────┬─────┘  └────┬────┘
          │              │             │
    ┌─────┴─────┐        │             │
    │           │        │             │
┌───▼───┐  ┌────▼────┐   │        ┌────▼────┐
│Backend│  │Frontend │◄──┘        │   QA    │
└───┬───┘  └────┬────┘            └────┬────┘
    │           │                      │
    └─────┬─────┘                      │
          │                            │
     ┌────▼────┐                       │
     │Reviewer │◄──────────────────────┘
     └────┬────┘
          │
     ┌────▼──────────────┐
     │ Technical Writer  │
     └───────────────────┘
```

## Reporting & Collaboration Lines

| Role | Reports To | Collaborates With |
|------|------------|-------------------|
| CEO | Human Operator | All Roles |
| PM | CEO | Architect, Backend, Frontend, QA |
| Architect | CEO | PM, Backend, Frontend, DevOps |
| Backend | Architect (tech), PM (scope) | Frontend, Reviewer, QA |
| Frontend | Architect (tech), PM (scope) | Backend, Reviewer, QA |
| Reviewer | Architect | Backend, Frontend, QA |
| QA | PM | Backend, Frontend, DevOps, Reviewer |
| DevOps | CEO | Architect, Backend, QA |
| Technical Writer | PM | All Roles |

## Decision Authority

| Decision Type | Owner | Approver |
|---------------|-------|----------|
| Product Scope | PM | CEO (if strategic) |
| Architecture | Architect | CEO (if high-risk) |
| Implementation Detail | Backend / Frontend | Reviewer |
| Release Go/No-Go | QA + DevOps | CEO (prod major) |
| Incident Severity | DevOps | CEO (SEV-1) |

## Span of Control Principle

- CEO: 전략, 우선순위, Escalation 최종 결정
- PM: Feature 범위, 일정, Stakeholder 정렬
- Architect: 기술 경계, ADR, 비기능 요구사항
- IC Agents (Backend/Frontend/QA/DevOps): 실행 및 산출물
