import numpy as np
import matplotlib.pyplot as plt
import graph_back.formula_handle as formula_handle

def get_figure(formula: str):

    x = np.arange(-11, 11, 1)

    y = []
    for value in x:

    	y.append(formula_handle.eval_rpn(formula, {"x": value}))

    ax = plt.axes()
    ax.set_facecolor("#849488")

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.title(f"Latest: {formula}")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.plot(x, y)

    return plt.gcf()