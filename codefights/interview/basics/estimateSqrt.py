# like SICP exercise

"""
Given n, estimate sqrt(n) to 5 decimal places
"""

def goodEnough(estimate, n):
    eps = 1e-6
    if abs((estimate * estimate) - n) <= eps:
        return True
    return False

def estimateSqrtIterate(n, bounds, guess):  #, counter):
    # if counter > 22:
    #     return 0
    # pr('bounds guess')
    if goodEnough(guess, n):
        return guess
    else:
        guessSquared = guess * guess
        if guessSquared > n:
            return estimateSqrtIterate(n, [bounds[0], guess], (guess + bounds[0]) / 2)  # , counter+1)
        else:
            return estimateSqrtIterate(n, [guess, bounds[1]], (guess + bounds[1]) / 2)  # , counter+1)
        
def estimateSqrt(n):
    return round(estimateSqrtIterate(n, [0, n], 0), 5)  #, 0), 5)


# SICP Solution

def average(x, y):
    return (x + y) / 2
    
def improve(guess, x):
    return average(guess, x / guess)

def sqrtIter(guess, x):
    pr('guess')
    if goodEnough(guess, x):
        return guess
    return sqrtIter(improve(guess, x), x)

def sicpSqrt(n):
    return round(sqrtIter(1, n), 5)
    
def test():
    testeql(estimateSqrt(2), 1.41421)
    testeql(estimateSqrt(9), 3.0000)
    testeql(estimateSqrt(16), 4.0000)
    
    # testeql(sicpSqrt(2), 1.41421)
    # testeql(sicpSqrt(9), 3.00000)
