import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

class ODESolver:
    def __init__(self, func_str):
        self.x, self.y = symbols('x y')
        self.expr = sympify(func_str)
        self.f = lambdify((self.x, self.y), self.expr, 'math')
        self.history = {}

    def solve_euler(self, x0, y0, h, n):
        xs, ys = [x0], [y0]
        for _ in range(n):
            ys.append(ys[-1] + h * self.f(xs[-1], ys[-1]))
            xs.append(xs[-1] + h)
        self.history['Euler'] = (xs, ys)
        return xs, ys

    def solve_rk4(self, x0, y0, h, n):
        xs, ys = [x0], [y0]
        for _ in range(n):
            xi, yi = xs[-1], ys[-1]
            k1 = h * self.f(xi, yi)
            k2 = h * self.f(xi + h/2, yi + k1/2)
            k3 = h * self.f(xi + h/2, yi + k2/2)
            k4 = h * self.f(xi + h, yi + k3)
            ys.append(yi + (k1 + 2*k2 + 2*k3 + k4) / 6)
            xs.append(xi + h)
        self.history['RK4'] = (xs, ys)
        return xs, ys
    
    def plot(self):
        plt.figure(figsize=(8,5))
        for method, (xs, ys) in self.history.items():
            plt.plot(xs, ys, label=method, marker='o' if method=='Euler' else 's')
        plt.legend()
        plt.grid(True)
        plt.show()
