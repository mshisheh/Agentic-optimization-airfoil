# Agentic Optimization Airfoil

## Project Objective

This project aims to build an **AI agentic framework for airfoil optimization** that:

- **Maximizes lift performance** (high Cl)
- **Minimizes drag** (low Cd)
- Improves the **Cl/Cd tradeoff** under practical design constraints

The workflow combines design generation, meshing, CFD simulation, analysis, and decision-making in a closed optimization loop.

## High-Level Framework

![Agentic Airfoil Optimization Objective](./images/objective-framework.svg)

The framework is organized as a multi-agent pipeline:

1. **Design Agent** proposes candidate airfoil geometries.
2. **Meshing Agent** prepares CFD-ready meshes.
3. **Simulation Agent** runs OpenFOAM cases.
4. **Analysis Agent** computes aerodynamic metrics (Cl, Cd, Cl/Cd).
5. **Decision Agent** selects/refines candidates and drives the next iteration.

An orchestration layer coordinates the loop until stop criteria are met (performance threshold, convergence, or iteration budget), then returns the best designs and supporting reports.

## Expected Outputs

- Best-performing airfoil geometry candidates
- Comparative performance report (Cl, Cd, Cl/Cd)
- Convergence/optimization history
- Decision rationale for selected designs

