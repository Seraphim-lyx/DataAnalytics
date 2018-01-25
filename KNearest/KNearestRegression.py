import KNearest


class KNearestRegression(KNearest.KNearest):

    def __init__(self):
        pass

    def predictNext(self, neighborSet):
        total = 0
        for i in neighborSet:
            total += i
        return total/len(neighborSet)

k = KNearestRegression()
dataSet = k.readData('data.dat', 4)


instance = [6.3, 4.2, 5.0, 2.0]
# distanceSet = k.getDistanceSet(instance, neighborSet)
# print(distanceSet)
# neighborSet = k.getNeighborSet(instance, 4)
neighborSet = [1, 3, 4, 6]
print(k.predictNext(neighborSet))
