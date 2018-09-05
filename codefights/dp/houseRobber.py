# interview/DP Basic

# SEE NEW SOLUTION HOUSE ROBBER_2

def houseRobber(nums):

    # idea: keep two arrays,
    # one OFF
    # another ON
    # each array has maximal length so far.
    # depending on value of new, decide which array to use, on or off

    len_nums = len(nums)
    # special cases
    if nums == []:
        return 0
    
    if len_nums < 3:
        return max(nums)
    
    first_3 = nums[0:3]
    max_sum = 0
    
    last_chosen = [0 for _ in range(len_nums)]
    last_not_chosen = [0 for _ in range(len_nums)]
    last_chosen[0] = nums[0]
    last_chosen[1] = nums[1]
    last_chosen[2] = nums[0] + nums[2]
    last_not_chosen[2] = nums[1]
    
    for i in range(3, len_nums):
        new = nums[i]
        prs('new')

        # unselect last_chosen
        last_unselected = last_chosen[i-1] - nums[i-1]
        prs('last_chosen last_not_chosen last_unselected')
        if new + last_unselected > max(new + last_not_chosen[i-1], last_chosen[i-1]):
            last_chosen[i] = last_unselected + new
            last_not_chosen[i] = last_not_chosen[i]
            
        elif new + last_not_chosen[i-1] > last_chosen[i-1]:
            last_chosen[i] = last_not_chosen[i-1] + new
            last_not_chosen[i] = last_chosen[i-1]
        else:
            last_not_chosen[i] = last_chosen[i-1]
            last_chosen[i] = last_chosen[i-1]
        prs('last_chosen last_not_chosen last_unselected')
    return max(last_chosen[-1], last_not_chosen[-1])
        
def test():
    # testeql(houseRobber([2,1]), 2)
    # testeql(houseRobber([1,1,1]), 2)
    testeql(houseRobber([1,1,1,1]), 2)
    testeql(houseRobber([3,5,3,0]), 6)
    # testeql(houseRobber([1,1,1,1,1,6]), 8)
    # testeql(houseRobber([1,1,1,2]), 3)
    # testeql(houseRobber([2, 1, 2, 6, 1, 8, 10, 10]), 26)
    # testeql(houseRobber([232, 161, 89, 177, 117, 212, 126, 247, 155, 197, 88, 217, 81, 207]), 1489)
    testeql(houseRobber([1,3,1,3,100]), 103)
    testeql(houseRobber([4, 1, 2, 7, 5, 3, 1]), 14)
