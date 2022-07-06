def selsort(alist):
    for i in range(len(alist) - 1):
        restmin = float('inf')
        minidx = 0
        for j in range(i, len(alist)):
            if alist[j] < restmin:
                restmin = alist[j]
                minidx = j
        print(i, restmin)
        alist[i], alist[minidx] = alist[minidx], alist[i]

def test_selsort():
    arr = [12,12,1,99,3,-1,-3,90,0,1020,3,1,2,5,-2]
    arrcopy = arr[:]
    selsort(arrcopy)
    print(arrcopy == sorted(arr))
    print(arrcopy, sorted(arr))
