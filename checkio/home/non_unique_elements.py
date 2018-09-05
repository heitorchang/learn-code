from collections import Counter

def getUniques(ctr):
    return [k for k, v in ctr.items() if v == 1]

def checkio(data):
    c = Counter(data)
    u = getUniques(c)
    return [elem for elem in data if elem not in u]

def test():
    testeql(checkio([1, 2, 3, 1, 3]), [1, 3, 1, 3])
    testeql(checkio([1, 2, 3, 4, 5]), [])
    testeql(checkio([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])
