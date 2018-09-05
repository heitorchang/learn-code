description = """
You are supposed to label a bunch of boxes with numbers from 0 to n, and all the labels are stored in the array arr. Unfortunately one of the labels is missing. Your task is to find it.

Example

For arr = [3, 1, 0], the output should be
missingNumber(arr) = 2.

Input/Output

[time limit] 4000ms (py3)
[input] array.integer arr

An unsorted array consisting of different integers from 0 to n inclusive, with only one of them missing.

Guaranteed constraints:
1 ≤ arr.length ≤ 1000,
0 ≤ arr[i] ≤ arr.length.

[output] integer

The missing number.
"""

def test():
    testeql(missingNumber([1,2]), 0)
    testeql(missingNumber([0]), 1)
    testeql(missingNumber([3,1,0]), 2)










    



def missingNumber(arr):
    s = set(arr)
    start = min(arr)
    end = len(arr)

    for i in range(0, end + 1):
        if i not in s:
            return i

