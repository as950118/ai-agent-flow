# Memory System

모든 Memory는 Git 내 Markdown으로 관리한다. Agent는 작업 전 관련 Memory를 읽고, 작업 후 갱신한다.

## Memory Types

| Memory | Path | Purpose | Write Owners |
|--------|------|---------|--------------|
| company-memory | `memory/company-memory/` | 회사 정책·원칙 요약, 운영 노트 | CEO, TW |
| project-memory | `memory/project-memory/` | 프로젝트 컨텍스트·제약·합의 | PM, Architect |
| decision-memory | `memory/decision-memory/` | ADR 인덱스 및 결정 요약 | Architect, CEO |
| task-memory | `memory/task-memory/` | Task 진행·블로커·산출물 링크 | Assignee Roles |
| lessons-learned-memory | `memory/lessons-learned-memory/` | 성공/실패 교훈 | DevOps, QA, Architect, PM |

## Rules

1. **Append-only preference**: 기존 항목을 조용히 덮어쓰지 말고, 상태 변경은 Changelog로 남긴다.
2. **Link, don't duplicate**: 원본 PRD/ADR/Task를 복제하지 말고 경로를 링크한다.
3. **No secrets**: 자격증명·토큰·개인식별민감정보 금지.
4. **Retrieval before action**: Graph node 시작 시 관련 memory를 State에 hydrate.
5. **Write-back on gates**: Approve/Sign-off/Incident close 시 필수 갱신.

## Index Files

각 폴더의 `README.md`가 엔트리포인트다.
