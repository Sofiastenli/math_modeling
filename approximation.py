import matplotlib.pyplot as plt 
import numpy as np



img = plt.imread('head.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

t=np.linspace(np.pi/2, np.pi/4.8 ,100)
x=0 + 380*np.cos(t)
y=800-430*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

t=np.linspace(np.pi, np.pi/2.6 ,200)
x=450+150*np.cos(t)
y=530 -40*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

x = [510,570]
y = [490,360]
ax.plot(x,y,'-',lw=2,color='r')

t=np.linspace(np.pi+np.pi/6, np.pi+np.pi/2.3 ,100)
x=420-175*np.cos(t)
y=320-80*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

t=np.linspace(np.pi+np.pi/2,np.pi/2  ,100)
x=480+130*np.cos(t)
y=360 -30*np.sin(t)
ax.plot(x,y,'-',lw=2,color='r')

plt.savefig('horse.png')



