def binarySearch(arr, x):
    # returns the index of x in arr, or -1 if not found
    # arr must be sorted
    left = 0
    right = len(arr) - 1
    while True:
        if right < left:
            return -1

        midpoint = (left + right) // 2
        if arr[midpoint] < x:
            left = midpoint + 1
        elif arr[midpoint] > x:
            right = midpoint - 1
        else:
            return midpoint

def test():
    testeql(binarySearch([0,1,2,3], 1), 1)
    testeql(binarySearch([0,1,2,3,4], 2), 2)
    testeql(binarySearch([0,1,2], 5), -1)
    testeql(binarySearch([0,1,2], -3), -1)
    testeql(binarySearch([0,1,2], 2), 2)
    testeql(binarySearch([3,7,12,15,19,22,23], 22), 5)
