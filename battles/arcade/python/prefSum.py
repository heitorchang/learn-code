from itertools import accumulate

def prefSumTLE(a):
    # time limit exceeded
    return [sum(a[:i+1]) for i in range(len(a))]

def prefSum(a):
    return list(accumulate(a))

def test():
    testeql(prefSum([1,2,3]), [1,3,6])
