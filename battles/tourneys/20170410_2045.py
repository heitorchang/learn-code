def isCaseInsensitivePalindrome(inputString):
    s = inputString.lower()
    sr = s[::-1]
    return s == sr


def quickSort(a, l, r):

    if l >= r:
        return a

    x = a[l]
    i = l
    j = r

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            t = a[i]
            a[i] = a[j]
            a[j] = t
            i += 1
            j -= 1

    quickSort(a, l, j)
    quickSort(a, i, r)

    return a

def divisorsSuperset(superset, n):

    def isInSequence(sequence, elem):
        for i in range(len(sequence)):
            if (sequence[i] == elem):
                return True
        return False

    res = 0

    for i in range(1, n + 1):
        correct = True
        j = 2
        while j * j <= i:
            if ... :
                if not isInSequence(superset, j) or not isInSequence(superset, i / j):
                    correct = False
                    break
            j += 1
        if correct:
            res += 1

    return res

def test():
    testeql(quickSort([5, 2, 1, 7, 5, 3, 2, 3], 0, 3), [1, 2, 5, 7, 5, 3, 2, 3])
    testeql(divisorsSuperset([3,2], 13), 10)
