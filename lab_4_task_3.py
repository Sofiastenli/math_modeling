import numpy as np
g = 10

def energy(m,h,v):
    energy = m*g*h + m*v**2/2
    print(energy)

energy(5,8,20)


