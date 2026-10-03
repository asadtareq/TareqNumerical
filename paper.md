---
title: 'TareqNumerical: A concise Python package for comparative numerical analysis, ODE solving and Curve fitting'
tags:
  - Python
  - Numerical Analysis
  - Root Finding
  - ODE Solver
  - Curve Fitting
authors:
  - name: Md Asaduzzaman
    orcid: 0000-0001-5007-169X
    affiliation: 1
affiliations:
 - name: School of Mechanical & Power Engineering, Zhengzhou University, China
   index: 1
date: 3 October 2026
bibliography: paper.bib
---

# Summary

`TareqNumerical` is a concise Python library designed to solve fundamental numerical analysis problems and perform comparative efficiency benchmarking across multiple methods. The library integrates three core sub-modules: Root Finding, Ordinary Differential Equation (ODE) Solvers, and Curve Fitting/Interpolation. Its primary goal is to provide researchers, engineers, and students with an intuitive and minimal API to compute accurate solutions while simultaneously analyzing convergence behavior, computation time, and error metrics.

# Statement of Need

While comprehensive scientific computing libraries like `SciPy` or `NumPy` provide robust individual solvers, comparing the performance, convergence speed, and accuracy of different numerical techniques side by side (e.g., Bisection vs. Newton-Raphson vs. Secant Method, or Euler vs. 4th-order Runge-Kutta) often requires writing repetitive boilerplate code.

`TareqNumerical` bridges this gap by offering a streamlined framework for side-by-side benchmarking. With minimal code lines, users can evaluate algorithm performance and visualize execution efficiency. This makes the package particularly useful for educational instruction, rapid algorithm prototyping, and benchmarking computational performance in numerical analysis.

# Key Features & Functionality

The package consists of three main operational modules:

- **Root Finding Engine:** Implements Bisection, Newton-Raphson, and Secant methods, offering side-by-side execution time and convergence analysis.
- **ODE Solver:** Implements Euler and Runge-Kutta (RK4) solvers with integrated error metrics and step-size comparison.
- **Interpolation & Curve Fitting:** Provides Lagrange interpolation capabilities with built-in visualization tools for fitted data.

# References