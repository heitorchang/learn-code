def prefixSums(a):
    result = []
    for i in range(len(a)):
        result.append(sum(a[:i+1]))
    return result


def phoneCall(min1, min2_10, min11, s):
    if s < min1:
        return 0
    for i in range(2, 11):
        if s < min1 + min2_10 * (i - 1):
            return i - 1
    return 10 + (s - min1 - min2_10 * 9) // min11

def houseNumbersSum(inputArray):

    numberSum = 0
    i = 0
    counter = 0
    # while True:
    while counter < 10:
        x = inputArray[i]
        i += 1
        numberSum += x
        if x == 0:
            break
        counter += 1
    return numberSum

def test():
    testeql(houseNumbersSum([5, 1, 2, 3, 0, 1, 5, 0, 2]), 11)
