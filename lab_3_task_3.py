import numpy as np
from lab_3_task_1 import acceleration_gravity as g 
x0=int(input('введите начальное положение тела на ось X :'))
y0=int(input('введите начальное положение тела на ось Y:'))
V0=int(input('введите начальную скорость тела:'))
t = int(input('введите время движения:'))
t= np.arange(0,5,0.1)
x = x0 + V0*t 
y = y0 +V0*t-g*t**2/2

print(t,x,y)
    





    
 
  
