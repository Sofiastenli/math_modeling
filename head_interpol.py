import matplotlib.pyplot as plt 
import numpy as np
from scipy import interpolate


img = plt.imread('head.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

t1=np.linspace(np.pi/2, np.pi/4.8 ,200)
x1=0 + 380*np.cos(t1)
y1=800-430*np.sin(t1)
ax.plot(x1,y1,'-',lw=2,color='r')

t2=np.linspace(np.pi, np.pi/2.6 ,200)
x2=450+150*np.cos(t2)
y2=530 -40*np.sin(t2)
ax.plot(x2,y2,'-',lw=2,color='r')

x = np.append(x1, x2)
y = np.append(y1, y2)

x3 = [510,570.1]
y3 = [490.1,360]
ax.plot(x3,y3,'-',lw=2,color='r')

x = np.append(x, x3)
y = np.append(y, y3)

t4=np.linspace(np.pi+np.pi/6, np.pi+np.pi/2.3 ,200)
x4=420-175*np.cos(t4)
y4=320-90*np.sin(t4)
ax.plot(x4,y4,'-',lw=2,color='r')

x = np.append(x, x4)
y = np.append(y, y4)

t5=np.linspace(np.pi+np.pi/2,np.pi/2  ,200)
x5=480+70*np.cos(t5)
y5=380 -30*np.sin(t5)
ax.plot(x5,y5,'-',lw=2,color='r')

x = np.append(x, x5)
y = np.append(y, y5)


t6=np.linspace(np.pi*2, np.pi+np.pi/2 ,200)
x6=480.1 + 75*np.cos(t6)
y6=270-80*np.sin(t6)
ax.plot(x6,y6,'-',lw=2,color='r')

x = np.append(x, x6)
y = np.append(y, y6)

x7 = [550,700]
y7 = [270.1,330]
ax.plot(x7,y7,'-',lw=2,color='r')

x = np.append(x, x7)
y = np.append(y, y7)

x8 = [700.1,730]
y8 = [330.1,410]
ax.plot(x8,y8,'-',lw=2,color='r')

x = np.append(x, x8)
y = np.append(y, y8)

x9 = [730.1,650]
y9 = [410.1,680]
ax.plot(x9,y9,'-',lw=2,color='r')

x = np.append(x, x9)
y = np.append(y, y9)

x10 = [650.1,730]
y10 = [680.1,690]
ax.plot(x10,y10,'-',lw=2,color='r')

x = np.append(x, x10)
y = np.append(y, y10)

x11 = [730.2,750]
y11 = [690.1,850]
ax.plot(x11,y11,'-',lw=2,color='r')

x = np.append(x, x11)
y = np.append(y, y11)

t12=np.linspace(np.pi, np.pi/4.8 ,200)
x12=1000.1 +250*np.cos(t12)
y12=850.1-90*np.sin(t12)
ax.plot(x12,y12,'-',lw=2,color='r')

x = np.append(x, x12)
y = np.append(y, y12)


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(x, y, 'bo')
plt.plot(spline_curve[0], spline_curve[1], 'g')
plt.axis('equal')
plt.savefig('head_horse_interpole.png')