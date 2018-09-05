def isoscelesTriangle(sides):
    sides.sort()
    pr('sides')
    if  sides[0] == sides[1] :
        return True
    return False



def arrayMaxConsecutiveSum(inputArray, k):

    result = 0
    currentSum = 0

    for i in range(k - 1):
        currentSum += inputArray[i]
    for i in range(k - 1, len(inputArray)):
        currentSum += inputArray[i]
        if currentSum > result:
            result = currentSum
        currentSum -= inputArray[i - k + 1]

    return result

def numbersGrouping(a):
    pass

def test():
    # testeql(isoscelesTriangle([5,3,5]), True)
    testeql(numbersGrouping([20000, 239, 10001, 999999, 10000, 20566, 29999]), 11)
