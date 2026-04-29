"""Design/CAD node."""

from __future__ import annotations

from pathlib import Path

from airfoil_opt.state import AirfoilState
from airfoil_opt.utils.geometry import default_geometry_params


def design_node(state: AirfoilState) -> AirfoilState:
    params = state.get("geometry_params", default_geometry_params())
    case_dir = Path(state.get("case_dir", "airfoil_opt/cases/default"))
    case_dir.mkdir(parents=True, exist_ok=True)

    cad_path = case_dir / "airfoil.cad"
    cad_path.write_text(f"# placeholder CAD with params: {params}\n", encoding="utf-8")

    return {
        **state,
        "geometry_params": params,
        "case_dir": str(case_dir),
        "cad_path": str(cad_path),
    }
