def swapArrayHalves(inputArray):
    pr('inputArray')
    for i in range(len(inputArray) // 2):
        pr('i')
        pr('inputArray')
        tmp = inputArray[i]
        pr('tmp')
        inputArray[i] = inputArray[i + len(inputArray) // 2]
        inputArray[i + len(inputArray) // 2] = tmp
    return inputArray

def countWays(n, k):
    from math import factorial
    if n <= k:
        return 0
    return (factorial(n) // (factorial(n - k) * factorial(k))) % (10 ** 9 + 7)



def toAndFro(a, b, t):

    length = abs(b - a)
    t %= 2 * length
    if t <= length:
        return a + (b - a) / abs(b - a) * t
    else:
        t -= length
        return b + (a - b) / abs(b - a) * t


    

def test():
    testeql(swapArrayHalves([1,3,2,1]), [2,1,1,3])
    testeql(countWays(1000, 500), 159835829)
    testeql(toAndFro(10, 4, 8), 6)
