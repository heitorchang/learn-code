def primes(size):
    sieve = [0] * (size+1)
    for i in range(2, int(size ** 0.5) + 1):  # remember + 1
        if not sieve[i]:
            for j in range(i * 2, size+1, i):
                sieve[j] = 1
    print(sieve)
    primes = []
    for i in range(2, size+1):
        if not sieve[i]:
            primes.append(i)
    return primes
