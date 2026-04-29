"""LangGraph assembly for the airfoil optimization workflow."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from airfoil_opt.nodes.analyze import analyze_node
from airfoil_opt.nodes.design import design_node
from airfoil_opt.nodes.evolve import evolve_node
from airfoil_opt.nodes.mesh import mesh_node
from airfoil_opt.nodes.simulate import simulate_node
from airfoil_opt.state import AirfoilState


def build_graph():
    graph = StateGraph(AirfoilState)

    graph.add_node("design", design_node)
    graph.add_node("mesh", mesh_node)
    graph.add_node("simulate", simulate_node)
    graph.add_node("analyze", analyze_node)
    graph.add_node("evolve", evolve_node)

    graph.add_edge(START, "design")
    graph.add_edge("design", "mesh")
    graph.add_edge("mesh", "simulate")
    graph.add_edge("simulate", "analyze")
    graph.add_edge("analyze", "evolve")
    graph.add_edge("evolve", END)

    return graph.compile()
