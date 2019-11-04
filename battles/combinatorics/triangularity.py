from itertools import combinations
def triangularity(segmentsLength):
    a = sorted(segmentsLength)
    pr('a')
    for c in combinations(a, 3):
        pr('c')
        if (c[0] + c[1]) > c[2]:
            return True
    return False

def test():
    testeql(triangularity([1,2,3,4]), True)
