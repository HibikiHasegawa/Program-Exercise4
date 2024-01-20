import numpy as np
import matplotlib.pyplot as plt

# 初期条件と物理パラメータ
L = 2.0  # 空間の長さ
T = 1.0  # 計算する時間の長さ
Nx = 101  # 空間方向のグリッド数
Nt = 1000  # 時間方向のグリッド数

dx = L / (Nx - 1)  # 空間のステップサイズ
dt = T / Nt  # 時間のステップサイズ
c = 3.0  # 波の速さ

# 初期条件の設定
x = np.linspace(0, L, Nx)
u = np.zeros((Nt+1, Nx))

u[0, :] = 0.05 * x**2 - x  # 初期条件 u(x,0)
u[:, 0] = 0  # 境界条件 u(0,t) = 0
u[:, -1] = 0  # 境界条件 u(L,t) = 0

# 波動方程式を差分近似で解く
for n in range(0, Nt):
    for i in range(1, Nx - 1):
        u[n + 1, i] = u[n, i] + c**2 * dt**2 / dx**2 * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])

# 結果のプロット
X, T = np.meshgrid(x, np.linspace(0, T, Nt+1))
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, T, u, cmap='viridis')
ax.set_xlabel('Space (x)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Amplitude (u)')
ax.set_title('Wave Equation Solution using Finite Difference Method')
plt.show()
