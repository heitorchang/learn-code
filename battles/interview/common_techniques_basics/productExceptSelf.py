description = """

You have an array nums. We determine two functions to perform on nums. In both cases, n is the length of nums:

    fi(nums) = nums[0] · nums[1] · ... · nums[i - 1] · nums[i + 1] · ... · nums[n - 1]. (In other words, fi(nums) is the product of all array elements except the ithf.)
    g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).

Using these two functions, calculate all values of f modulo the given m. Take these new values and add them together to get g. You should return the value of g modulo the given m.

Example

For nums = [1, 2, 3, 4] and m = 12, the output should be
productExceptSelf(nums, m) = 2.

The array of the values of f is: [24, 12, 8, 6]. If we take all the elements modulo m, we get:
[0, 0, 8, 6]. The sum of those values is 8 + 6 = 14, making the answer 14 % 12 = 2.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer nums

    Guaranteed constraints:
    2 ≤ nums.length ≤ 2 · 105,
    1 ≤ nums[i] ≤ 100.

    [input] integer m

    Guaranteed constraints:
    2 ≤ m ≤ 105.

    [output] integer


"""

def test():
    testeql(productExceptSelf([1,2,3,4], 12), 2)
    testeql(productExceptSelf([5, 8, 6, 3, 2], 8), 4)
    
def productExceptSelfNaive(nums, m):
    # naive solution
    def f(i, nums):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod *= nums[j]
        return prod

    total = 0
    for i in range(len(nums)):
        total += f(i, nums)
    return total % m

def productExceptSelf(nums, m):
    # codefights blog
    lenNums = len(nums)
    prodPrefix = [1] * lenNums
    prodSuffix = [1] * lenNums

    # build tables
    for i in range(1, lenNums):
        prodPrefix[i] = (prodPrefix[i-1] * nums[i-1]) % m
        prodSuffix[-i-1] = (prodSuffix[-i] * nums[-i]) % m

    total = 0
    for i in range(len(nums)):
        total += prodPrefix[i] * prodSuffix[i]
    return total % m
