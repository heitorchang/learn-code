def sumOfDivisors(n):
    divs = []
    for i in range(1, n+1):
        if n % i == 0:
            divs.append(i)

    pr('divs')
    return sum(divs)

def sumDigits(n):
    return int(sum(map(int, str(n))))

def reversedSumOfDigits(p, n):
    for i in range(start, end):
        if sumDigits(i) == p:
            return str(i)
    return "-1"

def alphabeticShift(inputString):
    result = ""
    for c in list(inputString):
        o = ord(c)
        if o == 122:
            result += "a"
        else:
            result += chr(o+1)
    return result

def knightsAndKnaves(answers):

    n = len(answers)
    isKnight = [False] * n
    isKnight[0] = True
    for i in range(1, n):
        isKnight[i] = answers[0] >> i & 1
    for i in range(n):
        for j in range(n):
            if ((isKnight[i] == isKnight[j]) ^
                    ((answers[i] >> j & 1))):
                return False
    return True

def sameDigitNumber(n):
    digit = n // 10
    pr('digit')
    while n != 0:
        if n % 10 != digit:
            return False
        n //= 10
    return True

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    #return digits[::-1]
    dd = digits[::-1]
    return ''.join(list(map(str, dd)))


def applesDistribution(apples, boxCapacity, maxResidue):
    result = 0
    for i in range(1, boxCapacity + 1):
        if apples % i <= maxResidue :
            result += 1
    return result


def maximalAllowableSubarrays(inputArray, maxSum):

    right = [0] * len(inputArray)
    j = 0
    curSum = 0
    for i in range(len(inputArray)):
        if i > 0:
            curSum -= inputArray[i-1]
        while j + 1 < len(inputArray) and curSum + inputArray[j + 1] <= maxSum:
            j += 1
            curSum += inputArray[j]
        right[i] = j

    return right


def isSumOfConsecutive2(n):
    tot = 0
    for i in range(1, n):
        sum = i
        add = i + 1
        while sum <= n:
            sum += add
            pr('i sum')
            if sum == n:
                tot += 1
            add += 1

    return tot


def test():
    testeql(applesDistribution(7, 4 ,1), 3)
    # testeql(maximalAllowableSubarrays([2, 3, 0, 1, 2], 4), [0, 3, 4, 4, 4])
    # testeql(maximalAllowableSubarrays([1, 1, 1, 1, 1, 1], 2), [1,2,3,4,5,5])
    # testeql(isSumOfConsecutive2(9), 2)
    # testeql(isSumOfConsecutive2(15), 3)
