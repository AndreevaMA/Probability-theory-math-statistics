
import numpy as np

def studentTTest2(array1, array2):
    x_mean = np.mean(array1)
    y_mean = np.mean(array2)
    x_var = np.var(array1, ddof = 1)
    y_var = np.var(array2, ddof = 1)
    n_x = len(array1)
    n_y = len(array2)

    t_emp = (x_mean - y_mean) / np.sqrt(x_var / n_x + y_var / n_y)
    return t_emp