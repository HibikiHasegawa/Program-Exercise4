import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np

def _set_initial_condition(
    *,
    array_2d: list,
    grid_counts_x: int,
) -> None:
    """初期条件の設定"""
    for i in range(1, grid_counts_x):
        array_2d[i][0] = 1.0  # 初期条件を1に変更
    return array_2d

def _set_boundary_condition(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_counts_t: int,
) -> None:
    """境界条件の設定"""
    # x=0上の境界条件
    for j in range(grid_counts_t + 1):
        array_2d[0][j] = 0.0

    # x=M上の境界条件
    for j in range(grid_counts_t + 1):
        array_2d[grid_counts_x][j] = 0.0  # 境界条件を0に変更

def calculate_equation(*, M: int, N: int, R: float) -> list:
    """差分方程式を計算する"""
    U: list = [[0.0 for _ in range(N + 1)] for _ in range(M + 1)]
    _set_initial_condition(array_2d=U, grid_counts_x=M)
    _set_boundary_condition(array_2d=U, grid_counts_x=M, grid_counts_t=N)

    for j in range(N):
        for i in range(1, M):
            U[i][j + 1] = (1.0 - 2 * R) * U[i][j] + R * (U[i + 1][j] + U[i - 1][j])
    return U

def animate_time_evolution(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_counts_t: int,
    grid_space: float,
    time_delta: float,
) -> None:
    array_2d = np.array(array_2d).T
    x_values = np.arange(grid_counts_x + 1) * grid_space

    path_gif = "./animation.gif"
    frames = []

    fig, ax = plt.subplots(figsize=(7, 5))
    plt.xlabel("X (m)")
    plt.ylabel("Temperature")
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
) -> None:
    with open("./calculated_result.txt", "w") as file:
        file.write(f"# This file shows calculated result as below.\n\n")
        file.write(f"# Calculation Parameters.\n")
        file.write(f"grid_counts_x: {grid_counts_x}\n")
        file.write(f"grid_counts_t: {grid_counts_t}\n")
        file.write(f"grid_space: {grid_space}\n")

        file.write(f"# Calculated Matrix U.\n")
        for row in array_2d:
            line = " ".join(map(str, row))
            file.write(line + "\n")

def validate_parameters(R: float) -> None:
    if R > 0.5:
        raise ValueError("R must be less than 0.5.")

if __name__ == "__main__":
    grid_counts_x: int = 40
    grid_counts_t: int = 150
    grid_space: float = 0.1
    time_delta: float = 0.07
    CHI: float = 2.0
    r: float = CHI * time_delta / grid_space**2

    #validate_parameters(R=r)

    array_2d = calculate_equation(M=grid_counts_x, N=grid_counts_t, R=r)
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
    )
