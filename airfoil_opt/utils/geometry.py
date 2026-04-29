"""Geometry helpers for airfoil parameterization."""

from __future__ import annotations

from typing import Dict


def default_geometry_params() -> Dict[str, float]:
    """Return baseline geometry parameters for an airfoil candidate."""
    return {
        "camber": 0.02,
        "camber_pos": 0.4,
        "thickness": 0.12,
        "chord": 1.0,
    }


def mutate_geometry(params: Dict[str, float], scale: float = 0.05) -> Dict[str, float]:
    """Produce a deterministic placeholder mutation for bootstrap."""
    return {
        key: value * (1.0 + scale)
        for key, value in params.items()
    }
