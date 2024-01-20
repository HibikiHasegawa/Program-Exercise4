import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def laplace_jacobi(phi, max_iter=10000, tolerance=1e-5):
    iterations=0
    for _ in range(max_iter):
        old_phi = phi.copy()
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                phi[i, j] = 0.25 * (old_phi[i + 1, j] + old_phi[i - 1, j] + old_phi[i, j + 1] + old_phi[i, j - 1])
        iterations+=1
        # 収束判定
        if np.max(np.abs(phi - old_phi)) < tolerance:
            break
    return phi, iterations
def laplace_gauss_seidel(phi, max_iter=10000, tolerance=1e-5):
    iterations=0
    for _ in range(max_iter):
        old_phi = phi.copy()
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                phi[i, j] = 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1])
        iterations+=1
        # 収束判定
        if np.max(np.abs(phi - old_phi)) < tolerance:
            break
    return phi, iterations
def laplace_sor(phi, omega, max_iter=10000, tolerance=1e-5):
    iterations=0
    for _ in range(max_iter):
        old_phi = phi.copy()
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                phi[i, j] = (1 - omega) * phi[i, j] + omega * 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1])
        iterations+=1
        # 収束判定
        if np.max(np.abs(phi - old_phi)) < tolerance:
            break
    return phi, iterations
# 領域の設定
Lx, Ly = 1.0, 1.0  # xおよびyの領域の長さ
Nx, Ny = 50, 50    # xおよびyの方向の離散化点数
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1)  # xおよびyの離散化ステップ
# 初期値の設定
phi = np.zeros((Nx, Ny))
# 境界条件の設定
phi[:, 0] = 0      # phi(x, 0) = 0
phi[:, -1] = np.linspace(0, 1, Nx)  # phi(x, 1) = x
phi[0, :] = 0      # phi(0, y) = 0
phi[-1, :] = np.linspace(0, 1, Ny)  # phi(1, y) = y
# ヤコビ法の実行
phi_jacobi, i_j = laplace_jacobi(phi.copy())
# ガウスザイデル法の実行
phi_gauss_seidel, i_g = laplace_gauss_seidel(phi.copy())
# SOR法の実行（omega=1.6としていますが、必要に応じて変更してください）
omega = 1.9
phi_sor, i_s = laplace_sor(phi.copy(), omega)
# 反復回数の表示
print("jacobi:", i_j,"/ gauss_seidel:", i_g, "/ sor:", i_s)
# 3次元プロット
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)
fig = plt.figure(figsize=(12, 4))
# ヤコビ法のプロット
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, phi_jacobi.T, cmap='viridis')
ax1.set_title('Jacobi Method')
# ガウスザイデル法のプロット
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, phi_gauss_seidel.T, cmap='viridis')
ax2.set_title('Gauss-Seidel Method')
# SOR法のプロット
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, phi_sor.T, cmap='viridis')
ax3.set_title(f'SOR Method (omega={omega})')
plt.tight_layout()
plt.show()