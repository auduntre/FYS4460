#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def maxwell_boltzmann_pdf(T):
    npower = 10.0**(-23)
    k = 1.38 * npower
    m = 0.028 * 6.02 * npower

    v = np.linspace(0, 300, 1000)
    plt.rc("text", usetex=True)
    plt.rc("font", size=14)

    for i, Ti in enumerate(T):
        D = (m / (2 * np.pi * k * Ti))**(3./2.) * 4 * np.pi * \
                v**2 * np.exp(- (m * v**2) / (2 * k * Ti))
        plt.plot(v, D, label="T({}) = {}".format(i, Ti))
        plt.xlabel(r"$v_{avg}$ [m/s]")
        plt.ylabel(r"$P(v_{avg})$")
        plt.title("Maxwell-Boltzmann Distribution")
    
    plt.legend()
    plt.show()


if __name__ == "__main__":
    maxwell_boltzmann_pdf([300, 600])
