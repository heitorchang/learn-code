def create2DArray(lengths):
    out = []
    for l in lengths:
        out.append(list(range(l)))
    return out

def extractEachKth(inputArray, k):

    result = []
    for i in range(len(inputArray)):
        if (i + 1) % k != 0:
            result.append(inputArray[i])
    return result

def test():
    testeql(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [1, 2, 4, 5, 7, 8, 10])
