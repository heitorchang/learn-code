description = """
Given a sorted integer array in which the range of elements is in the inclusive range [l, r], return its missing inner ranges.

Example

For nums = [-5, 10, 12, 13, 50], l = -5 and r = 88, the output should be

innerRanges(nums, l, r) = ["-4->9", "11", "14->49", "51->88"].

Input/Output

[time limit] 4000ms (py3)
[input] array.integer nums

Guaranteed constraints:

0 ≤ nums.length ≤ 10,

-231 - 1 ≤ nums[i] ≤ 231 - 1.

[input] integer l

Guaranteed constraints:

-231 - 1 ≤ l ≤ r ≤ 231 - 1.

[input] integer r

Guaranteed constraints:

-231 - 1 ≤ l ≤ r ≤ 231 - 1.

[output] array.string
"""

def test():
    # testeql(cleanRange([-1,-1,2,2,3,4,5]), [-1,2,3,4,5])
    # testeql(outputRange(1,1), "1")
    # testeql(outputRange(1,3), "1->3")
    testeql(innerRanges([], 1, 1), ["1"])
    testeql(innerRanges([-1], -2, -1), ["-2"])
    testeql(innerRanges([-1,-1], -2, 0), ["-2", "0"])
    testeql(innerRanges([2], 0, 9), ["0->1", "3->9"])
    testeql(innerRanges([0,5,9], 0, 9), ["1->4", "6->8"])



    

# 250 xp, 1000 coins

def cleanRange(lst): # remove duplicates
    result = []
    cur = None
    for elem in lst:
        if elem != cur:
            result.append(elem)
        cur = elem
    return result

def outputRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)

def innerRanges(nums, l, r):
    nums = cleanRange(nums)
    if len(nums) == 0:
        return [outputRange(l, r)]
    result = []

    # test left edge
    if l < nums[0]:
        result.append(outputRange(l, nums[0]-1))

    # add ranges in the middle
    for cursor in range(0, len(nums) - 1):
        if nums[cursor + 1] - nums[cursor] > 1:
            result.append(outputRange(nums[cursor] + 1, nums[cursor+1] - 1))

    # test right edge
    if r > nums[-1]:
        result.append(outputRange(nums[-1]+1, r))
        
    return result                

