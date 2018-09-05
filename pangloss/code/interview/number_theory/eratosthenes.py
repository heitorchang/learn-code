def primes(n):
    if n < 2:
        return []
    isPrime = [True] * (n+1)
    for base in range(3, int(n ** 0.5) + 1, 2):
        for multiple in range(base * 2, n+1, base):
            isPrime[multiple] = False
    primeList = [2]
    for n in range(3, n+1, 2):
        if isPrime[n]:
            primeList.append(n)
    return primeList

def test():
    testeql(primes(1), [])
    testeql(primes(14), [2,3,5,7,11,13])
    testeql(primes(49), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])
    testeql(primes(73), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73])
    
