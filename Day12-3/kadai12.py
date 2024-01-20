import numpy as np
import matplotlib.pyplot as plt

# パラメータの設定
L = 2.0   # 空間の長さ
T = 1.0   # 時間の長さ
Nx = 101  # 空間方向のグリッド数
Nt = 1000 # 時間方向のグリッド数

dx = L / (Nx - 1)
dt = T / Nt

# 初期条件の設定
x = np.linspace(0, L, Nx)
u = np.zeros((Nt+1, Nx))

# 初期条件の代入
u[0, :] = 0.05 * x * (2 - x)
u[:, 0] = 0
u[:, -1] = 0

# 差分法による数値解法
for n in range(0, Nt):
    for i in range(1, Nx-1):
        u[n+1, i] = 2 * (1 - 9 * dt**2 / dx**2) * u[n, i] - u[n-1, i] + (9 * dt**2 / dx**2) * (u[n, i+1] - 2 * u[n, i] + u[n, i-1])

# 結果のプロット
plt.imshow(u, aspect='auto', extent=[0, L, 0, T], origin='lower', cmap='viridis')
plt.colorbar(label='u')
plt.title('Wave Equation Numerical Solution')
plt.xlabel('x')
plt.ylabel('t')
plt.show()
