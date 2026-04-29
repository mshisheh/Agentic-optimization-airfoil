"""OpenFOAM helper stubs."""

from __future__ import annotations

from typing import Dict


def run_openfoam_case(case_dir: str) -> Dict[str, float]:
    """Return mocked aerodynamic coefficients for scaffold stage."""
    return {
        "CL": 0.8,
        "CD": 0.03,
        "CM": -0.05,
    }
