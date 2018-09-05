def countSumOfTwoRepresentations3Phail(n, l, r):
    # partial
    tot = 0
    for a in range(l, r+1):
        # a + b = n
        if a <= (n - a) <= r:
            tot += 1
    return tot

def countSumOfTwoRepresentations3AlsoPhail(n, l, r):
    # phail
    rt = n - l
    nums = rt - l + 1
    if nums % 2 == 0:
        return nums // 2
    else:
        return nums // 2 + 1

def test():
    testeql(countSumOfTwoRepresentations3(6,2,4), 2)
