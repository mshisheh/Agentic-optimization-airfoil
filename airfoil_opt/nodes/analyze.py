"""Analysis node."""

from __future__ import annotations

from airfoil_opt.state import AirfoilState


def analyze_node(state: AirfoilState) -> AirfoilState:
    result = state.get("simulation_result", {})
    cl = float(result.get("CL", 0.0))
    cd = float(result.get("CD", 1.0))
    fitness = cl / max(cd, 1e-9)

    return {
        **state,
        "analysis": {"lift_to_drag": fitness},
        "fitness": fitness,
    }
