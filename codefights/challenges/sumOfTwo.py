def sumOfTwo_Alex(a, b, v):
    a = sorted(set(a))
    b = sorted(set(b))

    i = 0
    j = len(b) - 1

    while i <= len(a) - 1 and j >= 0:
        cur_sum = a[i] + b[j]
        if cur_sum == v:
            return True
        if cur_sum < v:
            i += 1
        else:
            j -= 1
    return False

scenario = """
 1  2  3
10 20 30 40
"""

def sumOfTwo_set(a, b, v):
    a = set(a)
    b = set(b)

    for n in a:
        if v - n in b:
            return True
    return False
    
def test():
    testeql(sumOfTwo_set([1,2,3], [10,20,30,40], 42), True)
    testeql(sumOfTwo_set([10,20,30,40], [1,2,3], 42), True)
