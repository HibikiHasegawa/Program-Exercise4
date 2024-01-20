import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np


def set_initial_condition(array_2d, grid_counts_x):
    """
    初期条件の設定
    境界以外のU値を全て0.0とおく
    """
    for i in range(1, grid_counts_x):
        array_2d[i][0] = 1.0


def set_boundary_condition(array_2d, grid_counts_x, grid_counts_t):
    """境界条件の設定"""
    for j in range(grid_counts_t + 1):
        array_2d[0][j] = 0.0
        array_2d[grid_counts_x][j] = 0.0


def calculate_crank_nicolson(M, N, R):
    """
    Crank-Nicolson法を使用して差分方程式を計算する
    """
    U = np.zeros((M + 1, N + 1))
    set_initial_condition(U, M)
    set_boundary_condition(U, M, N)

    # Crank-Nicolson法に基づく差分方程式の計算
    for j in range(N):
        for i in range(1, M):
            alpha = R / 2.0
            U[i][j + 1] = (1.0 - R) * U[i][j] + alpha * (U[i + 1][j] - 2 * U[i][j] + U[i - 1][j]) + alpha * (U[i + 1][j + 1] - 2 * U[i][j + 1] + U[i - 1][j + 1])

    return U


def animate_time_evolution(array_2d, grid_counts_x, grid_counts_t, grid_space, time_delta):
    """
    点線プロットのアニメーションを作成
    array_1dのデータをプロットし、時間発展をアニメーションで表示する
    """
    array_2d = np.array(array_2d).T
    x_values = np.arange(grid_counts_x + 1) * grid_space

    path_gif = "./animation.gif"
    frames = []

    fig, ax = plt.subplots(figsize=(7, 5))
    plt.xlabel("X (m)")
    plt.ylabel("Temperature (deg.)")
    plt.grid(True)

    for j in range(grid_counts_t + 1):
        frame = plt.plot(x_values, array_2d[j], linestyle="--", marker="o", color="b")

        time = j * time_delta
        text = ax.text(0.05, 0.95, f"t = {time:.2f} (h)", transform=ax.transAxes, fontsize=14, verticalalignment="top")
        frames.append(frame + [text])

    anim = ArtistAnimation(fig, frames, interval=100)
    anim.save(path_gif, writer="pillow")


def output_result_file(array_2d, grid_counts_x, grid_counts_t, grid_space):
    """2次元配列をテキストファイルに書き出す"""
    with open("./calculated_result.txt", "w") as file:
        file.write("# This file shows calculated result as below.\n\n")
        file.write("# Calculation Parameters.\n")
        file.write(f"grid_counts_x: {grid_counts_x}\n")
        file.write(f"grid_counts_t: {grid_counts_t}\n")
        file.write(f"grid_space: {grid_space}\n")

        file.write("# Calculated Matrix U.\n")
        for row in array_2d:
            line = " ".join(map(str, row))
            file.write(line + "\n")


def validate_parameters(R):
    """パラメータの妥当性をチェックする"""
    if R > 0.5:
        raise ValueError("R must be less than 0.5.")


if __name__ == "__main__":
    grid_counts_x = 20  # 格子点番号mの値
    grid_counts_t = 150  # 格子点番号nの値
    grid_space = 0.2  # 刻み幅 (meter)
    time_delta = 0.01  # 刻み幅 (hour)
    CHI = 2.0  # 温度伝導率 (m^2/h)
    r = CHI * time_delta / grid_space ** 2

    validate_parameters(R=r)

    array_2d = calculate_crank_nicolson(M=grid_counts_x, N=grid_counts_t, R=r)
    animate_time_evolution(array_2d=array_2d, grid_counts_x=grid_counts_x, grid_counts_t=grid_counts_t, grid_space=grid_space, time_delta=time_delta)
    output_result_file(array_2d=array_2d, grid_counts_x=grid_counts_x, grid_counts_t=grid_counts_t, grid_space=grid_space)