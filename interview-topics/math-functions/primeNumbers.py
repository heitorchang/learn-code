def primesList(a, b):
    return list(filter(lambda x: all(x % i for i in range(2, int(x**0.5) + 1)), range(a, b+1)))
