import matplotlib.pyplot as plt 
import numpy as np

def cicloide(R=5 ):
    t = np.arange(1,10,0.1)
    x = R * (t- np.sin(t))
    y = R * (1 - np.cos(t))


    plt.plot(x, y, ls='--', lw=3)
    plt.axis('equal')
    plt.savefig('fig_1.png')

if __name__ == '__main__':
    cicloide()
    