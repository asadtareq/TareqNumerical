import time
import matplotlib.pyplot as plt
from sympy import symbols, sympify, diff, lambdify

class RootFinder:
    def __init__(self, func_str):
        self.x = symbols('x')
        self.expr = sympify(func_str)
        self.f = lambdify(self.x, self.expr, 'math')
        self.df = lambdify(self.x, diff(self.expr, self.x), 'math')
        self.results = {}

    def solve_bisection(self, a, b, tol=1e-5, max_iter=100):
        errors = []
        start = time.time()
        initial_guess = f"[{a}, {b}]"
        
        if self.f(a) * self.f(b) >= 0:
            self.results['Bisection'] = {'root': None, 'iter': 0, 'time': time.time()-start, 'errors': [], 'guess': initial_guess, 'status': 'Failed (Sign)'}
            return None
        
        status = 'Max Iter Reached'
        for i in range(max_iter):
            c = (a + b) / 2
            err = abs(self.f(c))
            errors.append(err)
            if err < tol:
                status = 'Converged'
                break
            if self.f(a) * self.f(c) < 0: b = c
            else: a = c
        
        self.results['Bisection'] = {'root': c, 'iter': i+1, 'time': time.time()-start, 'errors': errors, 'guess': initial_guess, 'status': status}
        return c

    def solve_newton(self, x0, tol=1e-5, max_iter=100):
        errors = []
        start = time.time()
        xn = x0
        initial_guess = f"x0={x0}"
        
        status = 'Max Iter Reached'
        for i in range(max_iter):
            fxn = self.f(xn)
            dfxn = self.df(xn)
            if dfxn == 0:
                status = 'Failed (Div by 0)'
                break
            x_next = xn - fxn / dfxn
            err = abs(x_next - xn)
            errors.append(abs(self.f(x_next)))
            if err < tol:
                status = 'Converged'
                break
            xn = x_next
            
        self.results['Newton'] = {'root': xn, 'iter': i+1, 'time': time.time()-start, 'errors': errors, 'guess': initial_guess, 'status': status}
        return xn

    def solve_secant(self, x0, x1, tol=1e-5, max_iter=100):
        errors = []
        start = time.time()
        initial_guess = f"x0={x0}, x1={x1}"
        
        status = 'Max Iter Reached'
        for i in range(max_iter):
            fx1 = self.f(x1)
            fx0 = self.f(x0)
            if fx1 - fx0 == 0:
                status = 'Failed (Div by 0)'
                break
            
            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            err = abs(x2 - x1)
            errors.append(abs(self.f(x2)))
            
            if err < tol:
                status = 'Converged'
                break
            x0 = x1
            x1 = x2
            
        self.results['Secant'] = {'root': x2, 'iter': i+1, 'time': time.time()-start, 'errors': errors, 'guess': initial_guess, 'status': status}
        return x2

    def show_comparison_table(self):
        """Initial Guess এবং Status সহ একটি সুন্দর প্রফেশনাল টেবিল প্রিন্ট করবে"""
        print("\n" + "="*90)
        print(f"{'Method':<12}{'Initial Guess':<18}{'Root':<14}{'Iterations':<12}{'Time (s)':<12}{'Status':<12}{'Final Error'}")
        print("="*90)
        
        for method, data in self.results.items():
            root_val = data['root']
            initial_guess = data['guess']
            iterations = data['iter']
            exec_time = data['time']
            status = data['status']
            final_err = data['errors'][-1] if data['errors'] else 0.0
            
            if root_val is not None:
                print(f"{method:<12}{initial_guess:<18}{root_val:<14.6f}{iterations:<12}{exec_time:<12.6f}{status:<12}{final_err:.6e}")
            else:
                print(f"{method:<12}{initial_guess:<18}{'N/A':<14}{iterations:<12}{exec_time:<12.6f}{status:<12}{'N/A'}")
        print("="*90)

    def plot_comparison(self):
        plt.figure(figsize=(10, 6))
        for method, data in self.results.items():
            if data['errors']:
                plt.plot(range(1, len(data['errors'])+1), data['errors'], label=method, marker='o')
        plt.yscale('log')
        plt.xlabel('Iterations')
        plt.ylabel('Error (log scale)')
        plt.title('Method Convergence Comparison')
        plt.legend()
        plt.grid(True, which="both", ls="--")
        plt.show()
