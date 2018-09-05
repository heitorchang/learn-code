from fractions import gcd

def maximumGcdAndSum(A, B):
    # brute force, times out a lot
    # passed 6 tests, score 3.26
    maxGCD = 0
    maxSum = 0
    for a in A:
        for b in B:
            g = gcd(a, b)
            if g > maxGCD:
                maxSum = a + b
                maxGCD = g
            elif g == maxGCD:
                s = a + b
                if s > maxSum:
                    maxSum = s
    return maxSum

def test():
    testeql(maximumGcdAndSum([3,1,4,2,8], [5,2,12,8,3]), 16)
    
