description = """
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

Example

    For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
    containsCloseNums(nums, k) = true.

    There are two 2s in nums, and the absolute difference between their positions is exactly 3.

    For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be

    containsCloseNums(nums, k) = false.

    The absolute difference between the positions of the two 2s is 3, which is more than k.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer nums

    Guaranteed constraints:
    0 ≤ nums.length ≤ 55000,
    -231 - 1 ≤ nums[i] ≤ 231 - 1.

    [input] integer k

    Guaranteed constraints:
    0 ≤ k ≤ 35000.

    [output] boolean

"""

def test():
    testeql(containsCloseNums([0, 1, 2, 3, 5, 2], 3), True)
    testeql(containsCloseNums([0, 1, 2, 3, 5, 2], 2), False)
    testeql(containsCloseNums([1], 1), False)
    testeql(containsCloseNums([-1,-1], 1), True)
    testeql(containsCloseNums([2,2], 3), True)
    testeql(containsCloseNums([1,0,1,1], 1), True)

def containsCloseNums(nums, k):
    lastSeen = {}
    for i, n in enumerate(nums):
        if n in lastSeen:
            if i - lastSeen[n] <= k:
                return True
            else:
                lastSeen[n] = i
        else:
            lastSeen[n] = i
    return False
