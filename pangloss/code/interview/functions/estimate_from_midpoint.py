def goodEnough(estimate, target):
    tolerance = 1e-4
    return abs(target - estimate) <= tolerance

def sqrtEstimateSICPIter(estimate, target):
    if goodEnough(estimate * estimate, target):
        return estimate
    return sqrtEstimateSICPIter((estimate + (target / estimate)) / 2, target)
    
def sqrtEstimateSICP(n):
    return sqrtEstimateSICPIter(1, n)

def sqrtEstimateMidpoint(x):
    left = 0
    right = x
    
    while True:
        midpoint = (right + left) / 2
        squareMidpoint = midpoint * midpoint

        if abs(squareMidpoint - x) < 1e-4:
            return midpoint
            
        if squareMidpoint > x:
            right = midpoint
        else:
            left = midpoint

def test():
    testeql(round(sqrtEstimateSICP(9), 3), 3)
    testeql(round(sqrtEstimateSICP(2), 3), 1.414)

    testeql(round(sqrtEstimateMidpoint(9), 3), 3)
    testeql(round(sqrtEstimateMidpoint(2), 3), 1.414)
