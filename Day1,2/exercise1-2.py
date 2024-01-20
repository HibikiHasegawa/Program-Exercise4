from scipy.optimize import root

# 解きたい非線形方程式の関数を定義
def equation(x):
    return x**3 - 3*x**2 + 9*x - 8

# 初期推定値を指定
initial_guess = 1.0

# root関数を使用して非線形方程式を解く
sol = root(equation, initial_guess)

if sol.success:
    print("解:", sol.x[0])
else:
    print("解が見つかりませんでした。")
