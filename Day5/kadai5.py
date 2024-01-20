def gauss_elimination(matrix):
    n = len(matrix)
    solutions = [0] * n

    for i in range(n):
        # ピボット選択
        max_row = i
        for j in range(i+1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # ピボット要素を1にする
        pivot = matrix[i][i]
        for j in range(i, n+1):
            matrix[i][j] /= pivot

        # ガウスの消去法を適用
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n+1):
                    matrix[k][j] -= factor * matrix[i][j]

    # 解の取り出し
    for i in range(n):
        solutions[i] = matrix[i][n]

    return solutions

# 連立方程式の係数行列と右辺の定数項を設定
A = [[2, 7, -1, 5, -3, 6],
     [1, -4, 2, -1, 6, 1],
     [3, 1, -9, -2, 1, -2],
     [10, -2, -5, 8, -7, 4],
     [-4, 3, 12, -4, -2, -10]]

# ガウスの消去法を適用
solutions = gauss_elimination(A)

# 解を表示
print("解:")
print(f"x = {solutions[0]}")
print(f"y = {solutions[1]}")
print(f"z = {solutions[2]}")
print(f"u = {solutions[3]}")
print(f"w = {solutions[4]}")
