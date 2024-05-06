import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

A1, f1 = 1, 1
A2, f2 = 0.5, 2


fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)


line1, = ax.plot([], [], label='A=1, f=1')
line2, = ax.plot([], [], label='A=0.5, f=2')


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    
    return line1, line2, 


def update(frame):
    t = np.linspace(0, frame, 100)
    y1 = A1 * np.sin(f1 * t)
    y2 = A2 * np.sin(f2 * t)
    
    line1.set_data(t, y1)
    line2.set_data(t, y2)
    
    
    
    return line1, line2, 


ani = animation.FuncAnimation(fig, update, frames=100, init_func=init)

plt.legend()
plt.show()


