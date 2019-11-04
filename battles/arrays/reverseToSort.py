desc = """Determine if it is possible to sort an array by reversing one of its contiguous subarrays.

It's guaranteed that array is not initially sorted.

array must be strictly increasing
"""

def isstrict(a):
    for i in range(1, len(a)):
        if a[i] - a[i-1] <= 0:
            return False
    return True

def reverseToSort(inputArray):
    st = sorted(inputArray)
    # try every subarray
    for start in range(len(inputArray)):
        for end in range(start+1, len(inputArray)+1):
            copy = inputArray[:]
            copy[start:end] = copy[start:end][::-1]
            # print(copy[start:end], copy[end-1:start:-1])
            # copy[start:end] = copy[end-1:start-1:-1]
            # print(start, end, copy)

            if st == copy and isstrict(copy):
                return True
    return False

test(
    reverseToSort([100, 99, 98]), True,
)
