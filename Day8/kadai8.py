import numpy as np
import matplotlib.pyplot as plt

# 積分対象の関数
def integrand(x):
    return np.exp(-x)

# 区分求積法
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

# モンテカルロ法
def monte_carlo_integration(func, a, b, n):
    x = np.random.uniform(a, b, n)
    y = func(x)
    return (b - a) * np.mean(y)

# シンプソンの公式
def simpsons_rule(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("分割数は偶数でなければなりません。")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

if __name__ == '__main__':
    a = 0  # 積分範囲の下限
    b = 10  # 積分範囲の上限
    exact_integral = 1.0  # 正確な積分値

    # 分割数や乱数の数を変化させながら計算と比較
    for n in [10, 100, 1000, 10000]:
        trapezoidal_result = trapezoidal_rule(integrand, a, b, n)
        monte_carlo_result = monte_carlo_integration(integrand, a, b, n)
        simpsons_result = simpsons_rule(integrand, a, b, n)

        print(f"分割数/乱数の数: {n}")
        print(f"区分求積法（台形法）: {trapezoidal_result:.10f}, 誤差: {abs(trapezoidal_result - exact_integral):.10f}")
        print(f"モンテカルロ法: {monte_carlo_result:.10f}, 誤差: {abs(monte_carlo_result - exact_integral):.10f}")
        print(f"シンプソンの公式: {simpsons_result:.10f}, 誤差: {abs(simpsons_result - exact_integral):.10f}")
        print("\n")
