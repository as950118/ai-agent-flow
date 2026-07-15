# Lessons Learned Memory

## Entries

### LL-0001 — Docs before runtime code

| Field | Value |
|-------|-------|
| Date | 2026-07-15 |
| Source | Founding bootstrap |
| Type | Success pattern |

**Lesson:** Multi-Agent 회사 OS는 Role/Workflow/Memory를 먼저 고정해야 Graph 구현 시 환각과 재작업이 줄어든다.

**Apply when:** 신규 프로젝트/신규 Graph 추가 시.

**Anti-pattern:** Prompt만으로 역할 정의 후 사후 문서화.

---

### LL-0002 — Gates are not optional

| Field | Value |
|-------|-------|
| Date | 2026-07-15 |
| Source | Values & Release policy |
| Type | Preventive |

**Lesson:** Reviewer/QA 게이트를 건너뛴 배포는 Incident 확률을 높인다. Emergency path는 CEO 승인 + 사후 문서화가 필수다.

**Apply when:** ReleaseGraph approval nodes.

## Template

```markdown
### LL-NNNN — Title
Date / Source / Type
Lesson:
Apply when:
Anti-pattern:
Related ADR/Incident:
```


### LL-LAB8 — PRD eval failures
Fail cases: ambiguous
Lesson: 모호한 요청은 AC를 채우기 전에 Open Questions를 강제한다.
