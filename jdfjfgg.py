import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)


A1 = 1  # Amplitude of the first sinusoid
f1 = 1  # Frequency of the first sinusoid
A2 = 2  # Amplitude of the second sinusoid
f2 = 0.5  # Frequency of the second sinusoid


num_points = 100


t = np.linspace(0, 10, num_points)
y1 = A1 * np.sin(2 * np.pi * f1 * t)
y2 = A2 * np.sin(2 * np.pi * f2 * t)


line1, = ax.plot([], [], lw=2, color='blue')
line2, = ax.plot([], [], lw=2, color='red')


def animate(i):
    y1_i = y1[:i]
    y2_i = y2[:i]

    
    line1.set_data(t[:i], y1_i)
    line2.set_data(t[:i], y2_i)

    return line1, line2,


anim = animation.FuncAnimation(fig, animate, interval=10)


plt.show()











