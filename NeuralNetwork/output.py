import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

a = [1,2]
b = [3,4]
c = [[1.5,1.5],[2,2]]
plt.contourf(a,b,c,cmap=plt.cm.Paired)
plt.show()