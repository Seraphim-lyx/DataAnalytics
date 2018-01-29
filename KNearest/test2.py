import numpy as np
import matplotlib.pyplot as plt
import random
import csv

from matplotlib import dates
from datetime import datetime
from sklearn import neighbors


X = []
TX = []
Y = []
with open('airline.csv', 'r') as f:
    lines = csv.reader(f)
    for i in lines:
        TX.append(datetime.strptime(i[0], '%Y-%m'))
        t = []
        y, m = i[0].split('-')
        t.append(int(y))
        t.append(int(m))
        X.append(t)
        Y.append(int(i[1]))

# print(X)
TrainingX = X[0:80]
TrainingY = Y[0:80]
TestX = X[80:]
TestY = Y[80:]
years = dates.YearLocator()
months = dates.MonthLocator()
dfmt = dates.DateFormatter('%Y')
datemin = TX[80]
datemax = TX[-1]
# print(TX[60])
n_neighbors = 5
knn = neighbors.KNeighborsRegressor(n_neighbors, weights='uniform')
y_ = knn.fit(TrainingX, TrainingY).predict(TestX)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(dfmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim(datemin, datemax)

ax.set_ylabel('passengers')
ax.scatter(TX[80:], TestY, c='k', label='data')
ax.plot(TX[80:], y_, linewidth=2, c='g', label='prediction')
# plt.scatter(TestX, TestY, c='k', label='data')
# plt.plot(TestX, y_, c='g', label='prediction')
plt.show()
