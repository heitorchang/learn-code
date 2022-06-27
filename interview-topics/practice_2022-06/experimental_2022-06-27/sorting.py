def bubblesort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


def insertionsort(alist):
    # left portion of list is sorted list,
    # start with the first item "sorted"
    for i in range(1, len(alist)):
        item_to_insert = alist[i]
        position = i
        while position > 0 and alist[position-1] > item_to_insert:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = item_to_insert
    print(alist)
    return alist


def mergesort(alist):
    print("called mergesort on", alist)
    if len(alist) > 1:
        midpt = len(alist) // 2
        left = alist[:midpt]
        right = alist[midpt:]

        mergesort(left)
        mergesort(right)

        # merge
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

    print(alist)
    return alist

def test_sort(fn):
    ainput = [34,1,4,1,2,3,2983,1,3,24,1,3,-192,3,-2,319,0,0,0,0]
    return fn(ainput) == sorted(ainput)
