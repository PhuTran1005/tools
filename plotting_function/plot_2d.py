import numpy as np
import matplotlib.pyplot as plt


def draw_2d_function(x1_mesh, x2_mesh, y):
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 7)
    pos = ax.contourf(x1_mesh, x2_mesh, y, levels=256, cmap='hot', vmin=-10.0, vmax=10.0)
    fig.colorbar(pos, ax=ax)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    levels = np.arange(-10.0, 10.0, 1.0)
    ax.contour(x1_mesh, x2_mesh, y, levels, cmap='winter')

    plt.show()

def linear_function_2d(x1, x2, beta, omega1, omega2):
    y = x1 * omega1 + x2 * omega2 + beta

    return y

if __name__ == '__main__':
    x1 = np.arange(0.0, 10.0, 0.1)
    x2 = np.arange(0.0, 10.0, 0.1)
    x1, x2 = np.meshgrid(x1, x2)

    # compute 2d function for given values of omega1, omega2
    beta = 0.0
    omega1 = 1.0
    omega2 = -0.5
    y = linear_function_2d(x1, x2, beta, omega1, omega2)

    # call draw function
    draw_2d_function(x1, x2, y)