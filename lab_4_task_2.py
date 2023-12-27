import numpy as np

def calculate(massive):
    s = 1
    for i in massive:
        s=s*i
   
    print(s)

mass1=np.arange(1,10,1)
calculate(mass1)



