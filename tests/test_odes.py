import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from TareqNumerical import ODESolver

ode_solver = ODESolver("x+y")
ode_solver.solve_euler(1,2,0.1,10)
ode_solver.solve_rk4(1,2,0.1,10)
ode_solver.plot()
