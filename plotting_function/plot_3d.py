import numpy as np
import matplotlib.pyplot as plt


def linear_function_3d(x1, x2, x3, beta, omega1, omega2, omega3):
    y = x1 * omega1 + x2 * omega2 + x3 * omega3

    return y

if __name__ == '__main__':
    # define the parameters
    beta1 = 0.5
    beta2 = 0.2
    omega11 = -1.0
    omega12 = 0.4
    omega13 = -0.3
    omega21 = 0.1
    omega22 = 0.1
    omega23 = 1.2

    # define the inputs
    x1 = 4
    x2 = -1
    x3 = 2

    # compute using the individual equations
    y1 = linear_function_3d(x1, x2, x3, beta1, omega11, omega12, omega13)
    y2 = linear_function_3d(x1, x2, x3, beta2, omega21, omega22, omega23)
    print("Individual equations...")
    print('y1 = %3.3f\n y2 = %3.3f' % ((y1, y2)))

    # define vectors and matrices
    beta_vec = np.array([[beta1], [beta2]])
    omega_mat = np.array([
        [omega11, omega12, omega13],
        [omega21, omega22, omega23]
    ])
    x_vec = np.array([[x1], [x2], [x3]])

    # compute with vector / matrix form
    y_vec = beta_vec + np.matmul(omega_mat, x_vec)
    print("Matrix / vector form")
    print('y1 = %3.3f\n y2 = %3.3f' % ((y_vec[0], y_vec[1])))