import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation

xdata, ydata = [], []


def heart(t):
    t = np.arange(0,2*np.pi, 0.01)
    xdata.append(16*np.sin(t)**3)
    ydata.append(13*np.cos(t) - 5*np.cos(2*t) - 2**np.cos(3*t) - np.cos(4*t))
    ball.set_data(xdata, ydata)
    return ball,

if __name__ == '__main__': 
    fig, ax = plt.subplots()
    ball, = plt.plot([],[], color='r')

    edge = 30
    plt.axis('equal')
    
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        heart,
                        frames=100,
                        interval=40)
    ani.save('animation_3_2.gif')