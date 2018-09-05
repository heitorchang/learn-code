def removeFirst(n):
    return n[1:]

def removeLast(n):
    return n[:-1]

def removeDigitsPhail(n, k):
    # DOES NOT PASS
    n = str(n)
    minn = n
    maxx = 0
    tmp = n
    # find max
    while len(str(n)) > k:
        if int(removeFirst(n)) > int(removeLast(n)):
            n = removeFirst(n)
            maxx = n
        else:
            n = removeLast(n)
            maxx = n
    n = tmp
    while len(str(n)) > k:
        if int(removeFirst(n)) > int(removeLast(n)):
            n = removeLast(n)
            minn = n
        else:
            n = removeFirst(n)
            minn = n
    return [int(minn), int(maxx)]
            

def removeDigits(n, k):
    s = str(n)
    maxx = 0
    minn = n
    for i in range(len(s) - k + 1):
        window = int(s[i:i+k])
        if window > maxx:
            maxx = window
        if window < minn:
            minn = window
    return [minn, maxx]
    

def test():
    testeql(removeDigits(15243, 2), [15,52])
    testeql(removeDigits(10391938, 4), [391, 9193])
