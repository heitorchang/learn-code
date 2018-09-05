description = """
In an array, arr, the elements at indices i and j (where i < j) form an inversion if arr[i] > arr[j]. In other words, inverted elements are considered to be "out of order". To correct an inversion, we can swap adjacent elements.
"""

from random import shuffle
from collections import deque
from itertools import islice

def countInversionsTimeout(a):
    inversions = 0

    def merge(a, b):
        nonlocal inversions
        result = deque()
    
        while True:
            if a:
                i = a[0]
            else:
                return result + b
            
            if b:
                j = b[0]
            else:
                return result + a

            if i <= j:
                result.append(a.popleft())
            else:
                inversions += 1
                result.append(b.popleft())
            

    def mergesort(a):
        a = deque(a)
        # print("mergesorting", a)
        n = len(a)
        if n == 1:
            return a
        midpt = n // 2
        left = mergesort(islice(a, 0, midpt))
        right = mergesort(islice(a, midpt, n))
        return merge(left, right)

    result = mergesort(a)
    print(result)
    
    return inversions


hackerrank = """
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
"""

def countInversions(arr):
    """Gave up, this is the HackerRank editorial solution"""
    n = len(arr)
    if n == 1:
        return 0
    n1 = n // 2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = countInversions(arr1) + countInversions(arr2)
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 < n1 and (i2 >= n2 or arr1[i1] <= arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans

def test():
    # testeql(merge(deque([1,2]), deque([-2,3])), (deque([-2,1,2,3]), 1))
    testeql(countInversions([2,1,3,1,2]), 4)
    testeql(countInversions([1,1,1,2,2]), 0)
    

