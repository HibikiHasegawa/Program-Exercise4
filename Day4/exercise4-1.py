from scipy.optimize import fsolve
import numpy as np

# 方程式を定義する関数
def equation(vars):
    x, y = vars[0], vars[1]
    return [x**3 + y**3 - 9*x*y + 27, 0]

# 初期推定値
initial_guess = [1.0, 1.0]

# 方程式を解く
result = fsolve(equation, initial_guess)

# 解を整数に丸める
rounded_x = round(result[0])
rounded_y = round(result[1])

# 結果を表示
print(f"x ≈ {rounded_x}")
print(f"y ≈ {rounded_y}")
