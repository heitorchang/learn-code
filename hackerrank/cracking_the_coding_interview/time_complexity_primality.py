def fermat(n):
    # NOTE: 1 (one) is not prime!
    if n == 1:
        return False
    if n == 2:  # exceptional case
        return True
    return pow(2, n-1, n) == 1

def exhaustive(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def test():
    testeql(exhaustive(49), False)
    testeql(exhaustive(47), True)
