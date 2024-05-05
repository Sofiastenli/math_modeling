import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation

first=(0.5 , 0.5)
speed=0.01
t=np.pi/4

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
ax.set_xlim(0,1)
ax.set_ylim(0,1)

def update(t):
    xdata.append(speed*np.cos(t))
    ydata.append(speed*np.sin(t))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    update,
                    interval=10
                    )
ani.save('animation_5.gif')


