import sympy as sp

# 未知数を定義
x, y = sp.symbols('x y')

# 方程式を定義
eq1 = sp.Eq(x**2 + y**2, 1)
eq2 = sp.Eq(x**3, y)

# 連立方程式を解く
solutions = sp.solve((eq1, eq2), (x, y))

# 解を表示
for solution in solutions:
    x_value, y_value = solution
    print(f"x = {x_value}")
    print(f"y = {y_value}")
