from langgraph.graph import StateGraph
from nodes.design import generate_designs
from nodes.simulate import simulate_node
from nodes.analyze import analyze_node
from nodes.evolve import evolve_node


def build_graph():
    builder = StateGraph(dict)

    builder.add_node("design", generate_designs)
    builder.add_node("simulate", simulate_node)
    builder.add_node("analyze", analyze_node)
    builder.add_node("evolve", evolve_node)

    builder.set_entry_point("design")

    builder.add_edge("design", "simulate")
    builder.add_edge("simulate", "analyze")
    builder.add_edge("analyze", "evolve")
    builder.add_edge("evolve", "design")

    return builder.compile()
