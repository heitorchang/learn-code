def extractEachKth(inputArray, k):
    keep = [True for _ in range(len(inputArray))]
    for i in range(k-1, len(inputArray), k):
        keep[i] = False
    return [i for i, k in zip(inputArray, keep) if k]
            
def test():
    testeql(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [1, 2, 4, 5, 7, 8, 10])
    testeql(extractEachKth([1, 1, 1, 1, 1], 1), [])
