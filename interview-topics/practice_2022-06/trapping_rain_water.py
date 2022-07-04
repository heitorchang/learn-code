# https://www.geeksforgeeks.org/trapping-rain-water/

# asked by joinner in 2019

# inp = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# is
#        o
#    o===oo=o
#  o=oo=oooooo
# ____________
#
# answer = 6

# idea: iterate over idx 1 to len(inp) - 1

def trap(inp):
    water = 0
    for i in range(1, len(inp) - 1):
        max_left = inp[i]
        max_right = inp[i]
        for left in range(i):
            max_left = max(max_left, inp[left])
        for right in range(i+1, len(inp)):
            max_right = max(max_right, inp[right])
        water += min(max_left, max_right) - inp[i]
    return water


def test_trap():
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap([3, 0, 2, 0, 4]))
