from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    print(list(enumerate(res)))
    deque(map(lambda x: x[1].rotate(-x[0]), enumerate(res)), 0)
    print([list(d) for d in res])
    return [list(d) for d in res]

def test():
    testeql(doodledPassword([1, 2, 3, 4, 5]), [[1,2,3,4,5], 
 [2,3,4,5,1], 
 [3,4,5,1,2], 
 [4,5,1,2,3], 
 [5,1,2,3,4]])
