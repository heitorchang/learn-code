description = """
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
Input/Output

[time limit] 4000ms (py3)
[input] array.integer inputArray

Array of positive integers.

Guaranteed constraints:
3 ≤ inputArray.length ≤ 105,
1 ≤ inputArray[i] ≤ 1000.

[input] integer k

An integer (not greater than the length of inputArray).

Guaranteed constraints:
1 ≤ k ≤ inputArray.length.

[output] integer

The maximal possible sum.
"""

def arrayMaxConsecutiveSumTLE(inputArray, k):
    s = sum(inputArray[0:k])
    maxSum = s
    for i in range(1, len(inputArray)-k+1):
        tmpSum = sum(inputArray[i:i+k])
        if tmpSum > maxSum:
            maxSum = tmpSum
    return maxSum

def arrayMaxConsecutiveSum(inputArray, k):
    s = sum(inputArray[0:k])
    maxSum = s
    for i in range(k, len(inputArray)):
        s += inputArray[i]
        s -= inputArray[i-k]
        if s > maxSum:
            maxSum = s
    return maxSum

def test():
    testeql(arrayMaxConsecutiveSum([2,3,5,1,6], 2), 8)
