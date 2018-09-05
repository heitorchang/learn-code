def ipow(a,b,n):
    #calculates (a**b)%n via binary exponentiation, yielding itermediate
    #results as Rabin-Miller requires
    A = a = long(a%n)
    yield A
    t = 1
    while t <= b:
        t <<= 1
    
    #t = 2**k, and t > b
    t >>= 2
    
    while t:
        A = (A * A)%n
        if t & b:
            A = (A * a) % n
        yield A
        t >>= 1

def RabinMillerWitness(test, possible):
    #Using Rabin-Miller witness test, will return True if possible is
    #definitely not prime (composite), False if it may be prime.
    
    return 1 not in ipow(test, possible-1, possible)

smallprimes = (3,5,7,11,13,17,19,23,29,31,37,41,43,
               47,53,59,61,67,71,73,79,83,89,97)
