description = """
You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden. The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system. The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.

Given a list of non-negative integers nums representing the amount of money hidden in each house, determine the maximum amount of money you can rob in one night without triggering an alarm.

Example

For nums = [1, 1, 1], the output should be
houseRobber(nums) = 2.

The optimal way to get the most money in one night is to rob the first and the third houses for a total of 2.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer nums

    An array representing the amount of money that each house on the street has.

    Guaranteed constraints:
    0 ≤ nums.length ≤ 100,
    0 ≤ nums[i] ≤ 500.

    [output] integer

"""

def test():
    print("houseRobber tests")
    testeql(houseRobber([1, 1, 1]), 2)
    testeql(houseRobber([0]), 0)
    testeql(houseRobber([1,2,1,1]), 3)
    testeql(houseRobber([1,1,1,2]), 3)
    testeql(houseRobber([1,7,9,4]), 11)
    testeql(houseRobber([4,9,7,1]), 11)
    testeql(houseRobber([4,1,2,7,5,3,1]), 14)
    testeql(houseRobberNinjaSolution([4,1,2,7,5,3,1]), 14)





















def houseRobber(nums):
    len_nums = len(nums)
    
    # special cases
    if nums == []:
        return 0
    
    if len_nums < 3:
        return max(nums)

    prev = [0 for _ in range(len_nums)]
    prev[0] = nums[0]
    prev[1] = max(nums[0], nums[1])
    
    if nums[0] + nums[2] > nums[1]:
        last_selected = True
        prev[2] = nums[0] + nums[2]
    else:
        last_selected = False
        prev[2] = nums[0]
        
    for i in range(3, len(nums)):
        new = nums[i]

        prev_free = max(prev[:i-1])
        # pr('prev_free new')
        prev[i] = max(prev_free + new, prev[i-1])
        # pr('prev')
        # print()
    return max(prev)

def houseRobberNinjaSolution(nums):
    a = b = 0
    for x in nums:
        a, b = b + x, max(a, b)
    return max(a, b)
    
