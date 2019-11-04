def dfsComponentSize(matrix, vertex):
    p = matrix[vertex]
    return sum(p) + 1

def twoArraysNthElement(array1, array2, n):
    def lowerBound(array, elem):
        l = -1
        r = len(array)
        while l + 1 < r:
            mid = (l + r) // 2
            if array[mid] > elem:
                r = mid - 1
            else:
                l = mid
        return l

    l = -1
    r = len(array1)

    while l + 1 < r:
        mid = (l + r) // 2
        pos = lowerBound(array2, array1[mid])

        if mid + pos + 1 <= n:
            l = mid
        else:
            r = mid

    if l > -1 and l + lowerBound(array2, array1[l]) + 1 == n:
        return array1[l]
    return twoArraysNthElement(array2, array1, n)

    
def test():
    testeql(twoArraysNthElement([1, 3, 4], [2, 6, 8], 5), 8)
    testeql(twoArraysNthElement([1,2,3], [4,5,6], 3), 4)
