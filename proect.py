import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()

first=(0.5,0.5)
t=(2*np.pi)
xdata, ydata = [], []

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
anim_object, = plt.plot([], [], color='b', lw=2)
anim_tail, = plt.plot([], [], color='r', lw=0.5)

def animate(i):
    x,y=first
    x+=0.01*np.cos(t)
    y+=0.01*np.sin(t)
    anim_object.set_data([x,first[0]], [y,first[1]])
    tail_x=np.linspace(first[0],xdata,15)
    tail_y=np.linspace(first[1],ydata,15)
    anim_tail.set_data(tail_x,tail_y)
    return anim_object, anim_tail,


 
ani = FuncAnimation(fig,
                    animate,
                    interval=10
                    )
ani.save('animation_5.gif')


