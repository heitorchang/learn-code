description = """

Given a rectangular matrix, return all of the elements of the matrix in spiral order.

Example

For

matrix =
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

the output should be
matrixElementsInSpiralOrder(matrix) = [1, 2, 3, 4, 5, 6, 7, 8, 9].

Input/Output

    [time limit] 4000ms (py3)

    [input] array.array.integer matrix

    A rectangular matrix.

    Guaranteed constraints:

    0 ≤ matrix.length ≤ 100,

    0 ≤ matrix[i].length ≤ 100,

    -1000 ≤ matrix[i][j] ≤ 1000.

    [output] array.integer

"""

# 250 XP, 1000 coins

def test():
    print("matrixElementsInSpiralOrder tests")
    testeql(matrixElementsInSpiralOrder([[1,2,3], 
                                         [8,9,4], 
                                         [7,6,5]]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9])
    testeql(matrixElementsInSpiralOrder([[0,3], [5,5]]), [0, 3, 5, 5])
    testeql(matrixElementsInSpiralOrder([]), [])
    testeql(matrixElementsInSpiralOrder([[1]]), [1])


    


from collections import namedtuple

def matrixElementsInSpiralOrder(matrix):
    if matrix == []:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # delta row, delta column
    Step = namedtuple('Step', 'dr dc')
    Coords = namedtuple('Coords', 'r c')
    
    # right, down, left, up
    directions = [Step(0, 1), Step(1, 0), Step(0, -1), Step(-1, 0)]

    result = []

    curElem = Coords(0, 0)

    count = 0

    segmentCount = 0
    currentDirection = directions[segmentCount % 4]

    while count < rows * cols:
        result.append(matrix[curElem.r][curElem.c])
        visited[curElem.r][curElem.c] = True
        
        nextElem = Coords(curElem.r + currentDirection.dr, curElem.c + currentDirection.dc)

        # check if next step was already visited or is out of bound
        if nextElem.r < 0 or nextElem.r >= rows or nextElem.c < 0 or nextElem.c >= cols or visited[nextElem.r][nextElem.c]:
            segmentCount += 1
            currentDirection = directions[segmentCount % 4]
            nextElem = Coords(curElem.r + currentDirection.dr, curElem.c + currentDirection.dc)
            
        curElem = nextElem
        count += 1
    return result

