import math
import operator


class KNearest(object):
    """docstring for KNearest"""

    dataSet = []

    def __init__(self):
        pass

    def readData(self, fileName, attrLength):
        """

        """
        with open(fileName) as f:
            line = f.readline().strip()
            while line is not "":
                line = line.split(',')
                for i in range(attrLength):
                    line[i] = float(line[i])
                self.dataSet.append(line)
                line = f.readline().strip()
        return self.dataSet

    def getNeighborSet(self, k):
        neighborSet = []
        for i in range(k):
            neighborSet.append(self.dataSet[-i-1])

        return neighborSet

    def getDistance(self, dataSet1, dataSet2, attrLength):
        total = 0
        for j in range(attrLength):
            total += pow(dataSet1[j]-dataSet2[j], 2)

        return math.sqrt(total)

    def getDistanceSet(self, dataInstance, neighborSet):
        distanceSet = []
        for neighbor in neighborSet:
            distanceSet.append(
                (neighbor, self.getDistance(neighbor, dataInstance, 3)))
        distanceSet.sort(key=operator.itemgetter(1))
        return distanceSet


# print(obj.getDistanceSet(data1, data2))
