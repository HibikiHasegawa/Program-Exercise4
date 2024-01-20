import numpy as np
import matplotlib.pyplot as plt

# 初期条件
L = 2.0  # 空間の長さ
T = 1.0  # 時間の終了
Nx = 100  # 空間の分割数
Nt = 200  # 時間の分割数
dx = L / Nx
dt = T / Nt

# 初期条件の設定
x_values = np.linspace(0, L, Nx + 1)
u = np.zeros((Nt + 1, Nx + 1))
u[0, :] = 0.05 * x_values * (2 - x_values)
u[:, 0] = 0
u[:, -1] = 0

# 差分法で偏微分方程式を解く
for n in range(0, Nt):
    for i in range(1, Nx):
        u[n + 1, i] = 2 * (1 - 2 * dt / dx**2) * u[n, i] - u[n - 1, i] + (dt / dx)**2 * 9 * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])

# 結果のプロット
plt.figure(figsize=(10, 6))
plt.imshow(u, extent=[0, L, 0, T], origin='lower', aspect='auto', cmap='viridis')
plt.colorbar(label='Amplitude')
plt.title('PDE Solution: $\\frac{\\partial^2 u}{\\partial t^2} = 9 \\frac{\\partial^2 u}{\\partial x^2}$ with $u(x, 0) = 0.05x(2 - x)$')
plt.xlabel('x')
plt.ylabel('t')
plt.show()
