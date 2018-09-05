description = """

Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays. The subarray from which this sum comes must contain at least 1 element.

Example

For inputArray = [-2, 2, 5, -11, 6], the output should be
arrayMaxConsecutiveSum2(inputArray) = 7.

The contiguous subarray that gives the maximum possible sum is [2, 5], with a sum of 7.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer inputArray

    An array of integers.

    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 105,
    -1000 ≤ inputArray[i] ≤ 1000.

    [output] integer

    The maximum possible sum of a subarray within inputArray.

"""

def test():
    testeql(arrayMaxConsecutiveSum2([-2,2,5,-11,6]), 7)
    testeql(arrayMaxConsecutiveSum2([-2,2,5,-11,6,20]), 26)
    testeql(arrayMaxConsecutiveSum2([-2,2,5,-1,6,20]), 32)
    testeql(arrayMaxConsecutiveSum2([-2, 2, 5, -11, 6]), 7)
    testeql(arrayMaxConsecutiveSum2([-3, -2, -1, -4]), -1)
    testeql(arrayMaxConsecutiveSum2CaptainSolution([-3, -2, -1, -4]), -1)
    testeql(arrayMaxConsecutiveSum2CaptainSolution([-2, 2, 5, -11, 6]), 7)

    
def arrayMaxConsecutiveSum2(inputArray):
    # first attempt
    if all([m < 0 for m in inputArray]):
        return max(inputArray)
    maxSum = 0
    curSum = 0
    for n in inputArray:
        if n > 0:  # this check must be why the solution doesn't work for an array of all negative numbers
            curSum += n
            if curSum > maxSum:
                maxSum = curSum
        else:
            if curSum + n > 0:
                curSum += n
            else:
                curSum = 0
    return maxSum
            
def arrayMaxConsecutiveSum2CaptainSolution(inputArray):
    # solution by k_lee
    maxSum = float('-inf')
    curSum = 0
    for x in inputArray:
        curSum += x
        maxSum = max(maxSum, curSum)
        if curSum < 0:
            curSum = 0
    return maxSum
    
