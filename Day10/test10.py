import numpy as np
import matplotlib.pyplot as plt

#微分方程式 y"-xy'+xy = 0
def func_f(y, dy_dx, x):
    
    return x * dy_dx - x * y


#4次のルンゲクッタ法
def Runge_Kutta_4():

    #範囲
    a = 0.0
    b = 1.0

    #分割
    N = 10000
    h = (b-a)/N

    
    xpoints = np.arange(a,b,h)
    ypoints = []
    dy_dx_points = []

    #初期値y(0)=1, y'(0)=1
    y = 1.0
    dy_dx = 1.0

    #ルンゲクッタ法
    for x in xpoints:

        ypoints.append(y)
        dy_dx_points.append(dy_dx)

        k1_y = h * dy_dx
        k1_dy_dx = h * func_f(y, dy_dx, x)

        k2_y = h * (dy_dx + 0.5 * k1_dy_dx)
        k2_dy_dx = h * func_f(y + 0.5 * k1_y, dy_dx + 0.5 * k1_dy_dx, x + 0.5 * h)

        k3_y = h * (dy_dx + 0.5 * k2_dy_dx)
        k3_dy_dx = h * func_f(y + 0.5 * k2_y, dy_dx + 0.5 * k2_dy_dx, x + 0.5 * h)

        k4_y = h * (dy_dx + k3_dy_dx)
        k4_dy_dx = h * func_f(y + k3_y, dy_dx + k3_dy_dx, x + h)

        y += (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        dy_dx += (k1_dy_dx + 2 * k2_dy_dx + 2 * k3_dy_dx + k4_dy_dx) / 6

   
    
    return xpoints, ypoints, dy_dx_points


#2次のルンゲクッタ法
def Runge_Kutta_2():

    # 範囲
    a = 0.0
    b = 1.0

    # 分割
    N = 10000
    h = (b - a) / N

    xpoints = np.arange(a, b, h)
    ypoints = []
    dy_dx_points = []

    # 初期値 y(0) = 1, y'(0) = 1
    y = 1.0
    dy_dx = 1.0

    # ルンゲクッタ法
    for x in xpoints:

        ypoints.append(y)
        dy_dx_points.append(dy_dx)

        k1_y = h * dy_dx
        k1_dy_dx = h * func_f(y, dy_dx, x)

        k2_y = h * (dy_dx + 0.5 * k1_dy_dx)
        k2_dy_dx = h * func_f(y + 0.5 * k1_y, dy_dx + 0.5 * k1_dy_dx, x + 0.5 * h)

        y += k2_y
        dy_dx += k2_dy_dx

   

    return xpoints, ypoints, dy_dx_points


#main
if __name__ == '__main__':

    #実行
    x1,y1,dy_dx1 = Runge_Kutta_4()

    x2,y2,dy_dx2 = Runge_Kutta_2()

    #関数yの図示　x軸 x,y軸 y
    plt.plot(x1,y1,label='Runge_Kutta_4th_order (y)')
    plt.plot(x1,y1,label='Runge_Kutta_2nd_order (y)')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()  
    plt.show()

    #関数y'の図示  x軸 y,y軸 y'
    plt.plot(y1,dy_dx1,label="Runge_Kutta_4th_order (y')")
    plt.plot(y2,dy_dx2,label="Runge_Kutta_2nd_order (y')")
    plt.xlabel("y")
    plt.ylabel("y'")
    plt.legend()  
    plt.show()