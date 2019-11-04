
def appleBoxes(k):

    sum = 1
    x = 0
    while x <= k:
        if x % 2 == 0:
            sum += x * x
        else:
            sum -= x * x
        x += 1

    return sum


def checkEqualFrequency(inputArray):

    numberOfEqual = 1

    inputArray.sort()

    while (numberOfEqual < len(inputArray)
            and inputArray[numberOfEqual - 1] == inputArray[numberOfEqual]):
        numberOfEqual += 1

    if len(inputArray) % numberOfEqual == 0:
        return False

    for i in range(0, len(inputArray), numberOfEqual):
        if i > 0 and inputArray[i] == inputArray[i - 1]:
            return False
        j = i + 1
        while j < i + numberOfEqual:
            if inputArray[j] != inputArray[j - 1]:
                return False
            j += 1

    return True

def letter(i):
    return chr(97+i)

def msgSum(m):
    return sum(map(lambda c: ord(c) - 97, list(m))) % 26

def cipher26(message):
    # phail
    dec = ""
    for i in range(len(message)-1,-1,-1):
        dec += letter(msgSum(message[:i]))
    return dec

def gcdEuclid(a, b):
    if a == 0:
        return b
    return gcdEuclid(b % a, a)


def maxFraction(numerators, denominators):
    ratios = [a / b for (a, b) in zip(numerators, denominators)]
    maxInx = 0
    maxVal = ratios[0]
    for i in range(1, len(ratios)):
        if ratios[i] > maxVal:
            maxVal = ratios[i]
            maxInx = i
    return maxInx


def test():
    # testeql(appleBoxes(15), -120)
    # testeql(appleBoxes(5), -15)
    # testeql(checkEqualFrequency([1,2,2,1]), True)
    # testeql(checkEqualFrequency([1, 2, 2, 3, 1, 3, 1, 3]), False)
    # testeql(cipher26("taiaiaertkixquxjnfxxdh"), "thisisencryptedmessage")
    testeql(maxFraction([5, 2, 5], [6, 3, 4]), 2)
