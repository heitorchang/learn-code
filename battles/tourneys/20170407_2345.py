def test():
    testeql(arrayMaximalAdjacentDifference([2,4,1,0]), 3)
    
def arrayMaximalAdjacentDifference(inputArray):
    lst = [abs(b - a) for (a, b) in zip(inputArray, inputArray[1:])]
    return max(lst)
        
def fractionSubtraction(a, b):

    C = [a[0] * b[1] - a[1] * b[0], a[1] * b[1]]
    gcd = gcdEuclid(C[0], C[1])

    C[0] /= gcd
    C[1] /= gcd

    return C

def gcdEuclid(a, b):
    if a == 0:
        return b
    return gcdEuclid(b % a, a)
