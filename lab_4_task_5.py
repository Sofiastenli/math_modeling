import numpy as np
def calculate_plosad(shape,a,b,r,h):
    if shape == 'круг':
        square=np.pi*r**2
    elif shape == 'треугольник':
        square=0.5*a*h
    elif shape == 'прямоугольник':
        square=a*b

print(calculate_plosad('круг',r=5))
