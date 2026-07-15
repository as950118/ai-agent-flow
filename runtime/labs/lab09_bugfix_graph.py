from __future__ import annotations

from company_os.bugfix_graph import run_bugfix
from company_os.repo import read_text


def main() -> None:
    print("=== Lab 9: BugFixGraph Mini ===")
    result = run_bugfix("감사 로그에 actor 누락")
    print("status:", result.get("status"))
    print("root_cause:", result.get("root_cause"))
    print("fix:", result.get("fix_notes_path"))
    assert result.get("status") == "done"
    assert result.get("qa_decision") == "pass"
    assert read_text(result["fix_notes_path"])
    print("DoD: BugFixGraph compile + done")


if __name__ == "__main__":
    main()
