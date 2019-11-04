from collections import defaultdict

def singleNumber(nums):
    d = defaultdict(int)
    for n in nums:
        d[n] += 1
    for k in d:
        if d[k] == 1:
            return k

def test():
    testeql(singleNumber([2,2,1,3,3]), 1)
