def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

def test():
    testeql(bubbleSort([1,2,3]), [1,2,3])
    testeql(bubbleSort([3,2,1]), [1,2,3])
    testeql(bubbleSort([3,1,2]), [1,2,3])
    testeql(bubbleSort([6, 1, 7, 5, 3, 8, 4, 2, 0, 9]), list(range(10)))
