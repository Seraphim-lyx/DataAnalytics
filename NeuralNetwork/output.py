from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

a = [1,2,3,4,5]
b = [2,3,4,5,6]
c = [3,4,2,1,2]
plt.subplot(221)
plt.plot(a,b, label = 'test')
plt.subplot(222)
plt.plot(a,c, label = 'test')
leg = plt.legend()
plt.show()