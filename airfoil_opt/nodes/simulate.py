"""Simulation node."""

from __future__ import annotations

from airfoil_opt.state import AirfoilState
from airfoil_opt.utils.openfoam import run_openfoam_case


def simulate_node(state: AirfoilState) -> AirfoilState:
    result = run_openfoam_case(state["case_dir"])
    return {**state, "simulation_result": result}
