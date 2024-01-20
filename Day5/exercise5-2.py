from sympy import symbols, Eq, solve

# 未知数を定義
x, y, z = symbols('x y z')

# 連立方程式を設定
eq1 = Eq(2*x + 3*y - z, 1)
eq2 = Eq(x + y + 2*z, 0)
eq3 = Eq(3*x - y + z, 2)

# 連立方程式を解く
solutions = solve((eq1, eq2, eq3), (x, y, z))

# 解を表示
print("解:")
print(f"x = {solutions[x]}")
print(f"y = {solutions[y]}")
print(f"z = {solutions[z]}")
