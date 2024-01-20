import matplotlib.pyplot as plt
import numpy as np
L = 0.1  # 長さ[m]
M = 10   # 分割数
dx = L/M  # 空間刻み[m]

dt = 1.0  # 時間刻み[s]
N = 100   # 時間ステップ数


alpha = 80.2 / (7874.0 * 440.0)

gamma = dt / dx**2
a = alpha * gamma

# 初期条件(温度273.15K)
T = [273.15 for i in range(M+1)]

# 境界条件
T[0] = 300.0  # 温度固定
T[M] = T[M-1]  # 断熱

# 空間方向の座標
x_values = [i * dx for i in range(M+1)]

# 計算結果を保存するリスト
result = []

for j in range(1, N):
    for i in range(1, M):
        preT = T.copy()

        # 陽解法による差分式
        T[i] = a * preT[i+1] + (1 - 2*a) * preT[i] + a * preT[i-1]
        T[0] = 300.0
        T[M] = T[M-1]

    # 計算結果をリストに追加
    result.append(T.copy())

# 結果の表示
result = np.array(result).T  # NumPyの配列に変換

# グラフのプロット
plt.figure(figsize=(10, 6))
for i in range(M+1):
    plt.plot([j * dt for j in range(N-1)], result[i], label=f'x = {i * dx:.2f}')

plt.title('Numerical Solution of Heat Conduction Equation')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.show()
