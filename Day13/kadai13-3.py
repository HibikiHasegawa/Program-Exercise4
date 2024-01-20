import numpy as np
import matplotlib.pyplot as plt

def heat_diffusion_explicit(dx, dt, xmax, tmax):
    D = 2.0  # 熱拡散係数

    beta = D * dt / dx**2  # 差分法の係数

    # 空間および時間の格子点数
    nx = int(xmax / dx) + 1
    nt = int(tmax / dt) + 1

    # 空間および時間の格子点
    x = np.linspace(0, xmax, nx)
    t = np.linspace(0, tmax, nt)

    # 初期条件
    u = np.ones((nx, nt))
    u[:, 0] = 1.0  # 初期条件

    # 境界条件
    u[0, :] = 0.0
    u[-1, :] = 0.0

    # 差分法による時間発展
    for n in range(0, nt - 1):
        for i in range(1, nx - 1):
            u[i, n + 1] = u[i, n] + beta * (u[i + 1, n] - 2.0 * u[i, n] + u[i - 1, n])

    return x, t, u

def main():
    dx = 0.1
    dt = 0.005
    xmax = 4.0
    tmax = 1.0

    x, t, u = heat_diffusion_explicit(dx, dt, xmax, tmax)

    # グラフの表示
    plt.figure(figsize=(8, 6))
    plt.pcolormesh(t, x, u, shading='auto', cmap='hot')
    plt.colorbar(label='Temperature')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title('Heat Diffusion')
    plt.show()

if __name__ == "__main__":
    main()
