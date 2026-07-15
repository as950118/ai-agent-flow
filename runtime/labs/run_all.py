from __future__ import annotations

from importlib import import_module


LABS = [
    "labs.lab00_hello",
    "labs.lab01_role_agent",
    "labs.lab02_write_prd",
    "labs.lab03_single_node",
    "labs.lab04_pm_architect",
    "labs.lab05_feature_graph",
    "labs.lab06_ceo_interrupt",
    "labs.lab07_tracing_playbook",
    "labs.lab08_evaluators",
    "labs.lab09_bugfix_graph",
    "labs.lab10_capstone",
]


def main() -> None:
    for name in LABS:
        print("\n" + "#" * 60)
        mod = import_module(name)
        mod.main()
    print("\nALL LABS COMPLETE")


if __name__ == "__main__":
    main()
