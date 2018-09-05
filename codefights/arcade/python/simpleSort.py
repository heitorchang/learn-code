def simpleSort(arr):
    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                pr('arr[j] arr[j+1]')
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr

def test():
    testeql(simpleSort([2,4,1,5]), [1,2,4,5])
