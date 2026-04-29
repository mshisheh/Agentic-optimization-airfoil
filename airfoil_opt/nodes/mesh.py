"""Meshing node."""

from __future__ import annotations

from airfoil_opt.state import AirfoilState
from airfoil_opt.utils.gmsh import build_mesh


def mesh_node(state: AirfoilState) -> AirfoilState:
    mesh_path = build_mesh(state["cad_path"], state["case_dir"])
    return {**state, "mesh_path": mesh_path}
