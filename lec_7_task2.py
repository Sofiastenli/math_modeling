import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)

def circle_move(R):
    a = np.arange(0,2*np.pi,0.0001)
    x = R * np.cos(a)
    y = R * np.sin(a)
    return x, y

def animate(i):
    ball.set_data(circle_move(R=i))

if __name__ == '__main__': 
    fig, ax = plt.subplots()
    ball, = plt.plot([],[], 'o', color='r')

    edge = 50
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=180,
                        interval=30)
ani.save('animation_2.gif')
