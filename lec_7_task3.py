import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)


def but(frame):
    xdata.append(np.sin(frame)*(np.e**np.cos(frame) - 2*np.cos(4*frame) + np.sin(frame/12)**5))
    ydata.append(np.cos(frame)*(np.e**np.cos(frame) - 2*np.cos(4*frame) + np.sin(frame/12)**5))
    anim_object.set_data(xdata, ydata)
    return anim_object,


   
    
    

ani = FuncAnimation(fig,
                    but,
                    frames=np.arange(0,12*np.pi, 0.1),
                    interval=100)
ani.save('animation_3.gif')