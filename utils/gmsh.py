import os


def generate_geo(dat_file, geo_file):
    with open(geo_file, "w") as f:
        f.write(
            f"""
Merge \"{dat_file}\";

Spline(1) = {{1:100}};

// domain
Rectangle(2) = {{-5, -5, 0, 15, 10, 0}};

// mesh size
Mesh.CharacteristicLengthMin = 0.01;
Mesh.CharacteristicLengthMax = 0.5;
"""
        )


def run_gmsh(geo_file):
    os.system(f"gmsh {geo_file} -2 -format msh2")
