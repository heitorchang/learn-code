description = """
Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

Example

For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
composeRanges(nums) = ["-1->2", "6->7", "9"].

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer nums

    A sorted array of unique integers.

    Guaranteed constraints:
    0 ≤ nums.length ≤ 15,
    -(231 - 1) ≤ nums[i] ≤ 231 - 1.

    [output] array.string

"""

def test():
    testeql(composeRanges([-1, 0, 1, 2, 6, 7, 9]), ["-1->2", 
                                                    "6->7", 
                                                    "9"])
    testeql(composeRanges([]), [])
    testeql(composeRanges([-1]), ["-1"])
    testeql(composeRanges([0, 1, 2, 4, 5, 7]), ["0->2", 
                                                "4->5", 
                                                "7"])
    testeql(composeRanges([0,1]), ["0->1"])






    
def singleRange(lst):
    if len(lst) == 1:
        return str(lst[0])
    else:
        return str(lst[0]) + "->" + str(lst[-1])
        
def composeRanges(nums):
    out = []
    if len(nums) == 0:
        return out
    curRange = [nums[0]]
    for n in nums[1:]:
        if n == curRange[-1] + 1:
            curRange.append(n)
        else:
            out.append(singleRange(curRange))
            curRange = [n]
    out.append(singleRange(curRange))
    return out
                       
