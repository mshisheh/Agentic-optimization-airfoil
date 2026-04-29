"""Meshing utilities (stub) for Gmsh integration."""

from __future__ import annotations

from pathlib import Path


def build_mesh(cad_path: str, output_dir: str) -> str:
    """Create a placeholder mesh artifact path."""
    out = Path(output_dir) / "mesh.msh"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(f"# Placeholder mesh generated from {cad_path}\n", encoding="utf-8")
    return str(out)
