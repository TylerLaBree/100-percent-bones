import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def exponential(x, a, b):
    return a * b**x


def get_curve_pars(d20, d21):
    year = np.linspace(1, 120, num=120)
    temp_20 = np.linspace(0, d20*100, num=100)
    temp_21 = np.linspace(d20*101, d20*100 + d21*20, num=20)
    temp = np.concatenate((temp_20, temp_21), axis=None)

    # print(temp)
    # plt.plot(year, temp)

    (param, cov) = curve_fit(exponential, year, temp, p0=[0.1, 1.05])
    # print(param)
    perr = np.sqrt(np.diag(cov))

    fit = exponential(year, param[0], param[1])
    # plt.plot(year, temp, 'r-', year, fit, 'b')

    # plt.show()
    return [param, perr]


# param, perr = get_curve_pars(0.019, 0.036)
# print(param)
