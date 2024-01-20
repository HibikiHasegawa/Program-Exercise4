import numpy as np
import matplotlib.pyplot as plt

# データ
x = np.array([0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00])
y = np.array([2.4824, 1.9975, 1.6662, 1.3775, 1.0933, 0.7304, 0.4344, 0.2981, -0.0017, -0.0026])

# 多項式の次数を入力
m = int(input("多項式の次数を入力してください: "))

# 多項式の係数を計算
coefficients = np.polyfit(x, y, m)

# フィット曲線の生成
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = np.polyval(coefficients, x_fit)

# 係数の表示
print("係数:", coefficients)

# データ点とフィット曲線のプロット
plt.scatter(x, y, label='Data Points')
plt.plot(x_fit, y_fit, label=f'Fitted Curve (Degree {m})', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Polynomial Curve Fitting (Degree {m})')
plt.legend()
plt.show()
