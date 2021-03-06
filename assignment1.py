import csv
import numpy as np
import matplotlib.pyplot as plt
import random

from sklearn.naive_bayes import GaussianNB
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

    def countAccuracy(self, y_):
        count = 0
        for i in range(len(self.TestY)):
            if y_[i] == self.TestY[i]:
                count += 1
        return count / len(self.TestY)


c = classification()
c.readData('iris.csv')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Neural Network
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(15,), random_state=1)
clf.fit(c.TrainingX, c.TrainingY)
y_ = clf.predict(c.TestX)

print('Accuracy for neural network is:', c.countAccuracy(y_))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# KNearest
clf = neighbors.KNeighborsClassifier(5, weights='distance')
y_ = clf.fit(c.TrainingX, c.TrainingY).predict(c.TestX)

print('Accuracy for KNearest is', c.countAccuracy(y_))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Support Vector Machine
clf = svm.SVC()

clf.fit(c.TrainingX, c.TrainingY)
y_ = clf.predict(c.TestX)


print('Accuracy for Support Vector Machine is:', c.countAccuracy(y_))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Naive Bayes
gnb = GaussianNB()
gnb.fit(c.TrainingX, c.TrainingY)
y_ = gnb.predict(c.TestX)

print('Accuracy for Gaussian Naive Bayes is', c.countAccuracy(y_))