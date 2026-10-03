import numpy as np
import matplotlib.pyplot as plt

class CurveAnalyzer:
    def __init__(self, x_data, y_data):
        self.x = np.array(x_data)
        self.y = np.array(y_data)
        
    def lagrange_interpolation(self, xp):
        n = len(self.x)
        yp = 0
        for i in range(n):
            p = 1
            for j in range(n):
                if i != j:
                    p *= (xp - self.x[j]) / (self.x[i] - self.x[j])
            yp += p * self.y[i]
        return yp

    def polynomial_fit(self, degree):
        coeff = np.polyfit(self.x, self.y, degree)
        return np.poly1d(coeff)

    def compare_and_plot(self, xp, degree=2):
        poly = self.polynomial_fit(degree)
        yp_lagrange = self.lagrange_interpolation(xp)
        yp_fit = poly(xp)
        
        # Plotting logic
        poly = self.polynomial_fit(degree)
        yp_lagrange = self.lagrange_interpolation(xp)
        yp_fit = poly(xp)

        # ২. এরর ক্যালকুলেশন
        y_lagrange_all = np.array([self.lagrange_interpolation(xi) for xi in self.x])
        error_lagrange = np.mean(np.abs(self.y - y_lagrange_all))

        y_fit_all = poly(self.x)
        error_fit = np.mean(np.abs(self.y - y_fit_all))

        # ৩. টার্মিনালে কম্পারিজন টেবিল প্রিন্ট করা
        print("\n============ RESULTS ============")
        print(f"Lagrange Prediction: {yp_lagrange:.6f}")
        print(f"Curve Fit Prediction: {yp_fit:.6f}")

        print("\n============ COMPARISON ============")
        print("Method\t\tPrediction\tError")
        print(f"Lagrange\t{yp_lagrange:.6f}\t{error_lagrange:.6f}")
        print(f"Curve Fit\t{yp_fit:.6f}\t{error_fit:.6f}")

        # ৪. প্লট তৈরি করা
        x_plot = np.linspace(min(self.x), max(self.x), 100)
        y_lagrange_plot = [self.lagrange_interpolation(xi) for xi in x_plot]
        y_fit_plot = poly(x_plot)

        plt.figure(figsize=(8, 5))
        plt.scatter(self.x, self.y, color='red', label="Data Points", zorder=5)
        plt.plot(x_plot, y_lagrange_plot, label="Lagrange", linewidth=2)
        plt.plot(x_plot, y_fit_plot, linestyle="--", label="Curve Fit", linewidth=2)
        plt.scatter([xp], [yp_lagrange], color='green', label="Predicted (Lagrange)", zorder=6)
        plt.scatter([xp], [yp_fit], color='orange', label="Predicted (Fit)", zorder=6)

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Interpolation vs Curve Fitting")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        return yp_lagrange, yp_fit
