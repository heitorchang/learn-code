def isBoo(s):
    if len(s) == 0:
        return False
    if s[0] == 'u':
        return False
    try:
        uleftidx = s.index('u')
    except ValueError:
        return False

    try:
        urightidx = s.rindex('u') + 1
    except ValueError:
        return False

    for i in range(uleftidx, urightidx):
        if s[i] != 'u':
            return False
            
    leftos = s[:uleftidx]
    rightos = s[urightidx:]

    return leftos == rightos


def booAnalysis(s):
    lens = len(s)
    maxboo = 0
    for boo1left in range(lens+1):
        for boo1right in range(boo1left, lens+1):
            for boo2left in range(boo1right, lens+1):
                for boo2right in range(boo2left, lens+1):
                    boo1 = s[boo1left:boo1right]
                    boo2 = s[boo2left:boo2right]

                    if isBoo(boo1):
                        maxboo = max(maxboo, len(boo1))

                    if isBoo(boo2):
                        maxboo = max(maxboo, len(boo2))

                    if isBoo(boo1) and isBoo(boo2):
                        maxboo = max(maxboo, len(boo1) + len(boo2))
    return maxboo
                    
                    

"""
test(isBoo('ouo'), True,
     isBoo('ouuo'), True,
     isBoo('o'), False,
     isBoo('uo'), False,
     isBoo('oouo'), False)
"""

test(booAnalysis("ouuooouo"), 7)
