import numpy as np
import matplotlib.pyplot as plt

def get_figure():

    x = np.arange(0, 11, 1)
    y = x

    plt.plot(x, y)
    plt.title("Identity Function")
    plt.xlabel("Values of x")
    plt.ylabel("Values of y")
    plt.draw()

    return plt.gcf()