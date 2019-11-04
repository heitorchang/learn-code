description = """

e(nums, queries) = 10.

The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 6 = 10.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer nums

    An array of integers.

    Guaranteed constraints:
    1 ≤ nums.length ≤ 105,
    -1000 ≤ nums[i] ≤ 1000.

    [input] array.array.integer queries

    An array containing sets of integers that represent the indices to query in the nums array.

    Guaranteed constraints:
    1 ≤ queries.length ≤ 3 · 105,
    queries[i].length = 2,
    0 ≤ queries[i][j] ≤ nums.length - 1,
    queries[i][0] ≤ queries[i][1].

    [output] integer

    An integer that is the sum of all of the sums gotten from querying nums, taken modulo 10^9 + 7.
"""

def test():
    testeql(sumInRange([3, 0, -2, 6, -3, 2],
                       [[0,2], 
                        [2,5], 
                        [0,5]]), 10)
    
    testeql(sumInRange([34, 19, 21, 5, 1, 10, 26, 46, 33, 10],
                       [[3,7], 
 [3,4], 
 [3,7], 
 [4,5], 
 [0,5]]), 283)
    
    # testeql(sumInRange(list(range(16)), [0, 1]), 1)
    
def sumInRangeTLE(nums, queries):
    # Time limit exceeded
    # count = [0] * len(nums)
    tot = 0
    memo = {}
    
    for q in queries:
        if (q[0], q[1]) in memo:
            partSum = memo[(q[0], q[1])]
        else:
            partSum = 0
            for i in range(q[0], q[1]+1):
                partSum += nums[i]
                memo[(q[0], q[1])] = partSum
        tot += partSum % (10 ** 9 + 7)
    return tot % (10 ** 9 + 7)
    

def sumInRange(nums, queries):
    # segment tree
    # http://codeforces.com/blog/entry/18051
    # holy **** it passed

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

    # pr('t')
    # build
    for i in range(n-1, 0, -1):
        # pr('i')
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

    result = 0
    for q in queries:
        result += query(q[0], q[1]) % (10 ** 9 + 7)
    return result % (10 ** 9 + 7)

    
# solution by k_lee

def sumInRangeCaptainSolution(nums, queries):
    psums = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        psums[i+1] += psums[i] + nums[i]
    return sum(psums[b+1] - psums[a] for a, b in queries) % (10 ** 9 + 7)
