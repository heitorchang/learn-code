def primesSumTimeOut(a,b):
    # sieve
    # http://stackoverflow.com/questions/10639861/python-prime-generator-in-one-line
    primes = list(filter(lambda n: n >= a, reduce((lambda r, x: r - set(range(x**2, b, x)) if (x in r) else r), range(2, b), set(range(2, b)))))
    pr('primes')
    return sum(primes)

def primesSum(a, b):
    return sum(filter(lambda n: n >= a, reduce((lambda r, x: (r.difference_update(range(x*x, b+1, 2*x)) or r) if (x in r) else r), range(3, int((b+2)**0.5+1), 2), set([2] + list(range(3, b+1, 2))))))

def primesSum_yasutaka_o(a, b):
    return sum(filter(lambda x: all(x % i for i in range(2, int(x**0.5) + 1)), range(max(2, a), b+1)))

def primesSum_yasutaka_o_decomposed(a, b):
    f = list(filter(lambda x: all(x % i for i in range(2, int(x**0.5) + 1)), range(max(2, a), b+1)))
    pr('f')

def test():
    testeql(primesSum(10, 20), 60)
    testeql(primesSum_yasutaka_o(10, 20), 60)

    testeql(primesSum_yasutaka_o_decomposed(10, 20), None)
