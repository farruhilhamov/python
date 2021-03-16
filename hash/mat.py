from matplotlib import pyplot as plt
import matplotlib
from math import *
import numpy as np
from numpy.core.fromnumeric import shape, sort
def func():
    l = []
    #x = [sin(n**2+n**2) for n in list]
    #y = [cos(n*n)**23 for n in list]
    x = np.random.randint(0,1000,100)
    y = np.random.randint(0,1000,100)
    #x,y=sin(x),sin(y)
    print(sort(x),"\n",sort(y))
    x,y = sort(x),sort(y)
    for i in x:
        l.append([sin(i)**2])
    for i in y:
        l.append([cos(i)**2])
    
    return l
print(func())
plt.plot(func())
plt.show()