# selection sort

def selsort(alist):
    """pick smallest item from each run and place it in position i"""
    for i in range(len(alist) - 1):
        minval = alist[i]
        minpos = i
        for j in range(i, len(alist)):
            if alist[j] < minval:
                minval = alist[j]
                minpos = j
        alist[i], alist[minpos] = alist[minpos], alist[i]
    print(alist)
    return alist


def merge(a, b):
    merged = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))

    if a:
        merged += a

    if b:
        merged += b
    return merged


def mergesort(alist):
    """divide list and merge the two halves"""
    if len(alist) > 1:
        midpt = len(alist) // 2
        return merge(mergesort(alist[:midpt]), mergesort(alist[midpt:]))
    return alist


def test_sort(fn):
    ainput = [34,1,4,1,2,3,2983,1,3,24,1,3,-192,3,-2,319,0,0,0,0]
    return fn(ainput) == sorted(ainput)
