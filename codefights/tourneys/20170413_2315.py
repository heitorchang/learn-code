def sumDigits(t):
    t = t.replace(".", "")
    return sum(map(int, t))

def sumClock(pair):
    total = 0
    return sumDigits(pair[0]) + sumDigits(pair[1])

def timeDiff(t, d):
    m, s = map(int, t.split("."))
    s -= d
    if s < 0:
        m -= 1
        s += 60
    return "{}.{:02d}".format(m, s)

def chessClockSumOfDigits(initialTime, k):
    # some int error
    minTime1 = 9999
    maxTime1 = 0
    minTime2 = 9999
    maxTime2 = 0
    t1 = initialTime[0]
    t2 = initialTime[1]
    for s in range(k+1):        
        t1d = s
        t2d = k - s
        newT1 = timeDiff(t1, t1d)
        newT2 = timeDiff(t2, t2d)
        curSum1 = sumDigits(newT1)

        if curSum1 > maxTime1:
            maxTime1 = curSum1
        if curSum1 < minTime1:
            minTime1 = curSum1
        for t in range(k+1-s):
            t2d = t
            newT2 = timeDiff(t2, t2d)
            curSum2 = sumDigits(newT2)

            if curSum2 > maxTime2:
                maxTime2 = curSum2
            if curSum2 < minTime2:
                minTime2 = curSum2

    return [minTime1 + minTime2, maxTime1 + maxTime2]
        


def test():
    testeql(chessClockSumOfDigits(["3.05", "9.02"], 9), [12, 38])
    # testeql(sumDigits("1.02"), 3)
    # testeql(timeDiff("3.00", 1), "2.59")
