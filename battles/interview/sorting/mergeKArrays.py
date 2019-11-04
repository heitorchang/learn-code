description = """
Given K sorted arrays, return their sorted concatenation.

Example

For arrays = [[1, 3, 5], [2, 3], [2, 3, 5, 8]], the output should be
mergeKArrays(arrays) = [1, 2, 2, 3, 3, 3, 5, 5, 8].

Input/Output

    [time limit] 4000ms (py3)

    [input] array.array.integer arrays

    An array of K one-dimensional sorted arrays.

    Guaranteed constraints:
    3 ≤ arrays.length ≤ 10,
    0 ≤ arrays[i].length ≤ 5,
    -100 ≤ arrays[i][j] ≤ 100.

    [output] array.integer

"""

def test():
    # testeql(mergeKArrays([[1],  [],  [1,1],  []]), [1,1,1])
    testeql(mergeKArrays([[1,3,5],  [2,3],  [2,3,5,8]]), [1, 2, 2, 3, 3, 3, 5, 5, 8])


def mergeKArrays(arrays):
    firstUnused = []
    result = []
    n = 0
    for i in range(len(arrays)):
        firstUnused.append(0)
        n += len(arrays[i])
    for i in range(n):
        minIndex = -1
        minValue = 0
        for j in range(len(arrays)):
            if firstUnused[j] < len(arrays[j]):
                pr('firstUnused j minIndex arrays[j][firstUnused[j]]')
                if minIndex == -1 or arrays[j][firstUnused[j]] < minValue:  # INSERT CODE HERE
                # if False:
                    minIndex = j
                    minValue = arrays[j][firstUnused[j]]
                    pr('minValue')
        result.append(minValue)
        firstUnused[minIndex] += 1
    return result
