import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation

xdata, ydata = [], []


def but(t):
    t = np.arange(0,12*np.pi, 0.01)
    xdata.append(np.sin(t)*(np.e**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5))
    ydata.append(np.cos(t)*(np.e**np.cos(t) - 2*np.cos(4*t) + np.sin(t/12)**5))
    ball.set_data(xdata, ydata)
    return ball,

if __name__ == '__main__': 
    fig, ax = plt.subplots()
    ball, = plt.plot([],[], 'o', color='r')

    edge = 20
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        but,
                        frames=180,
                        interval=30)
    ani.save('animation_3.gif')