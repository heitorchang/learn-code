description = """

You have an unsorted array arr of non-negative integers and a number s. Find a longest contiguous subarray in arr that has a sum equal to s. Return two integers that represent its inclusive bounds. If there are several possible answers, return the one with the smallest left bound. If there are no answers, return [-1].

Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.

Example

    For s = 12 and arr = [1, 2, 3, 7, 5], the output should be
    findLongestSubarrayBySum(s, arr) = [2, 4].

    The sum of elements from the 2nd position to the 4th position (1-based) is equal to 12: 2 + 3 + 7.

    For s = 15 and arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be
    findLongestSubarrayBySum(s, arr) = [1, 5].

    The sum of elements from the 1st position to the 5th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5.

    For s = 15 and arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], the output should be
    findLongestSubarrayBySum(s, arr) = [1, 8].

    The sum of elements from the 1st position to the 8th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5 + 0 + 0 + 0.

Input/Output

    [time limit] 4000ms (py3)

    [input] integer s

    The sum of the subarray that you are searching for.

    Guaranteed constraints:
    0 ≤ s ≤ 109.

    [input] array.integer arr

    The given array.

    Guaranteed constraints:
    1 ≤ arr.length ≤ 105,
    0 ≤ arr[i] ≤ 104.

    [output] array.integer

    An array that contains two elements that represent the left and right bounds of the subarray, respectively (1-based). If there is no such subarray, return [-1].

"""

def test():
    # testeql(findLongestSubarrayBySum(810, [85, 157, 91, 94, 197, 153, 55, 146, 109, 49, 92, 113, 132, 115, 40]), [-1])
    testeql(findLongestSubarrayBySum(15, [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]), [1, 8])
    testeql(findLongestSubarrayBySum(3, [3]), [1,1])
    testeql(findLongestSubarrayBySum(3, [0, 3, 0]), [1,3])
    testeql(findLongestSubarrayBySum(12, [1,2,3,7,5]), [2,4])
    testeql(findLongestSubarrayBySum(49, [1,2,3,4,5,49]), [6,6])
    testeql(findLongestSubarrayBySum(15, [1,8,5,10,1]), [3,4])
    testeql(findLongestSubarrayBySum(9, [1,1,1,1,9]), [5,5])
    testeql(findLongestSubarrayBySum(19, [1,1,1,1,9,10]), [5,6])
    testeql(findLongestSubarrayBySum(123, [1,20,3,100]), [2,4])
    testeql(findLongestSubarrayBySum(0, [1,0,2]), [2,2])
    testeql(findLongestSubarrayBySumFreemanlex(15, [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]), [1, 8])
    testeql(findLongestSubarrayBySumFreemanlex(0, [1,0,2]), [2,2])
    
def testOther():
    testeql(findLongestSubarrayBySum(0, [1,0,2]), [2,2])
    testeql(findLongestSubarrayBySum(12, [1,2,10]), [2,3])
    testeql(findLongestSubarrayBySum(13, [1,2,10]), [1,3])
    testeql(findLongestSubarrayBySum(1003, [1,2,3,1000,2000,3000,4000,5000]), [3,4])
    testeql(findLongestSubarrayBySum(2, [1,2,3]), [2,2])
    testeql(findLongestSubarrayBySum(6, [1,2,3]), [1,3])

def testSome():
    testeql(findLongestSubarrayBySum(9999, [1,2,3,4,5]), [-1])
    testeql(findLongestSubarrayBySum(15, [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]), [1, 8])
    
def findLongestSubarrayBySumTLE(s, arr):
    # time limit exceeded
    len_arr = len(arr)
    maxLen = 0
    ans = None
    for left in range(len_arr-1, -1, -1):
        for right in range(left, len_arr + 1):
            if sum(arr[left:right]) == s:
                # print(left, right)
                subarrayLen = right - left
                if subarrayLen > maxLen:
                    maxLen = subarrayLen
                    ans = (left, right)

    if not ans:
        return [-1]
    return [ans[0] + 1, ans[1]]



    
def findLongestSubarrayBySumSegmentTree(s, nums):
    # also times out
    
    # segment tree
    # http://codeforces.com/blog/entry/18051
    # holy **** it passed
    arr = nums[:]
    len_arr = len(arr)
    ans = None
    maxLen = 0
    
    orig = nums[:]
    origLen = len(nums)
    newNums = [0] * int(2 ** ((log(origLen) // log(2)) + 1))

    for i in range(origLen):
        newNums[i] = nums[i]

    nums = newNums
    
    n = len(nums)
    N = n << 1
    t = [0] * 2 * N

    for i in range(n):
        t[n + i] = nums[i]

    # build
    for i in range(n-1, 0, -1):
        t[i] = t[i << 1] + t[i << 1 | 1]

    def query(left, right):
        rtInit = right
        res = 0
        left += n
        right += n
        while left < right:
            if left & 1:
                res += t[left]
                # pr('left')
                left += 1
            if right & 1:
                right -= 1
                # pr('right')
                res += t[right]
            left >>= 1
            right >>= 1
        return res + orig[rtInit]

    for left in range(len_arr-1, -1, -1):
        for right in range(left, len_arr):
            if left == right:
                subarrayLen = 1
                if subarrayLen >= maxLen and orig[left] == s:
                    maxLen = subarrayLen
                    ans = (left, right)
            q = query(left, right)
            if q > s:
                break
            if q == s:            
                subarrayLen = right - left
                if subarrayLen > maxLen:
                    maxLen = subarrayLen
                    ans = (left, right)

    if not ans:
        return [-1]
    return [ans[0] + 1, ans[1] + 1]



def findLongestSubarrayBySumAlsoTLE(s, arr):
    # time limit exceeded
    len_arr = len(arr)
    maxLen = 0
    minLeft = len_arr
    ans = None
    for left in range(len_arr):
        curSum = 0
        for right in range(left, len_arr):
            curSum += arr[right]
            if curSum > s:
                break
            if curSum == s:
                curLen = right - left
                if curLen >= maxLen and left <= minLeft:
                    minLeft = left
                    maxLen = curLen
                    ans = (left, right)
    if not ans:
        return [-1]
    return [ans[0] + 1, ans[1] + 1]


def findLongestSubarrayBySumDoesNotPass(s, arr):
# def findLongestSubarrayBySum(s, arr):
    # idea: moving window
    # does not pass final test
    left = 0
    right = 0
    sumWindow = 0

    lenArr = len(arr)
    maxLen = 0
    minLeft = lenArr

    ans = None

    while left < lenArr:
        while sumWindow <= s and right < lenArr:
            sumWindow += arr[right]
            if sumWindow == s:
                # print("match right ", end="")
                if right - left >= maxLen:
                    maxLen = right - left
                    minLeft = left
                    ans = (left + 1, right + 1)
            right += 1
            
        sumWindow -= arr[left]
        left += 1
        if sumWindow == s:
            # print("match left ", end="")
            # pr("left right sumWindow")
            if right - left >= maxLen and left < minLeft:
                maxLen = right - left
                minLeft = left
                # pr('left right')
                ans = (left + 1, right)
                
        # pr('left right sumWindow')
    if not ans:
        return [-1]
    return list(ans)


def findLongestSubarrayBySum(s, arr):
    # idea: check longest for array starting at 0
    # Passed, not sure what was different from
    #   findLongestSubarrayBySumDoesNotPass.
    # Maybe the test case for s == 0

    if s == 0:
        try:
            zeroIndex = arr.index(0)
            return [zeroIndex + 1, zeroIndex + 1]
        except ValueError:
            return [-1]

    left = 0
    right = 0

    curSum = 0
    maxLen = -1
    lenArr = len(arr)
    ansLeft = -1
    ansRight = -1
    
    while left < lenArr:
        # pr('"outer_loop" left right curSum')
        while curSum <= s and right < lenArr:
            curSum += arr[right]
            # pr('left right curSum')
            if curSum == s:
                # print('match #1', left, right)
                curLen = right - left
                if curLen > maxLen:
                    maxLen = curLen
                    ansLeft = left + 1
                    ansRight = right + 1
            right += 1
        curSum -= arr[left]
        left += 1
        if curSum == s:
            # print("match #2", left, right)
            curLen = right - left
            if curLen > maxLen:
                maxLen = curLen
                ansLeft = left + 1
                ansRight = right
    if ansLeft == -1 and ansRight == -1:
        return [-1]
        
    return [ansLeft, ansRight]
    

def findLongestSubarrayBySumFreemanlex(s, arr):
    i2 = res = 0
    len_arr = len(arr)
    ind = [0, 0]
    for i1 in range(len_arr):
        while i2 < len_arr and res < s:
            res += arr[i2]
            i2 += 1
        if res == s:
            while i2 < len_arr and not arr[i2]:
                i2 += 1
            if ind == [0, 0] or (ind != [0, 0] and i2 - i1 > ind[1] - ind[0]):
                ind = [i1 + 1, i2]
        res -= arr[i1]
    return (ind, [-1])[ind == [0, 0]]
