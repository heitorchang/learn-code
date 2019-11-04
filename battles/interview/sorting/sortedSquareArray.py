description = """
Note: Come up with a linear solution, since that is what you would be asked to do in an interview.

You have a sorted array of integers. Write a function that returns a sorted array containing the squares of those integers.

Example

For array = [-6, -4, 1, 2, 3, 5], the output should be
sortedSquaredArray(array) = [1, 4, 9, 16, 25, 36].

The array of squared integers from array is: [36, 16, 1, 4, 9, 25]. When sorted, it becomes: [1, 4, 9, 16, 25, 36].

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer array

    A sorted array of integers.

    Guaranteed constraints:
    1 ≤ array.length ≤ 104,
    -104 ≤ array[i] ≤ 104.

    [output] array.integer

    A sorted array of integers composed of the squared integers from the input array.

"""

def test():
    testeql(sortedSquaredArray([-6, -4, 1, 2, 3, 5]), [1, 4, 9, 16, 25, 36])

def sortedSquaredArray(array):
    # Solution by cheungnj
    stack = []
    squares = []

    for i in array:
        square = i*i
        # squares from negative numbers go onto the stack
        if i < 0:
            stack.append(square)
            continue
        
        # put any of the negative numbers' squares before the current number if they are smaller
        while stack and square >= stack[-1]:
            squares.append(stack.pop())

        squares.append(square)

    # if we have any strays, put them in the array in reverse order
    while stack:
        squares.append(stack.pop())

    return squares
    
