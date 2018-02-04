import csv
import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn.neural_network import MLPClassifier
from sklearn import neighbors
from sklearn import svm


class classification(object):
    """docstring for classification"""
    TrainingX = []
    TrainingY = []
    TestX = []
    TestY = []

    def readData(self, filename):
        with open(filename) as f:
            lines = csv.reader(f)
            for i in lines:
                l = []
                for j in range(1, 5):
                    l.append(float(i[j]))
                if random.random() < 0.8:
                    self.TrainingX.append(l)
                    self.TrainingY.append(i[-1])
                else:
                    self.TestX.append(l)
                    self.TestY.append(i[-1])


c = classification()
c.readData('iris.csv')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Neural Network
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(15,), random_state=1)
clf.fit(c.TrainingX, c.TrainingY)
y_ = clf.predict(c.TestX)
count = 0
for i in range(len(c.TestY)):
    if c.TestY[i] == y_[i]:
        count += 1
print('Accuracy for neural network is:', count/len(c.TestY))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# KNearest
clf = neighbors.KNeighborsClassifier(5, weights='distance')
y_ = clf.fit(c.TrainingX, c.TrainingY).predict(c.TestX)
count = 0
for i in range(len(c.TestY)):
    if c.TestY[i] == y_[i]:
        count += 1
print('Accuracy for KNearest is', count/len(c.TestY))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Support Vector Machine
clf = svm.SVC()

clf.fit(c.TrainingX, c.TrainingY)
y_ = clf.predict(c.TestX)
count = 0
for i in range(len(c.TestY)):
    if c.TestY[i] == y_[i]:
        count += 1


print('Accuracy for Support Vector Machine is:', count/len(c.TestY))
