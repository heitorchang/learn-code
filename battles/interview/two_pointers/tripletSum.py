description = """
Note: Write a solution with O(n2) time complexity, since this is what you would be asked to do during a real interview.

You have an array a composed of exactly n elements. Given a number x, determine whether or not a contains three elements for which the sum is exactly x.

Example

    For x = 15 and a = [14, 1, 2, 3, 8, 15, 3], the output should be
    tripletSum(x, a) = false;

    For x = 8 and a = [1, 1, 2, 5, 3], the output should be
    tripletSum(x, a) = true.

    The given array contains the elements 1,2, and 5, which add up to 8.

Input/Output

    [time limit] 4000ms (py3)

    [input] integer x

    Guaranteed constraints:
    1 ≤ x ≤ 105.

    [input] array.integer a

    Guaranteed constraints:
    3 ≤ a.length ≤ 6 · 105,

    1 ≤ a[i] ≤ 105.

    [output] boolean

    Return true if the array contains three elements that add up to x and false otherwise.

"""
def test():
    testeql(tripletSum(15, [14, 1, 2, 3, 8, 15, 3]), False)
    testeql(tripletSum(8, [1, 1, 2, 5, 3]), True)
    testeql(tripletSumMySolution(15, [14, 1, 2, 3, 8, 15, 3]), False)
    testeql(tripletSumMySolution(8, [1, 1, 2, 5, 3]), True)























    
def tripletSum(x, a):
    # solution by redcpp
    
    a = sorted(a)
    for i in range(len(a)-1):
        target = x - a[i]
        l, r = i+1, len(a)-1
        while l != r:
            if a[l] + a[r] < target:
                l += 1
            elif a[l] + a[r] > target:
                r -= 1
            else:
                return True
    return False

def tripletSumMySolution(x, a):
    # not ideal because it is O(n^3), not O(n^2)
    len_a = len(a)
    for i in range(len_a-2):
        for j in range(i+1, len_a-1):
            for k in range(j+1, len_a):
                if a[i] + a[j] + a[k] == x:
                    return True
    return False

