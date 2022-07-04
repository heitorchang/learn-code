def isprime(n):
    nlimit = 21111
    if n >= nlimit:
        return "unknown. too large."
    sieve = {i: True for i in range(2, nlimit + 1)}
    for i in range(2, nlimit + 1):
        if sieve[i]:
            for j in range(2, nlimit // i + 1):
                sieve[i * j] = False
    return sieve[n]
