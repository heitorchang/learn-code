# from an interview practice problem, I concluded that using
# a set to generate primes is much faster than using a list

def eratosthenesSieveSet(n):
    if n < 2:
        return []
    out = set(range(2, n+1))
    for step in range(4, n+1, 2):
        out.discard(step)

    for base in range(3, int(n ** 0.5)+1, 2):
        for step in range(base * 2, n+1, base):
            out.discard(step)
    return sorted(out)

# A boolean array is even better

def eratosthenesSieveBoolFirstVersion(n):
    sieve = [True] * (n+1)
    
    for j in range(4, n+1, 2):
        sieve[j] = False

    for c in range(3, int(n ** 0.5) + 1, 2):
        for j in range(3*c, n+1, 2*c):
            sieve[j] = False
    out = []
    for i in range(2, n+1):
        if sieve[i]:
            out.append(i)
    return out

def eratosthenesSieveBool(n):
    # a list of prime numbers up to n
    # 2 is the only even element
    sieve = [True] * (n+1)
    
    # consider odd numbers up to sqrt(n), add 1 to range's end
    for odd in range(3, int(n ** 0.5) + 1, 2):
        # eliminate multiples.
        # we already decided to ignore 2*n 
        for step in range(3*odd, n+1, 2*odd):
            sieve[step] = False
            
    # build up result
    out = [2]
    for i in range(3, n+1, 2):
        if sieve[i]:
            out.append(i)
    return out
    
def test():
    testeql(eratosthenesSieveSet(29), [2,3,5,7,11,13,17,19,23,29])

    testeql(eratosthenesSieveBool(9), [2,3,5,7])
    testeql(eratosthenesSieveBool(29), [2,3,5,7,11,13,17,19,23,29])
    testeql(eratosthenesSieveBool(73), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73])
    testeql(eratosthenesSieveBool(49), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])
    testeql(eratosthenesSieveBool(199), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])
