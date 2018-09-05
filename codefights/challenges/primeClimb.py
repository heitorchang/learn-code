from collections import Counter

def eratoSieveLst(n):
    out = list(range(2, n+1))
    ct = 0
    while out[ct] <= int(n ** 0.5):
        p = out[ct]
        for step in range(2*p, n+1, p):
            try:
                out.remove(step)
            except ValueError:
                pass
        ct += 1
    return out

def eratoSieveSet(n):
    s = set(range(2, n+1))
    primes = set()
    
    nextBase = min(s)

    limit = int(n ** 0.5)

    while nextBase <= limit:
        primes.add(nextBase)
        for step in range(2*nextBase, n+1, nextBase):
            s.discard(step)
        s.discard(nextBase)
        nextBase = min(s)
    return sorted(primes | s)

def trimPrimes(lst, limit):
    return [e for e in lst if e <= limit]
    
def isPrime(n):
    # idea from challenge sumDivisors, Mgcmarco solution
    # Fermat primality test
    return pow(2, n-1, n) == 1

def primeClimb(n):
    if isPrime(n):
        return str(n)
    factors = []
    while n > 1:
        # check if divisible by 2
        if n % 2 == 0:
            factors.append(2)
            n //= 2
            continue
        for f in range(3, n+1, 2):
            if n % f == 0:
                factors.append(f)
                n //= f
                break
    ctr = Counter(factors)
    fk = sorted(ctr.keys())
    result = ""
    for k in fk:
        if ctr[k] > 1:
            result += str(k) + str(ctr[k])
        else:
            result += str(k)
    return result
                

def primeClimbTLE(n):
    # time limit exceeded
    primes = eratoSieveSet(n)
    factors = []
    while n > 1:
        for f in primes:
            if n % f == 0:
                factors.append(f)
                break
        n //= f
        trimPrimes(primes, n)
    ctr = Counter(factors)
    fk = sorted(ctr.keys())
    result = ""
    for k in fk:
        if ctr[k] > 1:
            result += str(k) + str(ctr[k])
        else:
            result += str(k)
    return result
    

def test():
    # testeql(eratoSieveSet(9), [2,3,5,7])
    # testeql(eratoSieveSet(11), [2,3,5,7,11])
    # testeql(eratoSieveSet(8), [2,3,5,7])

    testeql(primeClimb(60), "2235")
    testeql(primeClimb(12319), "97127")
    testeql(primeClimb(4782969), "314")
