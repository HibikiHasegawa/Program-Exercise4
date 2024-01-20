import numpy as np
import matplotlib.pyplot as plt

# 微分方程式 dy/dx
def func_f(y, x):
    return np.exp(-np.sin(x)) - y * np.cos(x)

# 4次のルンゲクッタ法
def runge_kutta_4th_order(a, b, N):
    h = (b - a) / N

    xpoints = np.arange(a, b, h)
    ypoints = []

    # 初期値 y(0) = 1
    y = 1.0

    # ルンゲクッタ法
    for x in xpoints:
        ypoints.append(y)
        k1 = h * func_f(y, x)
        k2 = h * func_f(y + 0.5 * k1, x + 0.5 * h)
        k3 = h * func_f(y + 0.5 * k2, x + 0.5 * h)
        k4 = h * func_f(y + k3, x + h)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6

    # 関数 y の図示
    plt.plot(xpoints, ypoints, label='Runge-Kutta 4th Order')
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.show()

    return xpoints, ypoints


# オイラー法
def euler(a, b, delta_x):
    x = a
    y = 1.0

    xpoints = [x]
    ypoints = [y]

    # オイラー法
    while x < b:
        y += func_f(y, x) * delta_x
        x += delta_x
        xpoints.append(x)
        ypoints.append(y)

    # 関数 y の図示
    plt.plot(xpoints, ypoints, label='Euler')
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.show()

    return xpoints, ypoints


# 2次のルンゲクッタ法
def runge_kutta_2nd_order(a, b, delta_x):
    x = a
    y = 1.0

    xpoints = [x]
    ypoints = [y]

    # 2次のルンゲクッタ法
    while x < b:
        k1 = delta_x * func_f(y, x)
        k2 = delta_x * func_f(y + 0.5 * k1, x + 0.5 * delta_x)
        y += k2
        x += delta_x
        xpoints.append(x)
        ypoints.append(y)

    # 関数 y の図示
    plt.plot(xpoints, ypoints, label='Runge-Kutta 2nd Order')
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.show()

    return xpoints, ypoints


# main
if __name__ == '__main__':
    a, b, N = 0.0, 100.0, 10000
    delta_x = 0.01

    x1, y1 = runge_kutta_4th_order(a, b, N)
    x2, y2 = euler(a, b, delta_x)
    x3, y3 = runge_kutta_2nd_order(a, b, delta_x)

    # 関数 y の図示
    plt.plot(x1, y1, label='Runge-Kutta 4th Order')
    plt.plot(x2, y2, label='Euler')
    plt.plot(x3, y3, label='Runge-Kutta 2nd Order')
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.show()
