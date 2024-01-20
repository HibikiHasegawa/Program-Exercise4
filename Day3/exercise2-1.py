def newton_method(initial_guess, epsilon, max_iterations):
    x = initial_guess
    iteration = 0
    
    while iteration < max_iterations:
        f_x = x**2 - 2  # 関数 f(x) = x^2 - 2
        f_prime_x = 2 * x  # 関数 f(x) の導関数
        
        if abs(f_x) < epsilon:
            break
        
        x = x - f_x / f_prime_x
        iteration += 1
    
    return x

# ニュートン法を実行
initial_guess = 1.0  # 初期推測値
epsilon = 1e-6  # 収束判定のための許容誤差
max_iterations = 100  # 最大反復回数

root_approximation = newton_method(initial_guess, epsilon, max_iterations)
print("ルート2の近似値:", root_approximation)
