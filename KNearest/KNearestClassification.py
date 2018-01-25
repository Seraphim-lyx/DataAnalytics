import KNearest
import operator


class KClassification(KNearest.KNearest):
    """docstring for ClassName"""

    def __init__(self):
        pass

    def voteResult(self, neighborSet):
        voteSet = {}
        result = None
        v = 0
        for i in neighborSet:
            if i in voteSet:
                voteSet[i] += 1
            else:
                voteSet[i] = 1

        for key, value in voteSet.items():
            if value > v:
                v = value
                result = key
        return result


s = ['a', 'a', 'b', 'c', 'c', 'c']


# test.iteritems()
k = KClassification()
result = k.voteResult()
