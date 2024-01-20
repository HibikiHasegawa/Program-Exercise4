import numpy as np
import matplotlib.pyplot as plt

# 微分方程式: y'' - xy' + xy = 0
def func_f(y, dy_dx, x):
    return x * dy_dx - x * y

# ルンゲ・クッタ法
def runge_kutta(order):
    a, b = 0.0, 1.0
    N = 10000
    h = (b - a) / N

    xpoints = np.arange(a, b, h)
    ypoints = []
    dy_dx_points = []

    y, dy_dx = 1.0, 1.0

    for x in xpoints:
        ypoints.append(y)
        dy_dx_points.append(dy_dx)

        # ルンゲ・クッタ法のステップ
        k1_y = h * dy_dx
        k1_dy_dx = h * func_f(y, dy_dx, x)

        k2_y = h * (dy_dx + 0.5 * k1_dy_dx)
        k2_dy_dx = h * func_f(y + 0.5 * k1_y, dy_dx + 0.5 * k1_dy_dx, x + 0.5 * h)

        if order == 4:
            k3_y = h * (dy_dx + 0.5 * k2_dy_dx)
            k3_dy_dx = h * func_f(y + 0.5 * k2_y, dy_dx + 0.5 * k2_dy_dx, x + 0.5 * h)

            k4_y = h * (dy_dx + k3_dy_dx)
            k4_dy_dx = h * func_f(y + k3_y, dy_dx + k3_dy_dx, x + h)

            y += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
            dy_dx += (k1_dy_dx + 2 * k2_dy_dx + 2 * k3_dy_dx + k4_dy_dx) / 6
        elif order == 2:
            y += k2_y
            dy_dx += k2_dy_dx

    return xpoints, ypoints, dy_dx_points

# グラフのプロット
def plot_results(xpoints, ypoints, dy_dx_points, label):
    # y(x)のプロット
    plt.plot(xpoints, ypoints, label=label + ' (y)')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

    # y'(y)のプロット
    plt.plot(ypoints, dy_dx_points, label=label + " (dy/dx)")
    plt.xlabel("y")
    plt.ylabel("y'")
    plt.legend()
    plt.show()

# メイン実行部分
if __name__ == '__main__':
    x1, y1, dy_dx1 = runge_kutta(4)
    x2, y2, dy_dx2 = runge_kutta(2)

    # 両方の方法でy(x)をプロット
    plot_results(x1, y1, dy_dx1, '4th Order Runge-Kutta')
    plot_results(x2, y2, dy_dx2, '2nd Order Runge-Kutta')

