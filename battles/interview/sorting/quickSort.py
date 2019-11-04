description = """
You are given an array of integers. Sort its sub-array between the given indices l and r (inclusive) and leave the other elements intact.

Example

For a = [5, 2, 1, 7, 5, 3, 2, 3], l = 0 and r = 3, the output should be
quickSort(a, l, r) = [1, 2, 5, 7, 5, 3, 2, 3].

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer a

    Guaranteed constraints:
    5 ≤ a.length ≤ 100,
    1 ≤ a[i] ≤ 100.

    [input] integer l

    The left bound of the array segment to sort.

    Guaranteed constraints:
    0 ≤ l ≤ r.

    [input] integer r

    The right bound of the array segment to sort.

    Guaranteed constraints:
    l ≤ r < a.length.

    [output] array.integer

"""

def test():
    testeql(quickSort([5, 2, 1, 7, 5, 3, 2, 3], 0, 3), [1, 2, 5, 7, 5, 3, 2, 3])
    testeql(quickSort([5, 2, 1, 7, 5, 3, 2, 3], 0, 7), [1, 2, 2, 3, 3, 5, 5, 7])

def quickSort(a, l, r):

    if l >= r:
        return a

    x = a[l]
    i = l
    j = r

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            t = a[i]
            a[i] = a[j]
            a[j] = t
            i += 1
            j -= 1

    quickSort(a, l, j)
    quickSort(a, i, r)

    return a
