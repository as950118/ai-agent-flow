from __future__ import annotations

from company_os.pm_agent import answer_next_role


def main() -> None:
    print("=== Lab 1: Role-Grounded Agent ===")
    q = "이 Feature의 다음 담당 Role은 누구인가? 근거 문서를 인용해."
    answer = answer_next_role(q)
    print(answer)
    assert "Architect" in answer
    assert "docs/agent-collaboration-rules.md" in answer
    assert "workflows/create-feature.md" in answer
    print("DoD: grounded citations OK")


if __name__ == "__main__":
    main()
