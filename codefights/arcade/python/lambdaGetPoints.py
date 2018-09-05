def getPoints(answers, p):
    questionPoints = lambda i, ans: i + 1 if ans else -p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res

def test():
    testeql(getPoints([True, True, False, True], 2), 5)
