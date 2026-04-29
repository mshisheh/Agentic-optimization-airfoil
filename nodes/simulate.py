import os
from utils.geometry import generate_naca4, save_dat
from utils.gmsh import generate_geo, run_gmsh
from utils.openfoam import setup_case, run_case


def run_single(design, case_id):
    case_dir = f"cases/case_{case_id}"
    os.makedirs(case_dir, exist_ok=True)

    coords = generate_naca4(design["m"], design["p"], design["t"])
    dat_file = f"{case_dir}/airfoil.dat"
    geo_file = f"{case_dir}/airfoil.geo"

    save_dat(coords, dat_file)
    generate_geo(dat_file, geo_file)
    run_gmsh(geo_file)

    mesh_file = geo_file.replace(".geo", ".msh")

    setup_case(case_dir, mesh_file)
    run_case(case_dir)

    return case_dir


def simulate_node(state):
    results = []
    for i, d in enumerate(state["designs"]):
        case_dir = run_single(d, i)
        results.append({"case": case_dir})

    return {**state, "results": results}
