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


instance = [6.0, 3.4, 4.5, 1.6]

# print(distanceSet)
neighborSet = k.getNeighborSet(instance, 4)
print(neighborSet)

k.dataSet.append(instance)

# neighborSet = [1, 3, 4, 6]
# print(k.predictNext(neighborSet))
