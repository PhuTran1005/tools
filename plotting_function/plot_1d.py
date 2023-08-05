# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt


def line_1d(x):
    y = 2.0 * x + 1.0

    return y

if __name__ == '__main__':
    # draw 1D line using matplotlib library
    x = np.arange(0.0, 10.0, 0.01)
    y = line_1d(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r*')
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    # show the plot
    plt.show()