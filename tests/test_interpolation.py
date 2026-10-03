import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from TareqNumerical import CurveAnalyzer

x_data = [0, 1, 2, 3]
y_data = [1, 3, 2, 5]
analyzer = CurveAnalyzer(x_data, y_data)
lag_val, fit_val = analyzer.compare_and_plot(xp=1.5, degree=2)

