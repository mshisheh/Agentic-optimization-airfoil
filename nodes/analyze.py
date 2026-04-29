import os


def extract_forces(case_dir):
    file = f"{case_dir}/postProcessing/forces/0/forces.dat"

    with open(file) as f:
        lines = f.readlines()

    last = lines[-1].split()
    cl = float(last[2])
    cd = float(last[1])

    return cl, cd


def analyze_node(state):
    analyzed = []

    for d, r in zip(state["designs"], state["results"]):
        cl, cd = extract_forces(r["case"])

        score = cl / cd if cd > 0 else -999

        analyzed.append({
            **d,
            "Cl": cl,
            "Cd": cd,
            "score": score
        })

    return {**state, "results": analyzed}
