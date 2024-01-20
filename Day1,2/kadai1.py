import time
from scipy.optimize import bisect

def binary_search_nonlinear_equation(f, a, b, tol=1e-10, max_iter=1000):
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

def equation(x):
    return x**5 - 25*x**4 + 220*x**3 - 780*x**2 + 870*x - 38

def measure_execution_time(func):
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time

def main():
    # 解の範囲を指定
    a = 1
    b = 2

    # ライブラリを使わない場合の計測
    result_binary, execution_time_binary = measure_execution_time(lambda: binary_search_nonlinear_equation(equation, a, b))

    # ライブラリを使う場合の計測
    result_scipy, execution_time_scipy = measure_execution_time(lambda: bisect(equation, a, b))

    # 結果と実行時間を表示
    print(f"ライブラリを使わない場合の解: x ≈ {result_binary:.6f}")
    print(f"ライブラリを使わない場合の実行時間: {execution_time_binary:.6f}秒")
    
    print(f"ライブラリを使う場合の解: x ≈ {result_scipy:.6f}")
    print(f"ライブラリを使う場合の実行時間: {execution_time_scipy:.6f}秒")

if __name__ == "__main__":
    main()
