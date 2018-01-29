import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
import random
import csv
from datetime import datetime
from sklearn import neighbors

X = []
y = []
year = 2015
with open('airline.csv', 'r') as f:
    lines = csv.reader(f)
    for i in lines:
        X.append(datetime.strptime(i[0], '%Y-%m'))
        y.append(int(i[1]))


years = dates.YearLocator()
months = dates.MonthLocator()
dfmt = dates.DateFormatter('%Y')
datemin = X[0]
datemax = X[-1]
print(datemax)
TT = []
for i in X:
    t = []
    t.append(i)
    TT.append(t)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(dfmt)
ax.xaxis.set_minor_locator(months)
ax.set_xlim(datemin, datemax)
ax.set_ylabel('passenger')
ax.plot(X, y, linewidth=2)
fig.set_size_inches(18, 4)

# plt.show()
