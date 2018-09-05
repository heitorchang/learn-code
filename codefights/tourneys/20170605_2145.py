
def electionsWinners(votes, k):
    v = sorted(votes, reverse=True)
    t = 0
    for i in range(1, len(v)):
        if k + v[i] > v[0]:
            t += 1
    return t + 1

def pagesNumbering(n):
    tot = 0
    for i in range(1,n+1):
        tot += len(str(i))
    return tot


def test():
    # testeql(electionsWinners([2,3,5,2], 3), 2)
