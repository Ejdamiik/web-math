import numpy as np
import matplotlib.pyplot as plt
import graph_back.formula_handle as formula_handle

def get_figure(formula: str):

    x = np.arange(-11, 11, 1)

    y = []
    for value in x:

    	y.append(formula_handle.eval_rpn(formula, {"x": value}))

    plt.plot(x, y)
    plt.title("Identity Function")
    plt.xlabel("Values of x")
    plt.ylabel("Values of y")
    plt.draw()

    return plt.gcf()