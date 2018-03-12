from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

i=1
a = [1,2,3,4,5]
b = [2,3,4,5,6]
c = [3,4,2,1,2]
plt.subplots(2)
plt.plot(a,b, label = 'test')
leg = plt.legend()

plt.plot(a,b, label = 'test')
leg = plt.legend()
plt.show()