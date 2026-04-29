"""State definitions for the airfoil optimization workflow."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, TypedDict


class AirfoilState(TypedDict, total=False):
    """Shared state passed across LangGraph nodes."""

    generation: int
    individual_id: str
    geometry_params: Dict[str, float]
    cad_path: str
    mesh_path: str
    case_dir: str
    simulation_result: Dict[str, Any]
    analysis: Dict[str, Any]
    fitness: float
    population: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    error: Optional[str]
