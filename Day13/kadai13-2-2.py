import numpy as np
import matplotlib.pyplot as plt

def main(mode):
    # 計算領域
    xmin, xmax = 0., 1.               # 1 m
    tmin, tmax = 0., 60. * 60. * 1.   # 1 hour
    n_max = int(1e3)   # 最大反復回数 (implicitのため)
    c_tol = 1e-6       # 収束許容値 (implicitのため)

    # 材料定数 (copper)
    rho = 8960.   # 密度 (kg / m3)
    lam = 398.    # 熱伝導率 (W / m / K)
    cap = 386.    # 容量
    D   = lam / (rho * cap)

    # 離散化
    dx = 1e-2
    dt = 1e-1
    dt_star = dx ** 2 / (2. * D)   # 拡散条件
    beta = D * dt / (dx ** 2.)    # 係数
    nx = 1 + int((xmax - xmin) / dx)
    nt = 1 + int((tmax - tmin) / dt)
    x = np.linspace(xmin, xmax, nx)

    # 未知ベクトル
    u_explicit = np.ones(shape=(nx))
    u_implicit = np.ones(shape=(nx))

    # 初期条件
    u_ic = 20.
    u_explicit *= u_ic
    u_implicit *= u_ic

    # 境界条件
    u_bc = 100.
    u_explicit[0]  = u_bc    # ディリクレ
    u_explicit[-1] = u_explicit[-2]   # ノイマン
    u_implicit[0]  = u_bc
    u_implicit[-1] = u_implicit[-2]

    # 計算設定

    if mode == 0:
        print(">>>>> explicit")
        if dt < dt_star:
            print(">>>>> dt: %.3e, dt_star: %.3e" % (dt, dt_star))
            print(">>>>> CFL条件満たされています")
        else:
            print(">>>>> dt: %.3e, dt_star: %.3e" % (dt, dt_star))
            print(">>>>> CFL条件が満たされていません。プログラムを終了します")
            exit()
    elif mode == 1:
        print(">>>>> implicit")
        print(">>>>> dt: %.3e, dt_star: %.3e" % (dt, dt_star))

    # FDM: 有限差分法
    for n in range(0, nt-1):
        # Explicit法
        if mode == 0:
            v_explicit = np.copy(u_explicit)
            u_explicit[1:-1] = v_explicit[1:-1] + beta * (v_explicit[2:] - 2. * v_explicit[1:-1] + v_explicit[:-2])
            u_explicit[0] = u_bc
            u_explicit[-1] = u_explicit[-2]

        # Implicit法
        elif mode == 1:
            v_implicit = np.copy(u_implicit)
            A = np.eye(nx)
            A[1:-1, 1:-1] += beta * dt / (dx ** 2)
            b = v_implicit[1:-1]
            b[0] += beta * dt / (dx ** 2) * u_bc
            b[-1] += beta * dt / (dx ** 2) * u_implicit[-2]
            u_implicit[1:-1] = np.linalg.solve(A, b)

        # 定期的にプロット
        if n % int(nt / 10) == 0:
            print("step: %d / %d" % (n, nt))
            plt.figure(figsize=(8, 4))
            plt.plot(x, u_explicit, label='Explicit')
            plt.plot(x, u_implicit, label='Implicit')
            plt.xlim(-.1, 1.1)
            plt.ylim(0, 120)
            plt.title("t: %.1f min (step: %d / %d)" % (n * dt / 60., n, nt))
            plt.xlabel("x")
            plt.ylabel("u")
            plt.grid(alpha=.3)
            plt.legend()
            plt.show()  # グラフを保存せずに表示
            plt.clf()
            plt.close()

if __name__ == "__main__":
    mode = 0  # explicit: 0, implicit: 1
    main(mode)
