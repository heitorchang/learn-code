def quicksort(arr):
    def partition(left, right):
        i = left - 1
        for j in range(left, right):
            if arr[j] <= arr[right]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i + 1

    def quicksortHelper(left, right):
        if left < right:
            middle = partition(left, right)
            quicksortHelper(left, middle - 1)
            quicksortHelper(middle + 1, right)

    quicksortHelper(0, len(arr) - 1)
    return arr

def test():
    testeql(quicksort([1,2,3]), [1,2,3])
    testeql(quicksort([3,2,1]), [1,2,3])
    testeql(quicksort([3,1,2]), [1,2,3])
    testeql(quicksort([6, 1, 7, 5, 3, 8, 4, 2, 0, 9]), list(range(10)))
