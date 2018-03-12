from sklearn.naive_bayes import GaussianNB
import csv
import numpy as np
import matplotlib.pyplot as plt
import random

gnb = GaussianNB()


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

y_ = gnb.fit(c.TrainingX, c.TrainingY).predict(c.TestX)
count = 0
for i in range(len(c.TestY)):
    if c.TestY[i] == y_[i]:
        count += 1
print(count / len(c.TestY))
