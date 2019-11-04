description = """
Given a positive integer n, calculate the sum of all the prime numbers from 1 to n, inclusive. Because this number may be very big, return it modulo 109 + 7 in your output.

Example

    For n = 6, the output should be
    primesSum2(n) = 10.

    The sum of the prime numbers from 1 to 6, inclusive, (2 + 3 + 5) is 10.

    For n = 11, the output should be
    primesSum2(n) = 28.

    The sum of the prime numbers from 1 to 11, inclusive, (2 + 3 + 5 + 7 + 11) is 28.

Input/Output

    [time limit] 4000ms (py3)

    [input] integer n

    Guaranteed constraints:
    1 ≤ n ≤ 105.

    [output] integer

    The sum of all the prime numbers from 1 to n, inclusive, modulo 109 + 7.


"""

def test():
    testeql(primesSum2(6), 10)
    testeql(primesSum2(28938), 42877601)
    
    testeql(eratosthenesSieveBool(9), [2,3,5,7])
    testeql(eratosthenesSieveBool(12), [2,3,5,7,11])
    testeql(eratosthenesSieveBool(7), [2,3,5,7])
    testeql(eratosthenesSieveBool(25), [2,3,5,7,11,13,17,19,23])

    
def eratosthenesSieve(n):
    # SET version is way faster
    if n < 2:
        return []
    out = list(range(2, n+1))
    index = 0
    prime = out[index]
    while prime <= int(n ** 0.5):
        for step in range(prime * 2, n+1, prime):
            try:
                out.remove(step)
            except ValueError:
                pass
        index += 1
        prime = out[index]
    return out

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

def eratosthenesSieveBool(n):
    sieve = [True] * (n+1)
    for j in range(4, n+1, 2):
        sieve[j] = False

    for c in range(3, int(n ** 0.5) + 1, 2):
        for j in range(2*c, n+1, c):
            sieve[j] = False
    out = []
    for i in range(2, n+1):
        if sieve[i]:
            out.append(i)
    return out

def primesSum2(n):
    primes = eratosthenesSieveBool(n)
    return sum(primes) % (10 ** 9 + 7)
