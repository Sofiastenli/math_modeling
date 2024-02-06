import matplotlib.pyplot as plt
import numpy as np

def circle_plotter(a=5, b=4):
    
    x = np.arange(-2*a, 2*a, 0.01)
    y = np.arange(-2*a, 2*a, 0.01)
    
    
    X, Y = np.meshgrid(x, y)
    fxy = X**2/a**2 + Y**2/b**2 - 1

    plt.contour(X, Y, fxy, levels=[0])
    plt.savefig('fig_4.png')
    
if __name__ == '__main__':
	circle_plotter()