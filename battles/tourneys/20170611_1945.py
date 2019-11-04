def greatestCommonPrimeDivisor(a, b):

    gcd = -1
    divisor = 2
    while a > 1 and b > 1:
        if a % divisor == 0 and b % divisor == 0:
            gcd = divisor
        while a % divisor == 0:
            a /= divisor
        while b % divisor == 0:
            b /=  divisor 
        divisor += 1
    return gcd

def differentValuesInMultiplicationTable(n, m):
    result = 0
    for value in range(n * m + 1):
        for i in range(1, min(n, m) + 1):
            if value % i == 0 and value / i <= max(n, m):
                result += 1
                break
    return result - 1


def test():
    testeql(differentValuesInMultiplicationTable(3,2), 5
