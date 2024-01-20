import numpy as np
from scipy.optimize import fsolve
import time

# 非線形方程式の右辺を定義
def equations(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 1
    eq2 = x**3 - y
    return [eq1, eq2]

# ニュートン・ラフソン法の実装
def newton_raphson(equations, initial_guess, tol=1e-6, max_iter=100):
    x, y = initial_guess
    for i in range(max_iter):
        eq_values = equations([x, y])
        eq1, eq2 = eq_values[0], eq_values[1]
        jacobian = [
            [2*x, 2*y],
            [3*x**2, -1]
        ]
        jacobian_inv = np.linalg.inv(jacobian)
        dx, dy = np.dot(jacobian_inv, [-eq1, -eq2])
        x += dx
        y += dy
        if abs(dx) < tol and abs(dy) < tol:
            return x, y
    return None

# 初期推定値
initial_guess = [0.5, 0.5]

# ライブラリを使用せずに方程式を解く時間を計測
start_time = time.time()
solution_no_library = newton_raphson(equations, initial_guess)
end_time = time.time()
elapsed_time_no_library = end_time - start_time

if solution_no_library:
    x_solution, y_solution = solution_no_library
    print("ライブラリを使用せずに得られた解:")
    print(f"x = {x_solution}")
    print(f"y = {y_solution}")
    print(f"実行時間: {elapsed_time_no_library}秒")
else:
    print("解が見つかりませんでした.")

# ライブラリを使用して方程式を解く時間を計測
start_time = time.time()
solution_library = fsolve(equations, initial_guess)
end_time = time.time()
elapsed_time_library = end_time - start_time

print("\nライブラリを使用して得られた解:")
print(f"x = {solution_library[0]}")
print(f"y = {solution_library[1]}")
print(f"実行時間: {elapsed_time_library}秒")
