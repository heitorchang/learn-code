
def digitSumsDifference(n):
    digits = list(map(int, list(str(n))))
    odd = filter(lambda n: n % 2 == 1, digits)
    even = filter(lambda n: n % 2 == 0, digits)
    return sum(even) - sum(odd)

def checkSameElementExistence(arr1, arr2):
    s = set(arr1)
    t = set(arr2)
    return len(s & t) > 0


def smallestNumber(n):

    if n == 1:
        return 0

    res = 1

    for i in range(0, n+1):
        res *= 10

    return res

def numberOfOperations(a, b):

    if a < b:
        a, b = b, a
    if a % b != 0:
        return 0
    return 1 + numberOfOperations(a // b, b)

# 21:05 OWNAGE

def test():
    testeql(smallestNumber(2), 10)
    testeql(numberOfOperations(432, 72), 4)
