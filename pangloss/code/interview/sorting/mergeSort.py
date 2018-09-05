def mergeSort(arr):
    n = len(arr)
    if n > 1:
        middle = n // 2
        left = arr[:middle]
        right = arr[middle:]

        mergeSort(left)
        mergeSort(right)

        # merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def test():
    testeql(mergeSort([1,2,3]), [1,2,3])
    testeql(mergeSort([3,2,1]), [1,2,3])
    testeql(mergeSort([3,1,2]), [1,2,3])
    testeql(mergeSort([6, 1, 7, 5, 3, 8, 4, 2, 0, 9]), list(range(10)))
