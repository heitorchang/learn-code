def kthDivisor(n, k):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    print(divisors)
    try:
        return(divisors[k-1])
    except:
        return -1



def test():
    testeql(kthDivisor(63,4), 9)
    testeql(kthDivisor(16,5), 16)
