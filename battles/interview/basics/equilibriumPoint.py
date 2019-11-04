description = """
Equilibrium position in an array is a position at which the sum of elements before it is equal to the sum of elements after it. Given an array arr, your task is to determine at which position equilibrium first occurs in the array. If there is no equilibrium position, the answer should be -1.

Example

    For arr = [5], the output should be

    equilibriumPoint(arr) = 1.

    Explanation: Since this array only has one element, the equilibrium point is at position 1.

    For arr = [10, 5, 3, 5, 2, 2, 6, 8], the output should be

    equilibriumPoint(arr) = 4.

    Explanation: The equilibrium point is at position 4, because the sum of elements before it - (10 + 5 + 3) - is equal to the sum of elements after it - (2 + 2 + 6 + 8).

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer arr

    Guaranteed constraints:

    1 ≤ arr.length ≤ 105,

    -1000 ≤ arr[i] ≤ 1000.

    [output] integer

    The first equilibrium position in arr, or -1.

"""

def test():
    #testeql(equilibriumPoint([2, 3, -5, 100]), 4)
    #testeql(equilibriumPoint([5]), 1)
    #testeql(equilibriumPoint([10, 5, 3, 5, 2, 2, 6, 8]), 4)
    #testeql(equilibriumPoint([2, 3, -5, 100]), 4)
    testeql(equilibriumPoint([1, 3, 5, 2, 3]), -1)




    
def equilibriumPointTLE(arr):
    # time limit exceeded
    # The reason is that the temporary sums are recomputed at every
    # step, leading to a very inefficient process
    eqPtZeroBased = 0
    while eqPtZeroBased < len(arr):
        if sum(arr[:eqPtZeroBased]) == sum(arr[eqPtZeroBased+1:]):
            return eqPtZeroBased + 1
        eqPtZeroBased += 1
    return -1

def equilibriumPoint(arr):
    eqPtZeroBased = 0
    leftSum = 0
    rightSum = sum(arr) - arr[eqPtZeroBased]

    while eqPtZeroBased < len(arr):
        if leftSum == rightSum:
            return eqPtZeroBased + 1
        elif eqPtZeroBased == len(arr) - 1:
            return -1
        else:
            eqPtZeroBased += 1
            leftSum += arr[eqPtZeroBased-1]
            rightSum -= arr[eqPtZeroBased]
    return -1
    
