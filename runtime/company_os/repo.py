from __future__ import annotations

from pathlib import Path

import yaml

from company_os.config import repo_root


def read_text(rel_path: str) -> str:
    path = repo_root() / rel_path
    if not path.exists():
        raise FileNotFoundError(f"Missing document: {rel_path}")
    return path.read_text(encoding="utf-8")


def write_text(rel_path: str, content: str) -> str:
    path = repo_root() / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return str(path.relative_to(repo_root()))


def load_agent_yaml(name: str) -> dict:
    path = repo_root() / "agents" / f"{name}.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Invalid agent yaml: {name}")
    return data


def system_prompt_for(role: str) -> str:
    data = load_agent_yaml(role)
    prompt = data.get("system_prompt", "").strip()
    role_doc = read_text(f"roles/{role}.md")
    return (
        f"{prompt}\n\n"
        f"--- Role Document (roles/{role}.md) ---\n{role_doc}\n"
        "Rules:\n"
        "- Cite file paths when making claims.\n"
        "- If information is missing, say so. Do not guess.\n"
    )


FEATURE_REQUEST = (
    "Operator가 Task를 생성하고 상태(todo → in_progress → done)를 변경할 수 있어야 한다. "
    "변경 시 actor, from, to, timestamp가 감사 로그로 남아 조회 가능해야 한다."
)
