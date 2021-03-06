import csv
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib

from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler


class NNClassification(object):
    """docstring for NNClassification"""

    def __init__(self):

        self.setX = []
        self.setY = []

    def loadData(self, filename):
        """
        load and shuffle data from dataset
        """

        with open(filename) as f:
            lines = csv.reader(f)
            X = [i for i in lines]
            random.shuffle(X)  # shuffle the dataset

            for i in X:
                l = []
                for j in range(1, 5):
                    l.append(float(i[j]))
                self.setX.append(l)
                self.setY.append(i[-1])

        #     if random.random() < 0.7:
        #         TrainingX.append(l)
        #         TrainingY.append(i[-1])
        #     else:
        #         TestX.append(l)
        #         TestY.append(i[-1])

    def dataTrain(self, i, layers, activation):
        """
        train data with cross validation
        """

        TrainingX = []
        TrainingY = []
        TestX = []
        TestY = []

        size = int(len(self.setX) / 5)
        TestX = self.setX[i * size: i * size + size]
        TestY = self.setY[i * size: i * size + size]
        TrainingX = self.setX[:]
        del TrainingX[i * size:
                      i * size + size]

        TrainingY = self.setY[:]
        del TrainingY[i * size:
                      i * size + size]

        scaler = StandardScaler()
        scaler.fit(TrainingX)
        TrainingX = scaler.transform(TrainingX)
        TestX = scaler.transform(TestX)
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                            hidden_layer_sizes=layers, random_state=1,
                            activation=activation)
        # initial classification model
        clf.fit(TrainingX, TrainingY)
        y_ = clf.predict(TestX)  # predict the result of the test set
        return self.accuracy(TestY, y_)

    def accuracy(self, TestY, realY):
        """
        calculate the accuracy of test set
        """
        count = 0
        for i in range(len(TestY)):
            if TestY[i] == realY[i]:
                count += 1

        return count / len(TestY)


if __name__ == '__main__':
    obj = NNClassification()
    obj.loadData('iris.csv')
    activation = ('identity', 'logistic', 'tanh',
                  'relu')  # for kinds of activations

    for act in activation:
        layers = ()
        neutrons = 100
        avgAccuracy = []
        print("the activation is {0}".format(act))
        for i in range(10):
            accuracy = []
            layers = layers + (neutrons,)
            neutrons -= 10  # neutrons minus 10 for each layers
            for i in range(5):
                accuracy.append(obj.dataTrain(i, layers, act))
            print("the layers is {0}, the average accuracy is {1}".format(
                layers, sum(accuracy) / 5))
            avgAccuracy.append(sum(accuracy)/5)
        plt.subplot()
        plt.plot([i for i in range(10)], avgAccuracy, label=act)
        plt.xlabel('layers')
        plt.ylabel('accuracy')
        leg = plt.legend(loc='best', ncol=2, mode="expand",
                         shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.5)
    plt.show()
