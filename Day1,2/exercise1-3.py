import numpy as np
from scipy.optimize import fsolve

# 解きたい非線形方程式の関数を定義
def equation(x):
    return x**3 - 3*x**2 + 9*x - 8

# 初期推定値を指定
initial_guess = 1.0

# fsolveを使用して非線形方程式を解く
solution = fsolve(equation, initial_guess)

print("解:", solution[0])
