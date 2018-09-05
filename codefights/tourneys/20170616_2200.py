
def mirrorBits(a):

    b = 0
    while a > 0:
        b <<= 1
        b |= a & 1
        a >>= 1
        pr('a b')
    return b

def subsetsSequence(sets):
    def isSubset(setA, setB):
        j = 0
        for i in range(len(setB)):
            if j < len(setA) and setA[j] == setB[i]:
                j += 1
        if j == len(setA):
            return True
        else:
            return False

    supersets = [0] * len(sets)

    for i in range(len(sets)):
        sets[i].sort()

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if isSubset(sets[i], sets[j]):
                supersets[i] += 1
            if isSubset(sets[j], sets[i]):
                supersets[j] += 1

    supersets.sort()

    # INSERT CODE HERE
    for j in range(len(sets)):
        if supersets[j] < j:
            return False
        
    return True


def test():
    testeql(mirrorBits(97), 67)
    testeql(subsetsSequence([[1,3,2], 
 [1,2], 
 [2,3], 
 [2]]), False)
    testeql(subsetsSequence([[1,3,2], 
 [2], 
 [1,2], 
 [2,1]]), True)
    testeql(subsetsSequence([[3,4,2,5], 
 [2,4], 
 [2,3,4], 
 [5,2,4], 
 [2]]), False)
