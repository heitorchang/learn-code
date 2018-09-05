def insertDashes(inputString):
    words = inputString.split()
    res = ""
    for w in words:
        wl = list(s)
        res += "-".join(wl)
    return res

def isLuckyNumber(n):
    while n > 0:
        tmpDigit = n % 10
        if tmpDigit != 7 and tmpDigit != 4:
            return False
        n = n // 10
    return True


def leastFactorial(n):
    fact = 1
    if n == 1:
        return 1
    lastFact = fact
    i = 2
    while True:
        fact *= i
        if fact >= n:
            return fact
        lastFact = fact
        i += 1

def isInfiniteProcess(a, b):
    return a > b or (b - a) % 2 == 1


def countDivisors(n):
    tot = 0
    for i in range(1, n+1):
        if n % i == 0:
            tot += 1
    return tot
    
def divNumber(k, l, r):
    res = 0
    for i in range(l, r+1):
        if countDivisors(i) == k:
            res += 1
    return res
    
def test():
    testeql(isLuckyNumber(47), True)
    testeql(leastFactorial(17), 24)
