def isProbablePrime(n):
    if n == 2:
        return True
    if not n & 1:
        return False  # even numbers
    return pow(2, n-1, n) == 1

def isPrime(n):
    # brute force
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def test():
    testeql(isProbablePrime(2), True)
    testeql(isProbablePrime(17), True)
    testeql(isProbablePrime(35), False)

    # Carmichael Number
    testeql(isProbablePrime(561), True)  
    testeql(isProbablePrime(3 * 11 * 17), False)

    testeql(isPrime(17), True)
    testeql(isPrime(2), True)
    testeql(isPrime(8), False)
    testeql(isPrime(561), False)
