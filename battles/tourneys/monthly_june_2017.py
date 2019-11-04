def isArrayDense(a):
    minArr = min(a)
    maxArr = max(a)
    setArr = set(a)
    if len(setArr) != len(a):
        return False
    return setArr == set(range(minArr, maxArr+1))

def decodeRLE(code):
    p = re.compile('[a-z]')
    s = p.split(code)
    tot = 0
    for num in s:
        if num != '':
            tot += int(num)
    return tot


def swapInPermutation(p):
    lenP = len(p)
    if lenP == 1:
        return p[0] % 2 == 0
    evensInRightPlace = 0
    oddsInRightPlace = 0
    for i, n in enumerate(p):
        if i % 2 == 0:
            if n % 2 == 0:
                evensInRightPlace += 1
        else:
            if n % 2 == 1:
                oddsInRightPlace += 1

    if lenP % 2 == 0:
        if evensInRightPlace == oddsInRightPlace == lenP // 2:
            return True
        if evensInRightPlace == oddsInRightPlace == (lenP // 2) - 1:
            return True
    else:
        if evensInRightPlace == (lenP // 2) + 1 and oddsInRightPlace == (lenP // 2):
            return True
        if evensInRightPlace == (lenP // 2) and oddsInRightPlace == (lenP // 2) - 1:
            return True
    return False
    

def splitPresentCost(l, r, s):
    end = min(s - l, r)
    start = max(s - r, l)
    pr('start end')
    return max(end - start + 1, 0)

def matchChars(base, s):
    baseCursor = 0
    out = []
    lenBase = len(base)
    increased = False
    # out = 0
    for sCursor in range(len(s)):
        if s[sCursor] == base[baseCursor]:
            if s[sCursor] == 1:
                if not increased:
                    increased = True
                out.append(s[sCursor])
            else:
                if not increased:
                    out.append(s[sCursor])
            # out += 1
            baseCursor += 1
            if baseCursor == lenBase:
                break
    return out

def binaryLCIS(a, b):
    maxLen = 0
    for baseStart in range(len(a)):
        curLen = len(matchChars(a[baseStart:], b))
        if curLen > maxLen:
            maxLen = curLen
    return maxLen

def test():
    # testeql(decodeRLE("a239b1"), 240)
    # testeql(swapInPermutation([2,4,6,5,1,3]), True)
    # testeql(splitPresentCost(7,18,28), 9)
    # testeql(splitPresentCost(2,4,5), 2)
    # testeql(splitPresentCost(1,3,7), 0)
    # testeql(splitPresentCost(1,1,1), 0)
    testeql(matchChars([0,1,1,0,1], [1,1,0,0,1,1]), [0,1,1])
    testeql(binaryLCIS([0, 1, 1, 0, 1], [1,1,0,0,1,1]), 3)
    testeql(matchChars([1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]), [1,1,1,1,1,1,1])
