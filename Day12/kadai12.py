import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


def _set_initial_condition(array_2d, grid_counts_x, grid_space):
    for i in range(1, grid_counts_x):
        array_2d[i][0] = np.sin(np.pi * i * grid_space)


def _set_boundary_condition(array_2d, grid_counts_x, grid_counts_t):
    for j in range(grid_counts_t + 1):
        array_2d[0][j] = 0.0
        array_2d[grid_counts_x][j] = 0.0


def calculate_equation(M, N, H, K):
    U = [[0.0 for _ in range(N + 1)] for _ in range(M + 1)]

    _set_initial_condition(U, M, H)
    _set_boundary_condition(U, M, N)

    for i in range(1, M):
        R = (K / H) ** 2 * (i * H + 1)
        S = 2 * (1.0 - R)
        Q = K**2 * i * H * np.exp(0)
        U[i][1] = (R * (U[i + 1][0] + U[i - 1][0]) + S * U[i][0] + Q) / 2.0

    for j in range(1, N):
        for i in range(1, M):
            R = (K / H) ** 2 * (i * H + 1)
            S = 2 * (1.0 - R)
            Q = K**2 * i * H * np.exp(-j * K)
            U[i][j + 1] = (
                R * (U[i + 1][j] + U[i - 1][j]) + S * U[i][j] - U[i][j - 1] + Q
            )

    return U


def animate_time_evolution(array_2d, grid_counts_x, grid_counts_t, grid_space, time_delta):
    array_2d = np.array(array_2d).T
    x_values = np.arange(grid_counts_x + 1) * grid_space

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


def output_result_file(array_2d, grid_counts_x, grid_counts_t, grid_space, time_delta):
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


def validate_parameters(R):
    if R > 1.0:
        raise ValueError("R must be less than 1.0.")


if __name__ == "__main__":
    grid_counts_x = 100
    grid_counts_t = 400
    grid_space = 0.01
    time_delta = 0.0005

    validate_parameters(R=2 * (time_delta / grid_space))

    array_2d = calculate_equation(M=grid_counts_x, N=grid_counts_t, H=grid_space, K=time_delta)
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
