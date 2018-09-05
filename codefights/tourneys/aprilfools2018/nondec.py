def isNondec(a):
    cur = a[0]
    for val in a[1:]:
        if val < cur:
            return False
        cur = val
    return True

def checkArray(a):
    if len(a) < 2:
        return True
    absdiff = []
    seenPos = False
    seenNeg = False
    aabs = map(abs, a)
    cur = next(aabs)
    for v in aabs:
        print(v - cur)
        if (v - cur) > 0:
            seenPos = True
        if seenPos and (v - cur) < 0:
            return False
        cur = v
    return True

def test():
    # asst(checkArray([1,2,-10]), True)
    # asst(checkArray([1,3,1]), False)
    testeql(checkArray([1,2,-10]), True)
    testeql(checkArray([1,3,1]), False)
    testeql(checkArray([11,10,2,3]), True)
    testeql(checkArray([-20]), True)
    testeql(checkArray([10, 18, 18, 22, 12, 13]), False)
