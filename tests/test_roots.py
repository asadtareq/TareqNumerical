import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from TareqNumerical import RootFinder

solver = RootFinder("x**3 - x - 2")
solver.solve_bisection(a=1, b=2)
solver.solve_newton(x0=1.5)
solver.solve_secant(x0=1.5, x1=2.0)
solver.show_comparison_table()
solver.plot_comparison()

