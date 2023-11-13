import numpy as np
from lab_3_task_1 import acceleration_gravity as g 
h=100
a=np.pi/3
b=np.degrees(30)
V=np.sqrt(g*h*np.tan(b)**2/2*np.cos(a)**2*(1-np.tan(a)*np.tan(b)))
print(V)
