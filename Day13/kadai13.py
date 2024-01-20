import numpy as np
import matplotlib.pyplot as plt

# 初期条件と空間・時間の設定
L = 4  # 空間の長さ
T = 1  # 時間の終了
Nx = 100  # 空間方向のグリッド数
Nt = 1000  # 時間方向のグリッド数
dx = L / (Nx - 1)
dt = T / Nt
alpha = 2  # 熱伝導率

# 初期条件の設定
x_values = np.linspace(0, L, Nx)
u_initial = np.where((0 < x_values) & (x_values < 4), 10, 0)

# 行列の作成
A_cn = np.diag(1 + alpha * dt / (2 * dx**2) * np.ones(Nx - 2), k=0) - np.diag(alpha * dt / (4 * dx**2) * np.ones(Nx - 3), k=-1) - np.diag(alpha * dt / (4 * dx**2) * np.ones(Nx - 3), k=1)
B_cn = np.diag(1 - alpha * dt / (2 * dx**2) * np.ones(Nx - 2), k=0) + np.diag(alpha * dt / (4 * dx**2) * np.ones(Nx - 3), k=-1) + np.diag(alpha * dt / (4 * dx**2) * np.ones(Nx - 3), k=1)

A_fd = np.diag(1 - alpha * dt / dx**2 * np.ones(Nx - 1), k=0) + np.diag(alpha * dt / dx**2 * np.ones(Nx - 2), k=1)
B_fd = np.diag(1 + alpha * dt / dx**2 * np.ones(Nx - 1), k=0) - np.diag(alpha * dt / dx**2 * np.ones(Nx - 2), k=1)

A_bd = np.diag(1 + alpha * dt / dx**2 * np.ones(Nx - 1), k=0) - np.diag(alpha * dt / dx**2 * np.ones(Nx - 2), k=-1)
B_bd = np.diag(1 - alpha * dt / dx**2 * np.ones(Nx - 1), k=0) + np.diag(alpha * dt / dx**2 * np.ones(Nx - 2), k=-1)

# 時間発展
u_values_cn = [u_initial[1:-1]]  # Crank-Nicolson法の初期条件を保存
u_values_fd = u_initial[1:-1]  # 前進差分法の初期条件を保存
u_values_bd = [u_initial[1:-1]]  # 後退差分法の初期条件を保存

for n in range(1, Nt + 1):
    # Crank-Nicolson法
    b_cn = B_cn.dot(u_values_cn[-1])
    u_new_cn = np.linalg.solve(A_cn, b_cn)
    u_values_cn.append(u_new_cn)

    # 前進差分法
    b_fd = B_fd.dot(u_values_fd)
    u_new_fd = np.linalg.solve(A_fd, b_fd)
    u_values_fd = u_new_fd

    # 後退差分法
    b_bd = B_bd.dot(u_values_bd[-1])
    u_new_bd = np.linalg.solve(A_bd, b_bd)
    u_values_bd.append(u_new_bd)

# 結果の表示
u_values_cn = np.concatenate([np.zeros((1, Nt + 1)), u_values_cn, np.zeros((1, Nt + 1))], axis=0).T
u_values_fd = np.concatenate([np.zeros((1, Nt + 1)), u_values_fd.reshape(-1, 1), np.zeros((1, Nt + 1))], axis=0).T
u_values_bd = np.concatenate([np.zeros((1, Nt + 1)), u_values_bd, np.zeros((1, Nt + 1))], axis=0).T

x_mesh, t_mesh = np.meshgrid(x_values, np.linspace(0, T, Nt + 1))

fig = plt.figure(figsize=(18, 6))

# Crank-Nicolson法の結果
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(x_mesh, t_mesh, u_values_cn, cmap='viridis')
ax1.set_title('Crank-Nicolson法')
ax1.set_xlabel('x')
ax1.set_ylabel('t')
ax1.set_zlabel('u(x, t)')

# 前進差分法の結果
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(x_mesh, t_mesh, u_values_fd, cmap='viridis')
ax2.set_title('前進差分法')
ax2.set_xlabel('x')
ax2.set_ylabel('t')
ax2.set_zlabel('u(x, t)')

# 後退差分法の結果
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(x_mesh, t_mesh, u_values_bd, cmap='viridis')
ax3.set_title('後退差分法')
ax3.set_xlabel('x')
ax3.set_ylabel('t')
ax3.set_zlabel('u(x, t)')

plt.show()
