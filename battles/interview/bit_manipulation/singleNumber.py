description = """
You are given an array of integers in which every element appears twice, except for one. Find the element that only appears one time. Your solution should have a linear runtime complexity (O(n)). Try to implement it without using extra memory.

Example

For nums = [2, 2, 1], the output should be
singleNumber(nums) = 1.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer nums

    Guaranteed constraints:
    1 ≤ nums.length ≤ 104,
    -109 ≤ nums[i] ≤ 109.

    [output] integer

"""

def test():
    print("singleNumber tests")
    testeql(singleNumber([2,2,1]), 1)
    testeql(singleNumber([-1, -1, -2]), -2)
    testeql(singleNumberMySolution([2,2,1]), 1)

















from collections import defaultdict

def singleNumberMySolution(nums):
    d = defaultdict(int)
    for n in nums:
        d[n] += 1
    for k in d:
        if d[k] == 1:
            return k

def singleNumber(nums):
    # solution by minato
    
    singleElem = 0
    
    for num in nums:
        singleElem ^= num 
    return singleElem

