import matplotlib.pyplot as plt
import numpy as np

def _set_initial_condition(array_2d, grid_counts_x, grid_counts_y, grid_space):
    for j in range(1, grid_counts_y):
        for i in range(1, grid_counts_x):
            x = i * grid_space
            array_2d[i][j] = 0.05 * x**2 - x

def _set_boundary_condition(array_2d, grid_counts_x, grid_counts_y, grid_space):
    for i in range(grid_counts_x + 1):
        array_2d[i][0] = 0.0

    for i in range(grid_counts_x + 1):
        array_2d[i][grid_counts_y] = 0.0

def _is_converged(U, UF, M, N):
    ERROR_CONSTANT = 0.0001
    sum = 0.0
    sum0 = 0.0

    for j in range(1, N):
        for i in range(1, M):
            sum0 += abs(U[i][j])
            sum += abs(U[i][j] - UF[i][j])

    sum = sum / sum0
    return sum <= ERROR_CONSTANT

def calculate_equation(M, N, H, MK):
    U = [[0.0 for _ in range(M + 1)] for _ in range(N + 1)]
    UF = [[0.0 for _ in range(M + 1)] for _ in range(N + 1)]

    _set_initial_condition(U, M, N, H)
    _set_boundary_condition(U, M, N, H)

    calc_count = 0
    for _ in range(MK):
        for j in range(1, N):
            for i in range(1, M):
                UF[i][j] = U[i][j]
                U[i][j] = U[i + 1][j] + U[i - 1][j] - 9 * (H**2) * U[i][j - 1]

        calc_count += 1

        # 収束判定
        if _is_converged(U=U, UF=UF, M=M, N=N):
            print("収束しました")
            break

    return U, calc_count

def color_plot(array_2d, grid_counts, grid_space):
    min_x_y = 0.0 - grid_space / 2
    max_x_y = grid_space * grid_counts + grid_space / 2
    extent=(min_x_y, max_x_y, min_x_y, max_x_y)
    
    array_2d = np.array(array_2d).T
    plt.imshow(
        array_2d,
        cmap="viridis",
        interpolation="none",
        aspect="auto",
        origin="lower",
        extent=extent,
    )
    plt.colorbar()
    plt.savefig("./2d_color_plot.png", format="png")

def output_result_file(array_2d, grid_counts_x, grid_counts_y, grid_space, calc_count):
    with open("./calculated_result.txt", "w") as file:
        file.write(f"# This file shows calculated result as below.\n\n")
        file.write(f"# Calculation Parameters.\n")
        file.write(f"grid_counts_x: {grid_counts_x}\n")
        file.write(f"grid_counts_y: {grid_counts_y}\n")
        file.write(f"grid_space: {grid_space}\n")
        file.write(f"calculation_count: {calc_count}\n\n")

        file.write(f"# Calculated Matrix H.\n")
        for row in array_2d:
            line = " ".join(map(str, row))
            file.write(line + "\n")

if __name__ == "__main__":
    grid_counts_x = 100
    grid_counts_y = 100
    grid_space = 0.02
    total_calc_count = 1000

    array_2d, calc_count = calculate_equation(
        M=grid_counts_x,
        N=grid_counts_y,
        H=grid_space,
        MK=total_calc_count,
    )
    color_plot(
        array_2d=array_2d,
        grid_counts=grid_counts_x,
        grid_space=grid_space,
    )
    output_result_file(
        array_2d=array_2d,
        grid_counts_x=grid_counts_x,
        grid_counts_y=grid_counts_y,
        grid_space=grid_space,
        calc_count=calc_count,
    )
