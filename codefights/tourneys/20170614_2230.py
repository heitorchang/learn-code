
def computeDefiniteIntegral(l, r, p):
    # does not pass all
    p = p + [0]
    intg = [0 for _ in range(len(p)+1)]
    for i in range(0, len(p)):
        # pr('p[i]')
        if p[i] != 0:
            pr('i p[i]')
            intg[i+1] = (1/(i+1)) * p[i] + p[i+1]
    pr('intg')
    leftsum = 0
    rightsum = 0
    for i in range(1, len(intg)):
        leftsum += intg[i] * (l) ** i
        rightsum += intg[i] * (r) ** i
    return rightsum - leftsum



def test():
    testeql(computeDefiniteIntegral(-1, 2, [0,0,0,1]), 3.75)
    testeql(computeDefiniteIntegral(1, 3, [1, 0, 0, 4]), 82)
