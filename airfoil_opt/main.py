"""Main entrypoint for running a single airfoil optimization pass."""

from __future__ import annotations

from pprint import pprint

from airfoil_opt.graph import build_graph


def main() -> None:
    app = build_graph()
    initial_state = {
        "generation": 0,
        "individual_id": "seed-0",
        "case_dir": "airfoil_opt/cases/seed-0",
    }
    final_state = app.invoke(initial_state)
    pprint(final_state)


if __name__ == "__main__":
    main()
