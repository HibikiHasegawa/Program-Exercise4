import time

def binary_search_nonlinear_equation(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) と f(b) は異なる符号である必要があります。")
    
    iter_count = 0
    
    while (b - a) / 2.0 > tol and iter_count < max_iter:
        c = (a + b) / 2.0
        if f(c) == 0.0:
            return c  # 解が見つかった場合
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2.0  # 解が見つからなかった場合、最も近い近似値を返す

# 解きたい非線形方程式の関数を定義
def equation(x):
    return x**3 - 3*x**2 + 9*x - 8

# 解の範囲を指定
a = 1
b = 2
start = time.perf_counter()
# 二分法を使用して非線形方程式を解く
result = binary_search_nonlinear_equation(equation, a, b)
end = time.perf_counter()
print("解:", result)
print(end - start)
