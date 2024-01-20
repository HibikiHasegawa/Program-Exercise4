import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t, y, m1, m2, m3):
    x1, y1, x1d, y1d, x2, y2, x2d, y2d, x3, y3, x3d, y3d = y
    r1 = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    r2 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    r3 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    x1dd = m2 * (x2 - x1) / r3**3 + m3 * (x3 - x1) / r2**3
    y1dd = m2 * (y2 - y1) / r3**3 + m3 * (y3 - y1) / r2**3
    x2dd = m1 * (x1 - x2) / r3**3 + m3 * (x3 - x2) / r1**3
    y2dd = m1 * (y1 - y2) / r3**3 + m3 * (y3 - y2) / r1**3
    x3dd = m1 * (x1 - x3) / r2**3 + m2 * (x2 - x3) / r1**3
    y3dd = m1 * (y1 - y3) / r2**3 + m2 * (y2 - y3) / r1**3
    return np.array([x1d, y1d, x1dd, y1dd, x2d, y2d, x2dd, y2dd, x3d, y3d, x3dd, y3dd])

# 初期条件
m1 = 3.0
m2 = 4.0
m3 = 5.0

# 新しい初期条件
x1_0, y1_0 = 1, 3
x2_0, y2_0 = -2, -1
x3_0, y3_0 = 1, -1

xd1_0, yd1_0 = 0.0, 0.0
xd2_0, yd2_0 = 0.0, 0.0
xd3_0, yd3_0 = 0.0, 0.0

# 時間の範囲に関する制約
t_min = 0
t_max = 65
dt = 0.01
t_span = (t_min, t_max)

# Solve
ini = np.array([x1_0, y1_0, xd1_0, yd1_0, x2_0, y2_0, xd2_0, yd2_0, x3_0, y3_0, xd3_0, yd3_0])
t_values = np.arange(t_min, t_max, dt)
solved_data = solve_ivp(f, t_span, ini, t_eval=t_values, args=(m1, m2, m3), rtol=1.0e-13, atol=1.0e-13)

# 軌道のプロット
plt.figure(figsize=(8, 8))
plt.plot(solved_data.y[0], solved_data.y[1], label=f'm1 = {m1}')
plt.plot(solved_data.y[4], solved_data.y[5], label=f'm2 = {m2}')
plt.plot(solved_data.y[8], solved_data.y[9], label=f'm3 = {m3}')
plt.scatter([x1_0, x2_0, x3_0], [y1_0, y2_0, y3_0], color='red')  # 初期位置を赤で表示
plt.title('Pitagora Three-Body Problem')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
