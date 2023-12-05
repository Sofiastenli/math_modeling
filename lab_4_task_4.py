import numpy as np


def simple_func(a,b,N):
    x = np.linspace(a, b, N)
    y=x**2
    return y


print(simple_func(4, 7, 100))


