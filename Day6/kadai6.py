import numpy as np

# 与えられた連立方程式の係数行列と右辺ベクトル
A = np.array([[9, 2, 1, 1],
              [2, 8, -2, 1],
              [-1, -2, 7, -2],
              [1, -1, -2, 6]], dtype=float)
b = np.array([20, 16, 8, 17], dtype=float)

# 初期推定値
x0 = np.zeros_like(b)

# ヤコビ法
def jacobi(A, b, x0, max_iter=100, tol=1e-6):
    x = x0.copy()
    n = len(x)
    x_history = []  # 解の履歴を保存するリスト
    for iter in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        x_history.append(x_new.copy())  # 解を履歴に追加
        if np.allclose(x, x_new, rtol=tol):
            break
        x = x_new
    return x, x_history

# ガウス・ザイデル法
def gauss_seidel(A, b, x0, max_iter=100, tol=1e-6):
    x = x0.copy()
    n = len(x)
    x_history = []  # 解の履歴を保存するリスト
    for iter in range(max_iter):
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        x_history.append(x.copy())  # 解を履歴に追加
        if np.allclose(A @ x, b, rtol=tol):
            break
    return x, x_history

# ヤコビ法での解と収束過程
x_jacobi, x_history_jacobi = jacobi(A, b, x0)
print("ヤコビ法の解:", x_jacobi)
print("ヤコビ法の収束過程:")
for i, x in enumerate(x_history_jacobi):
    print(f"Iteration {i + 1}: {x}")

# ガウス・ザイデル法での解と収束過程
x_gauss_seidel, x_history_gauss_seidel = gauss_seidel(A, b, x0)
print("ガウス・ザイデル法の解:", x_gauss_seidel)
print("ガウス・ザイデル法の収束過程:")
for i, x in enumerate(x_history_gauss_seidel):
    print(f"Iteration {i + 1}: {x}")
