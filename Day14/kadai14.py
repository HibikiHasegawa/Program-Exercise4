import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class LaplaceSolver:
    def __init__(self, Lx, Ly, Nx, Ny, omega=1.9):
        self.Lx, self.Ly = Lx, Ly
        self.Nx, self.Ny = Nx, Ny
        self.dx, self.dy = Lx / (Nx - 1), Ly / (Ny - 1)
        self.omega = omega

    def initialize_phi(self):
        phi = np.zeros((self.Nx, self.Ny))
        phi[:, 0] = 0
        phi[:, -1] = np.linspace(0, 1, self.Nx)
        phi[0, :] = 0
        phi[-1, :] = np.linspace(0, 1, self.Ny)
        return phi

    def laplace_jacobi(self, phi, max_iter=10000, tolerance=1e-5):
        iterations = 0
        for _ in range(max_iter):
            old_phi = phi.copy()
            for i in range(1, self.Nx - 1):
                for j in range(1, self.Ny - 1):
                    phi[i, j] = 0.25 * (old_phi[i + 1, j] + old_phi[i - 1, j] + old_phi[i, j + 1] + old_phi[i, j - 1])
            iterations += 1
            if np.max(np.abs(phi - old_phi)) < tolerance:
                break
        return phi, iterations

    def laplace_gauss_seidel(self, phi, max_iter=10000, tolerance=1e-5):
        iterations = 0
        for _ in range(max_iter):
            old_phi = phi.copy()
            for i in range(1, self.Nx - 1):
                for j in range(1, self.Ny - 1):
                    phi[i, j] = 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1])
            iterations += 1
            if np.max(np.abs(phi - old_phi)) < tolerance:
                break
        return phi, iterations

    def laplace_sor(self, phi, max_iter=10000, tolerance=1e-5):
        iterations = 0
        for _ in range(max_iter):
            old_phi = phi.copy()
            for i in range(1, self.Nx - 1):
                for j in range(1, self.Ny - 1):
                    phi[i, j] = (1 - self.omega) * phi[i, j] + self.omega * 0.25 * (
                            phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1])
            iterations += 1
            if np.max(np.abs(phi - old_phi)) < tolerance:
                break
        return phi, iterations

    def plot_solution(self, method, phi, title):
        x = np.linspace(0, self.Lx, self.Nx)
        y = np.linspace(0, self.Ly, self.Ny)
        X, Y = np.meshgrid(x, y)
        fig = plt.figure(figsize=(6, 4))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, phi.T, cmap='viridis')
        ax.set_title(title)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Phi')
        plt.show()

def main():
    Lx, Ly = 1.0, 1.0
    Nx, Ny = 50, 50
    omega = 1.9
    solver = LaplaceSolver(Lx, Ly, Nx, Ny, omega)

    phi = solver.initialize_phi()

    phi_jacobi, i_j = solver.laplace_jacobi(phi.copy())
    phi_gauss_seidel, i_g = solver.laplace_gauss_seidel(phi.copy())
    phi_sor, i_s = solver.laplace_sor(phi.copy())

    print("jacobi:", i_j, "/ gauss_seidel:", i_g, "/ sor:", i_s)

    solver.plot_solution("Jacobi Method", phi_jacobi, 'Jacobi Method')
    solver.plot_solution("Gauss-Seidel Method", phi_gauss_seidel, 'Gauss-Seidel Method')
    solver.plot_solution(f'SOR Method (omega={solver.omega})', phi_sor, f'SOR Method (omega={solver.omega})')

if __name__ == "__main__":
    main()
