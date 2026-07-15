from __future__ import annotations

from company_os.artifacts import build_prd
from company_os.config import mock_llm
from company_os.llm import get_chat_model
from company_os.repo import FEATURE_REQUEST, system_prompt_for
from company_os.tools import read_repo_file, write_repo_file


def write_prd_with_skill(feature_request: str | None = None) -> str:
    """Lab2: follow skills/write-prd.md using tools (template + memory + write)."""
    skill = read_repo_file.invoke({"relative_path": "skills/write-prd.md"})
    template = read_repo_file.invoke({"relative_path": "docs/prd-template.md"})
    memory = read_repo_file.invoke({"relative_path": "memory/project-memory/README.md"})

    if not mock_llm():
        model = get_chat_model()
        guidance = (
            system_prompt_for("pm")
            + "\nUse the write-prd skill. Produce a complete PRD markdown.\n"
            + skill[:4000]
            + "\nTEMPLATE:\n"
            + template[:4000]
            + "\nMEMORY:\n"
            + memory[:2000]
            + f"\nFEATURE:\n{feature_request or FEATURE_REQUEST}\n"
        )
        draft = str(getattr(model.invoke(guidance), "content", ""))
        if draft.strip().startswith("#"):
            path = "projects/ai-company-task-manager/prd/PRD-0002-task-status-audit.md"
            write_repo_file.invoke({"relative_path": path, "content": draft})
            return path

    return build_prd(feature_request)
