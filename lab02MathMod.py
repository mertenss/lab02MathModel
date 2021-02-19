from math import *

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"Написал r1 r2, для двух случаев, аккуратно комментим r1 и первую строчку " \
"матплотлиба чтобы получить реультат второго случая, аналогично для первого"

def model(r, theta):
    return r/sqrt(5.76)


if __name__ == "__main__":
    theta_range1 = np.linspace(0, 360, 100)
    r0 = 7.1/3.4

    theta_range2 = np.linspace(-180, 180, 100)
    r0_1 = 7.1/1.4

    #r1 = odeint(model, r0, theta_range1)
    r2 = odeint(model, r0_1, theta_range2)

    #matplotlib.pyplot.polar(theta_range1, r1)
    matplotlib.pyplot.polar(theta_range2, r2)
    plt.show()