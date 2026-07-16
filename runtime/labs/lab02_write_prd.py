from __future__ import annotations

from company_os.prd_agent import write_prd_with_skill
from company_os.repo import FEATURE_REQUEST, read_text


def main() -> None:
    print("=== Lab 2: Write PRD Skill ===")
    path = write_prd_with_skill(FEATURE_REQUEST)
    text = read_text(path)
    print("wrote:", path)
    assert "Acceptance Criteria" in text or "AC-1" in text
    assert "Non-Goals" in text
    assert "Goals" in text
    print("DoD: PRD-0002 created with Goals/Non-Goals/AC")


if __name__ == "__main__":
    main()
