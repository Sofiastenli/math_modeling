import numpy as np

g = 10

def energy(h,m,v):
    total_enegy =  m * g * h + (m*v**2)/2
    print(total_enegy)


energy(5,7,4)
