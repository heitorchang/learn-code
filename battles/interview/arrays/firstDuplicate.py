description = """
Note: Write a solution with O(n) time complexity and O(1) additional space complexity, since this is what you would be asked to do during a real interview.

Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

    For a = [2, 3, 3, 1, 5, 2], the output should be
    firstDuplicate(a) = 3.

    There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

    For a = [2, 4, 3, 5, 1], the output should be
    firstDuplicate(a) = -1.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer a

    Guaranteed constraints:
    1 ≤ a.length ≤ 105,
    1 ≤ a[i] ≤ a.length.

    [output] integer

    The element in a that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return -1.

"""

def test():
    testeql(firstDuplicate([2, 3, 3, 1, 5, 2]), 3)
    testeql(firstDuplicate([2, 4, 3, 5, 1]), -1)
    testeql(firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8]), 6)

    testeql(firstDuplicateSet([2, 3, 3, 1, 5, 2]), 3)
    testeql(firstDuplicateSet([2, 4, 3, 5, 1]), -1)
    testeql(firstDuplicateSet([8, 4, 6, 2, 6, 4, 7, 9, 5, 8]), 6)





    

def firstDuplicate(a):
    marker = 10 ** 6  # a number larger than the largest possible entry
    # if a number n has been seen, a[i] will be a[i] + marker
    len_a = len(a)
    out = marker
    outInx = marker
    for i in range(len_a):
        if a[a[i] % marker - 1] >= marker and i < outInx:
            out = a[i] % marker
            outInx = i
            # pr('i out')
        a[a[i] % marker - 1] += marker
        # pr('i a[i] a')
    if out == marker:
        return -1
    return out

def firstDuplicateSet(a):
    seen = set()
    lowestIndex = float('inf')
    out = float('inf')
    for i in range(len(a)):
        if a[i] in seen:
            if i < lowestIndex:
                out = a[i]
                lowestIndex = i
        seen.add(a[i])
    if out == float('inf'):
        return -1
    return out

    
def firstDuplicateAWice(A):
    # Ninja solution
    for i, x in enumerate(A):
        A[abs(x) - 1] *= -1
        if A[abs(x) - 1] > 0:
            return abs(x)
    return -1
