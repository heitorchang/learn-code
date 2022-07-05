def qsort(alist):
    qsort_helper(alist, 0, len(alist) - 1)


def qsort_helper(alist, first, last):
    if first < last:
        split = partition(alist, first, last)
        qsort_helper(alist, first, split - 1)
        qsort_helper(alist, split + 1, last)


def partition(alist, first, last):
    pivot = alist[first]
    left = first + 1
    right = last
    done = False

    while not done:
        while left <= right and alist[left] <= pivot:
            left += 1
        while left <= right and alist[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]
    alist[first], alist[right] = alist[right], alist[first]

    return right


def test_sort():
    ainput = [34,1,4,1,2,3,2983,1,3,24,1,3,-192,3,-2,319,0,0,0,0]
    qsort(ainput)
    return ainput == sorted(ainput)
