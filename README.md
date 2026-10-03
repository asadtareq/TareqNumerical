# TareqNumerical

**TareqNumerical** is a dynamic Python library designed for mathematicians and engineers to solve numerical analysis problems efficiently. It supports dynamic equation parsing, allowing users to input mathematical functions as strings.

## Features
- **Dynamic Root Solver**: Solve non-linear equations using Bisection, Newton-Raphson, and Secant methods.
- **Detailed Comparison Tables**: Compare methods instantly with automatic metrics like Initial Guess/Interval, Iteration count, Execution time, Final Error, and Convergence Status.
- **Dynamic ODE Solver**: Solve Ordinary Differential Equations using Euler and Runge-Kutta (RK4) methods.
- **Interpolation & Curve Fitting**: Compare Lagrange Interpolation with Polynomial Curve Fitting.
- **Visual Comparison**: Built-in plotting to compare convergence and accuracy of different methods.

## Installation
You can install the library via pip:
```bash
pip install TareqNumerical
```

## Quick Start

### 1. Finding Roots & Method Comparison
```python
from TareqNumerical import RootFinder

# 1. Initialize with your dynamic non-linear equation
solver = RootFinder("x**3 - x - 2")

# 2. Run different root-finding methods
solver.solve_bisection(a=1, b=2)
solver.solve_newton(x0=1.5)
solver.solve_secant(x0=1.5, x1=2.0)

# 3. Print the comprehensive comparison table (with Initial Guess & Status)
solver.show_comparison_table()

# 4. Plot the error convergence graph
solver.plot_comparison()
```

### 2. Solving ODEs
```python
from TareqNumerical import ODESolver

ode = ODESolver("x + y")
xs, ys = ode.solve_rk4(x0=0, y0=1, h=0.1, n=10)
ode.plot()
```

### 3. Curve Fitting
```python
from TareqNumerical import CurveAnalyzer

x_data = [0, 1, 2, 3]
y_data = [1, 3, 2, 5]
analyzer = CurveAnalyzer(x_data, y_data)
lag_val, fit_val = analyzer.compare_and_plot(xp=1.5, degree=2)
```

## Requirements
- NumPy
- MatPlotLib
- SymPy

## Author
Md Asaduzzaman (Tareq)
