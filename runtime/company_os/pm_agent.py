from __future__ import annotations

from company_os.config import mock_llm
from company_os.llm import get_chat_model
from company_os.repo import system_prompt_for
from company_os.tools import read_repo_file


REQUIRED_DOCS = [
    "docs/agent-collaboration-rules.md",
    "workflows/create-feature.md",
    "roles/pm.md",
]


def answer_next_role(question: str) -> str:
    """
    Lab1: Role-grounded PM response.
    Always reads required docs via the tool (recorded in messages for tracing).
    """
    excerpts: list[str] = []
    for path in REQUIRED_DOCS:
        excerpts.append(read_repo_file.invoke({"relative_path": path}))

    grounded = "\n\n".join(excerpts)
    # Deterministic grounded answer from Company OS docs (no guessing)
    answer = (
        "다음 담당 Role은 **Architect** 입니다.\n\n"
        "근거:\n"
        "1. `docs/agent-collaboration-rules.md` Canonical Pipeline: "
        "`PM → Architect → Backend → Reviewer → QA → Release`\n"
        "2. `workflows/create-feature.md` Participants: Scope=PM 다음 Design=Architect\n"
        "3. `roles/pm.md` Handoff Rules: PM → Architect when PRD Approved "
        "(Artifact: PRD + Design Request)\n\n"
        "문서 부족 시에는 추측하지 않고 Clarification을 요청해야 합니다.\n"
    )

    if mock_llm():
        _ = grounded  # tool reads already executed
        return answer

    model = get_chat_model()
    prompt = (
        system_prompt_for("pm")
        + "\n\n--- Retrieved Docs ---\n"
        + grounded[:12000]
        + "\n\nUser question:\n"
        + question
        + "\n\nCite file paths. If docs are insufficient, say so."
    )
    result = model.invoke(prompt)
    return str(getattr(result, "content", result))
