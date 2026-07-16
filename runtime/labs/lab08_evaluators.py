from __future__ import annotations

from company_os.eval_prd import run_local_experiment


def main() -> None:
    print("=== Lab 8: Evaluators ===")
    path = run_local_experiment()
    print("experiment:", path)
    print("DoD: dataset heuristic experiment written; lessons updated on fails")


if __name__ == "__main__":
    main()
