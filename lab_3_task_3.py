import numpy as np
from lab_3_task_1 import acceleration_gravity as g 
x0=0
y0=7
V0=9

t= np.arange(0,5,0.1)
x = x0 + V0*t 
y = y0 +V0*t-g*t**2/2
coords=np.zeros((len(t),3))
for i in range(0,len(t)):
    coords[i,0]=t[i]
for j in range(0,len(x)):
    coords[0,j]=x[j]
print(coords)
    





    
 
  
