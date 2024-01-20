import numpy as np
from scipy.optimize import fsolve

# 未知数を定義
def equations(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 1
    eq2 = x**3 - y
    return [eq1, eq2]

# 初期推定値
initial_guess = [0.5, 0.5]

# 連立方程式を解く
solution = fsolve(equations, initial_guess)

# 解を表示
x_solution, y_solution = solution
print(f"x = {x_solution}")
print(f"y = {y_solution}")
