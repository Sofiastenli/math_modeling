import matplotlib.pyplot as plt
import numpy as np
def giperbola(a=1):
    x = np.arange(-15,15,0.5)
    y = a/x
    plt.plot(x,y)
    plt.savefig('fig_2.png')
	
if __name__ == '__main__':
	giperbola()