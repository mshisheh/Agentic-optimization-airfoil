import os
import shutil

BASE_CASE = "base_case"  # template you create once


def setup_case(case_dir, mesh_file):
    shutil.copytree(BASE_CASE, case_dir)

    os.system(f"gmshToFoam {mesh_file} -case {case_dir}")
    os.system(f"checkMesh -case {case_dir}")


def run_case(case_dir, nproc=2):
    os.system(f"cd {case_dir} && decomposePar")
    os.system(f"cd {case_dir} && mpirun -np {nproc} simpleFoam -parallel")
    os.system(f"cd {case_dir} && reconstructPar")
