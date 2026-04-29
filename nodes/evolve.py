import random


def select_top(results, k=3):
    return sorted(results, key=lambda x: x["score"], reverse=True)[:k]


def mutate(d):
    return {
        "m": max(0, min(0.1, d["m"] + random.uniform(-0.01, 0.01))),
        "p": max(0.2, min(0.6, d["p"] + random.uniform(-0.05, 0.05))),
        "t": max(0.08, min(0.18, d["t"] + random.uniform(-0.01, 0.01))),
        "alpha": max(0, min(10, d["alpha"] + random.uniform(-1, 1))),
    }


def evolve_node(state):
    top = select_top(state["results"])

    new_designs = []
    for d in top:
        new_designs.append(mutate(d))
        new_designs.append(mutate(d))

    return {
        "designs": new_designs,
        "iteration": state["iteration"] + 1,
    }
