def coolPairs(a, b):
    uniqueSums = {i + j for i in a for j in b if (i * j) % (i + j) == 0}
    pr('uniqueSums')
    return len(uniqueSums)

def test():
    testeql(coolPairs([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]), 4)
