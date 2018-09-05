description = """
You have two integer arrays, a and b, and an integer target value v. Determine whether there is a pair of numbers, where one number is taken from a and the other from b, that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false.

Example

For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
sumOfTwo(a, b, v) = true.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer a

    An array of integers.

    Guaranteed constraints:
    0 ≤ a.length ≤ 105,
    -109 ≤ a[i] ≤ 109.

    [input] array.integer b

    An array of integers.

    Guaranteed constraints:
    0 ≤ b.length ≤ 105,
    -109 ≤ b[i] ≤ 109.

    [input] integer v

    Guaranteed constraints:
    -109 ≤ v ≤ 109.

    [output] boolean

    true if there are two elements from a and b which add up to v, and false otherwise.

"""

def test():
    print("sumOfTwo tests")
    testeql(sumOfTwo([1, 2, 3], [10, 20, 30, 40], 42), True)
    testeql(sumOfTwo([1, 2, 3], [10, 20, 30, 40], 50), False)




















    
def sumOfTwoMySolution(a, b, v):
    hash_a = {}
    hash_b = {}
    for i in range(len(a)):
        hash_a[a[i]] = i
    for i in range(len(b)):
        hash_b[b[i]] = i
    for i in range(len(b)):
        val = None
        try:
            val = hash_a[v - b[i]]
            if val != -1:
                return True
        except:
            pass
    return False

def sumOfTwo(a, b, v):
    # solution by jens_k
    s = set(b)
    for n in a:
        if (v - n) in s:
            return True
    return False
