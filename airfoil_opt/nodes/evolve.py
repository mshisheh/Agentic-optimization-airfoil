"""Evolution node."""

from __future__ import annotations

from airfoil_opt.state import AirfoilState
from airfoil_opt.utils.geometry import mutate_geometry


def evolve_node(state: AirfoilState) -> AirfoilState:
    current = state.get("geometry_params", {})
    next_params = mutate_geometry(current)
    return {
        **state,
        "generation": int(state.get("generation", 0)) + 1,
        "geometry_params": next_params,
    }
