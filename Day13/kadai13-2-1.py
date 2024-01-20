import numpy as np
import matplotlib.pyplot as plt

def main(mode):
    # conputational domain
    xmin, xmax = 0., 1.               # 1 m
    tmin, tmax = 0., 60. * 60. * 1.   # 1 hour
    n_max = int(1e3)   # max iteration (for implicit)
    c_tol = 1e-6       # convergence tolerance (for implicit)

    # material parameter (copper)
    rho = 8960.   # density (kg / m3)
    lam = 398.    # conductivity (W / m / K)
    cap = 386.    # capacity
    D   = lam / (rho * cap)

    # discretization
    dx = 1e-2
    dt = 1e-1
    dt_star = dx ** 2 / (2. * D)   # diffusion condition
    beta = D * dt / (dx ** 2.)    # coef
    nx = 1 + int((xmax - xmin) / dx)
    nt = 1 + int((tmax - tmin) / dt)
    x = np.linspace(xmin, xmax, nx)

    # unknown vector
    u_explicit = np.ones(shape=(nx))
    u_implicit = np.ones(shape=(nx))

    # initial condition
    u_ic = 20.
    u_explicit *= u_ic
    u_implicit *= u_ic

    # boundary condition
    u_bc = 100.
    u_explicit[0]  = u_bc    # Dirichlet
    u_explicit[-1] = u_explicit[-2]   # Neumann
    u_implicit[0]  = u_bc
    u_implicit[-1] = u_implicit[-2]

    # conputational setting

    if mode == 0:
        print(">>>>> explicit")
        if dt < dt_star:
            print(">>>>> dt: %.3e, dt_star: %.3e" % (dt, dt_star))
            print(">>>>> CFL met")
        else:
            print(">>>>> dt: %.3e, dt_star: %.3e" % (dt, dt_star))
            print(">>>>> CFL NOT met, program terminating now")
            exit()
    elif mode == 1:
        print(">>>>> implicit")
        print(">>>>> dt: %.3e, dt_star: %.3e" % (dt, dt_star))

    # FDM: Finite Difference Method
    for n in range(0, nt-1):
        # Explicit method
        if mode == 0:
            v_explicit = np.copy(u_explicit)
            u_explicit[1:-1] = v_explicit[1:-1] + beta * (v_explicit[2:] - 2. * v_explicit[1:-1] + v_explicit[:-2])
            u_explicit[0] = u_bc
            u_explicit[-1] = u_explicit[-2]

        # Implicit method
        elif mode == 1:
            v_implicit = np.copy(u_implicit)
            for n_ in range(n_max):
                w_implicit = np.copy(u_implicit)
                u_implicit[1:-1] = 1. / (1. + 2. * beta) * (v_implicit[1:-1] + beta * (w_implicit[2:] + w_implicit[:-2]))
                if n_ % 10 == 0:
                    r_implicit = np.sqrt(np.sum(u_implicit - w_implicit) ** 2) / np.sum(w_implicit ** 2)
                    if r_implicit < c_tol:
                        break
            u_implicit[0] = u_bc
            u_implicit[-1] = u_implicit[-2]

        # Plot at regular intervals
        if n % int(nt / 10) == 0:
            print("step: %d / %d" % (n, nt))
            plt.figure(figsize=(8, 4))
            plt.plot(x, u_explicit, label='Explicit')
            plt.plot(x, u_implicit, label='Implicit')
            plt.xlim(-.1, 1.1)
            plt.ylim(0, 120)
            plt.title("t: %.1f min (step: %d / %d)" % (n * dt / 60., n, nt))
            plt.xlabel("x")
            plt.ylabel("u")
            plt.grid(alpha=.3)
            plt.legend()
            plt.show()  # Display the plot without saving
            plt.clf()
            plt.close()

if __name__ == "__main__":
    mode = 0  # 0 or 1 for explicit or implicit
    main(mode)
