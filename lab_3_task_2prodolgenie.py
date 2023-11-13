import numpy as np 
from lab_3_task_1  import bolcman_constant as k 
from lab_3_task_1 import plancks_constant as h 
from lab_3_task_1 import euler_number as e 

T = 200*k
ε = 300 #Дж
pi=3.14
N =(h/(k*T)**1.5) * (e**(-ε/k*T)) * (ε**(T/2)) * (2/np.sqrt(pi))
print(N)
