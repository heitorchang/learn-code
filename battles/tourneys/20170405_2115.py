import re
def test():
    testeql(primeSum(9, 2), True)

def caseUnification(inputString):
    lowers = len(re.findall('[a-z]', inputString))
    uppers = len(re.findall('[A-Z]', inputString))
    if lowers > uppers:
        return inputString.lower()
    else:
        return inputString.upper()

def houseOfCats(legs):
    result = []
    for i in range((legs % 4) // 2, ... , 2):
        result.append(i)
    return result

def primeSum(n, k):

    primes = []
    for i in range(2, n + 1):
        ok = True
        for j in range(len(primes)):
            if primes[j] * primes[j] > i:
                break
            if i % primes[j] == 0:
                ok = False
                break
        if ok:
            primes.append(i)

    # dp[A][B] is true if number A can be represented
    # as a sum of B prime numbers
    # and false otherwise

    print(primes)
    dp = []
    for i in range(n + 1):
        dp.append([])
        for j in range(k + 1):
            dp[i].append(False)

    print(dp)
    dp[0][0] = True
    for b in range(1, k + 1):
        for a in range(2, n + 1):
            for p in primes:
                if a - p >= 0 and dp[a - p][b - 1]:
                    print(a, p, b)
                    dp[a][b] = True

    return dp[n][k]
