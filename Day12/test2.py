import matplotlib.pyplot as plt
import numpy as np


def _set_initial_condition(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_counts_y: int,
) -> None:
    """
    初期条件の設定

    境界以外のU値を全て0.0001とおく
    """
    for j in range(1, grid_counts_y):
        for i in range(1, grid_counts_x):
            array_2d[i][j] = 0.0001


def _set_boundary_condition(
    *,
    array_2d: list,
    grid_counts_x: int,
    grid_counts_y: int,
    grid_space: float,
) -> None:
    """境界条件の設定"""
    # y=0上の境界条件
    for i in range(grid_counts_x + 1):
        array_2d[i][0] = 0.0

    # y=M上の境界条件
    for i in range(grid_counts_x + 1):
        array_2d[i][grid_counts_y] = (
            4 * (grid_space * i) * (1.0 - grid_space * i)
        )


def _is_converged(*, U: list, UF: list, M: int, N: int) -> bool:
    """
    収束判定を行う

    誤差の合計の相対量がERROR_CONSTANT以下になったら収束と判定する
    """
    ERROR_CONSTANT: float = 0.0001  # 精度定数
    sum: float = 0.0  # 誤差の初期値
    sum0: float = 0.0

    for j in range(1, N):
        for i in range(1, M):
            sum0 += abs(U[i][j])
            sum += abs(U[i][j] - UF[i][j])

    sum = sum / sum0
    return sum <= ERROR_CONSTANT


def calculate_equation(*, M: int, N: int, H: float, MK: int) -> (list, int):
    """
    差分方程式を計算する

    本プログラムの肝となる関数
    """
    # U値のリスト
    U: list = [[0.0 for _ in range(M + 1)] for _ in range(N + 1)]
    # U値のリスト(精度判定用)
    UF: list = [[0.0 for _ in range(M + 1)] for _ in range(N + 1)]

    # 初期値設定
    _set_initial_condition(
        array_2d=U,
        grid_counts_x=M,
        grid_counts_y=N,
    )
    _set_boundary_condition(
        array_2d=U,
        grid_counts_x=M,
        grid_counts_y=N,
        grid_space=H,
    )

    # 計算
    calc_count: int = 0
    for _ in range(MK):
        for j in range(1, N):
            for i in range(1, M):
                UF[i][j] = U[i][j]  # 収束判定に必要なため、UをUFにコピー
                U[i][j] = (
                    U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1]
                ) / 4.0
        calc_count += 1

        # 収束判定
        if _is_converged(U=U, UF=UF, M=M, N=N):
            print("収束しました")
            break
    return U, calc_count


def color_plot(
        *, 
        array_2d: list, 
        grid_counts: int, 
        grid_space: float,
    ) -> None:
    """
    2次元カラープロット

    array_2dのi行j列のままimshowでプロットすると、
    原点が左上、横軸が右向き、縦軸が下向きになる。
    そこで、array_2dをx軸、y軸としてプロットするために、
    転置してからorigin="lower"で縦軸を上向きにしてプロットする。
    """
    # グラフの軸の範囲を指定
    min_x_y = 0.0 - grid_space / 2
    max_x_y = grid_space * grid_counts + grid_space / 2
    extent=(min_x_y, max_x_y, min_x_y, max_x_y)
    
    # 2次元配列を転置
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


def output_result_file(
    array_2d: list,
    grid_counts_x: int,
    grid_counts_y: int,
    grid_space: float,
    calc_count: int,
) -> None:
    """2次元配列をテキストファイルに書き出す"""
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
    """
    楕円形方程式の数値解法（ガウス-ザイデル法）

    grid_counts_x = grid_counts_y の前提で実装をしている
    grid_spaceは刻み幅であり、grid_space = 1 / grid_counts_x となる
    """
    grid_counts_x: int = 10  # 格子点番号mの値
    grid_counts_y: int = 10  # 格子点番号nの値
    grid_space: float = 0.1  # 刻み幅
    total_calc_count: int = 1000  # 総計算回数

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