from sympy import symbols, Eq, solve, N

x, y = symbols('x y')
eq1 = Eq(x**2 + y**2, 1)
eq2 = Eq(x**3, y)

# 初期推定値のリスト
initial_guesses = [(0.5, 0.5), (-0.5, -0.5), (0.5, -0.5), (-0.5, 0.5)]

# 解のリストを初期化
all_solutions = []

# 各初期推定値に対して解を求める
for guess in initial_guesses:
    solution = solve((eq1, eq2), (x, y))
    if solution:
        all_solutions.extend(solution)

# 解を表示
for solution in all_solutions:
    x_value = N(solution[x], 6)
    y_value = N(solution[y], 6)
    print(f"x = {x_value}")
    print(f"y = {y_value}")
