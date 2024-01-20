from sympy import symbols, Eq, solve

# 未知数を定義
x, y, z, u, w = symbols('x y z u w')

# 連立方程式を設定
eq1 = Eq(2*x + 7*y - z + 5*u - 3*w, 6)
eq2 = Eq(x - 4*y + 2*z - u + 6*w, 1)
eq3 = Eq(3*x + y - 9*z - 2*u + w, -2)
eq4 = Eq(10*x - 2*y - 5*z + 8*u - 7*w, 4)
eq5 = Eq(-4*x + 3*y + 12*z - 4*u - 2*w, -10)

# 連立方程式を解く
solutions = solve((eq1, eq2, eq3, eq4, eq5), (x, y, z, u, w))

# 解を表示
print("解:")
print(f"x = {solutions[x]}")
print(f"y = {solutions[y]}")
print(f"z = {solutions[z]}")
print(f"u = {solutions[u]}")
print(f"w = {solutions[w]}")
