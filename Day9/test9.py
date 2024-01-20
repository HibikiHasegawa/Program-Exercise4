import numpy as np
import matplotlib.pyplot as plt

#微分方程式dy/dx
def func_f(y, x):
    return np.exp(-np.sin(x)) - y * np.cos(x)


#4次のルンゲクッタ法
def Runge_Kutta_4():

    #範囲
    a = 0.0
    b = 100.0

    #分割
    N = 10000
    h = (b-a)/N

    
    xpoints = np.arange(a,b,h)
    ypoints = []

    #初期値y(0)=1
    y = 1.0

    #ルンゲクッタ法
    for x in xpoints:
        ypoints.append(y)
        k1 = h*func_f(y, x)
        k2 = h*func_f(y+0.5*k1, x+0.5*h)
        k3 = h*func_f(y+0.5*k2, x+0.5*h)
        k4 = h*func_f(y+k3, x+h)
        y += (k1+2*k2+2*k3+k4)/6

    #関数yの図示
    plt.plot (xpoints, ypoints,label = 'Runge_Kutta 4th order')
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.show()
    
    return xpoints, ypoints


#オイラー法
def Euler():

    DELTA_X = 0.01
    MAX_X = 100.0

    #初期値
    x = 0.0 
    y = 1.0 

    y_hist = [y]
    x_hist = [x]

    #積分部分を長方形近似
    while x < MAX_X:
        y += func_f(y,x)*DELTA_X
        x += DELTA_X
        y_hist.append(y)
        x_hist.append(x)

    #関数yの図示 
    plt.plot(x_hist, y_hist,label = 'Euler')
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.show()

    return x_hist,y_hist


#2次のルンゲクッタ法
def Runge_Kutta_2():

    DELTA_X = 0.01
    MAX_X = 100.0

    # 初期値
    x = 0.0 
    y = 1.0 

    y_hist = [y]
    x_hist = [x]

    #中点を利用した近似
    while x < MAX_X:
        k1 = DELTA_X * func_f(y, x)
        k2 = DELTA_X * func_f(y + 0.5 * k1, x + 0.5 * DELTA_X)
        y += k2
        x += DELTA_X
        y_hist.append(y)
        x_hist.append(x)

    #関数yの図示 
    plt.plot(x_hist, y_hist, label='Runge-Kutta 2nd Order')
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.show()

    return x_hist, y_hist


#main
if __name__ == '__main__':

    #実行
    x1,y1 = Runge_Kutta_4()
    x2,y2 = Euler()
    x3,y3 = Runge_Kutta_2()

    #関数yの図示
    plt.plot(x1,y1,label='Runge_Kutta_4th_order')
    plt.plot(x2,y2,label='Euler')
    plt.plot(x3,y3,label='Runge_Kutta_2nd_order')
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()  
    plt.show()