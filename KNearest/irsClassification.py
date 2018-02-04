import csv
import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn import neighbors, datasets

n_neighbors = 5

TrainingX = []
TrainingY = []
TestX = []
TestY = []
with open('iris.csv') as f:
    lines = csv.reader(f)
    for i in lines:
        l = []
        for j in range(1, 5):
            l.append(float(i[j]))
        if random.random() < 0.8:
            TrainingX.append(l)
            TrainingY.append(i[-1])
        else:
            TestX.append(l)
            TestY.append(i[-1])

clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
y_ = clf.fit(TrainingX, TrainingY).predict(TestX)
count = 0
for i in range(len(TestY)):
    if TestY[i] == y_[i]:
        count += 1


print(count/len(TestY))
