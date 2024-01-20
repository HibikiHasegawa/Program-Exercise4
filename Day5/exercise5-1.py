def gauss_elimination(matrix):
    n = len(matrix)
    
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
    solution = [row[-1] for row in matrix]
    return solution

# 連立方程式の係数行列と右辺の定数項を設定
A = [[2, 3, -1, 1],
     [1, 1, 2, 0],
     [3, -1, 1, 2]]

# ガウスの消去法を適用
solution = gauss_elimination(A)

# 解を表示
print("解:")
print(f"x = {solution[0]}")
print(f"y = {solution[1]}")
print(f"z = {solution[2]}")
