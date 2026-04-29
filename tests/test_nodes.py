from pathlib import Path

from airfoil_opt.nodes.analyze import analyze_node
from airfoil_opt.nodes.design import design_node
from airfoil_opt.nodes.evolve import evolve_node
from airfoil_opt.nodes.mesh import mesh_node
from airfoil_opt.nodes.simulate import simulate_node


def test_design_node_creates_placeholder_cad_file(tmp_path: Path):
    state = {"case_dir": str(tmp_path), "geometry_params": {"camber": 0.03}}

    updated = design_node(state)

    cad_path = Path(updated["cad_path"])
    assert cad_path.exists()
    assert "placeholder CAD" in cad_path.read_text(encoding="utf-8")


def test_mesh_node_creates_mesh_path_from_cad(tmp_path: Path):
    cad_path = tmp_path / "airfoil.cad"
    cad_path.write_text("cad", encoding="utf-8")

    updated = mesh_node({"cad_path": str(cad_path), "case_dir": str(tmp_path)})

    assert Path(updated["mesh_path"]).exists()


def test_simulate_node_adds_mock_simulation_result(tmp_path: Path):
    updated = simulate_node({"case_dir": str(tmp_path)})

    assert updated["simulation_result"]["CL"] == 0.8
    assert updated["simulation_result"]["CD"] == 0.03


def test_analyze_node_computes_lift_to_drag_ratio():
    updated = analyze_node({"simulation_result": {"CL": 1.2, "CD": 0.06}})

    assert updated["analysis"]["lift_to_drag"] == 20.0
    assert updated["fitness"] == 20.0


def test_evolve_node_increments_generation_and_mutates_geometry():
    updated = evolve_node({"generation": 2, "geometry_params": {"camber": 0.1}})

    assert updated["generation"] == 3
    assert updated["geometry_params"]["camber"] == 0.10500000000000001
