import time
import scipy.optimize as optimize
import timeit

def measure_execution_time(func):
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time

def newton_method(f, df, initial_guess, epsilon, max_iterations):
    x = initial_guess
    iteration = 0
    
    while iteration < max_iterations:
        f_x = f(x)  # 関数 f(x) の値
        f_prime_x = df(x)  # 関数 f(x) の導関数
        
        if abs(f_x) < epsilon:
            break
        
        x = x - f_x / f_prime_x
        iteration += 1
    
    return x

# 解を求めたい非線形方程式 f(x) = 0 の関数とその導関数を定義
def my_function(x):
    return x**5 - 25*x**4 + 220*x**3 - 780*x**2 + 870*x - 38

def my_derivative(x):
    return 5*x**4 - 100*x**3 + 660*x**2 - 1560*x + 870

def main():
    # ニュートン法を実行
    initial_guess = 1.0  # 初期推測値
    epsilon = 1e-6  # 収束判定のための許容誤差
    max_iterations = 100  # 最大反復回数

    # 実行時間を計測（カスタム関数）
    result_custom, execution_time_custom = measure_execution_time(lambda: newton_method(my_function, my_derivative, initial_guess, epsilon, max_iterations))

    # 実行時間を計測（SciPyのnewton関数）
    result_scipy = optimize.newton(my_function, initial_guess, fprime=my_derivative, tol=epsilon, maxiter=max_iterations)
    execution_time_scipy = timeit.timeit(lambda: optimize.newton(my_function, initial_guess, fprime=my_derivative, tol=epsilon, maxiter=max_iterations), number=1)

    print("カスタム関数での解:", result_custom)
    print("カスタム関数での実行時間:", execution_time_custom, "秒")

    print("SciPyでの解:", result_scipy)
    print("SciPyでの実行時間:", execution_time_scipy, "秒")

if __name__ == "__main__":
    main()
