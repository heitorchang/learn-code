
def leastFactorial(n):
    k = 1
    counter = 2
    while k < n:
        k *= counter
        counter += 1
    return k
    
def test():
    testeql(
