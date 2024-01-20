import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np


def _set_initial_condition(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_space: float,
) -> None:
    """
    初期条件の設定

    境界以外のt=0のU値を設定する
    """
    for i in range(1, grid_counts_x):
        array_2d[i][0] = np.sin(np.pi * i * grid_space)


def _set_boundary_condition(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_counts_t: int,
) -> None:
    """境界条件の設定"""
    for j in range(grid_counts_t + 1):
        array_2d[0][j] = 0.0
        array_2d[grid_counts_x][j] = 0.0


def calculate_equation(*, M: int, N: int, H: float, K: float) -> list:
    """
    差分方程式を計算する

    本プログラムの肝となる関数
    """
    # U値のリスト
    U: list = [[0.0 for _ in range(N + 1)] for _ in range(M + 1)]

    # 初期条件設定
    _set_initial_condition(
        array_2d=U,
        grid_counts_x=M,
        grid_space=H,
    )
    # 境界条件設定
    _set_boundary_condition(
        array_2d=U,
        grid_counts_x=M,
        grid_counts_t=N,
    )

    # U[i][1]の計算
    for i in range(1, M):
        R = (K / H) ** 2 * (i * H + 1)
        S = 2 * (1.0 - R)
        Q = K**2 * i * H * np.exp(0)
        U[i][1] = (R * (U[i + 1][0] + U[i - 1][0]) + S * U[i][0] + Q) / 2.0

    # U[i][j + 1]の計算
    for j in range(1, N):
        for i in range(1, M):
            R = (K / H) ** 2 * (i * H + 1)
            S = 2 * (1.0 - R)
            Q = K**2 * i * H * np.exp(-j * K)
            U[i][j + 1] = (
                R * (U[i + 1][j] + U[i - 1][j]) + S * U[i][j] - U[i][j - 1] + Q
            )

    return U


def animate_time_evolution(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_counts_t: int,
    grid_space: float,
    time_delta: float,
) -> None:
    """
    点線プロットのアニメーションを作成
    array_1dのデータをプロットし、時間発展をアニメーションで表示する
    """
    # 2次元配列を転置
    array_2d = np.array(array_2d).T
    # x軸の値を生成
    x_values = np.arange(grid_counts_x + 1) * grid_space

    # アニメーションの作成
    path_gif = "./animation.gif"
    frames = []

    fig, ax = plt.subplots(figsize=(7, 5))
    plt.xlabel("X (m)")
    plt.ylabel("Temperature (deg.)")
    plt.grid(True)

    for j in range(grid_counts_t + 1):
        frame = plt.plot(
            x_values,
            array_2d[j],
            linestyle="--",
            marker="o",
            color="b",
        )

        time = j * time_delta
        text = ax.text(
            0.05,
            0.95,
            f"t = {time:.2f} (h)",
            transform=ax.transAxes,
            fontsize=14,
            verticalalignment="top",
        )
        frames.append(frame + [text])

    anim = ArtistAnimation(fig, frames, interval=100)
    anim.save(path_gif, writer="pillow")


def output_result_file(
    array_2d: list,
    grid_counts_x: int,
    grid_counts_t: int,
    grid_space: float,
    time_delta: float,
) -> None:
    """2次元配列をテキストファイルに書き出す"""
    with open("./calculated_result.txt", "w") as file:
        file.write(f"# This file shows calculated result as below.\n\n")
        file.write(f"# Calculation Parameters.\n")
        file.write(f"grid_counts_x: {grid_counts_x}\n")
        file.write(f"grid_counts_t: {grid_counts_t}\n")
        file.write(f"grid_space: {grid_space}\n")
        file.write(f"time_delta: {time_delta}\n\n")

        file.write(f"# Calculated Matrix U.\n")
        for row in array_2d:
            line = " ".join(map(str, row))
            file.write(line + "\n")


def validate_parameters(R: float) -> None:
    """パラメータの妥当性をチェックする"""
    if R > 1.0:
        raise ValueError("R must be less than 1.0.")


if __name__ == "__main__":
    """
    双曲形方程式の数値解法（陽解法）
    """
    grid_counts_x: int = 10  # 格子点番号mの値
    grid_counts_t: int = 40  # 格子点番号nの値
    grid_space: float = 0.1  # 刻み幅 (meter)
    time_delta: float = 0.05  # 刻み幅 (hour)

    validate_parameters(R=2 * (time_delta / grid_space))

    array_2d = calculate_equation(
        M=grid_counts_x,
        N=grid_counts_t,
        H=grid_space,
        K=time_delta,
    )
    animate_time_evolution(
        array_2d=array_2d,
        grid_counts_x=grid_counts_x,
        grid_counts_t=grid_counts_t,
        grid_space=grid_space,
        time_delta=time_delta,
    )
    output_result_file(
        array_2d=array_2d,
        grid_counts_x=grid_counts_x,
        grid_counts_t=grid_counts_t,
        grid_space=grid_space,
        time_delta=time_delta,
    )