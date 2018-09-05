def insertionSort(arr):
    # begin at the second element
    for j in range(1, len(arr)):
        key = arr[j]
        # insert A[j] into the sorted sequence arr[0:j]
        pr('arr[0:j] key')
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
        pr('arr')
    return arr

def test():
    testeql(insertionSort([1,2,3]), [1,2,3])
    testeql(insertionSort([3,2,1]), [1,2,3])
    testeql(insertionSort([2,1,3]), [1,2,3])
    testeql(insertionSort([5,1,4,3,2]), [1,2,3,4,5])
