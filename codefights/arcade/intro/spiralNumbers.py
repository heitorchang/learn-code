description = """

Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]

Input/Output

    [time limit] 4000ms (py3)

    [input] integer n

    Matrix size, a positive integer.

    Guaranteed constraints:
    3 ≤ n ≤ 10.

    [output] array.array.integer

"""


def test():
    testeql(spiralNumbers(3), [[1,2,3], 
 [8,9,4], 
 [7,6,5]])


    
def spiralNumbers(n):
    def outOfBounds(coords):
        if coords[0] < 0 or coords[0] >= n or coords[1] < 0 or coords[1] >= n:
            return True
        return False
        
    m = [row[:] for row in [[0] * n] * n]
    # Right, Down, Left, Up
    direction = [(0,1), (1,0), (0,-1), (-1,0)]
    curDir = 0
    curPos = (0, 0)
    for i in range(1, n*n + 1):
        m[curPos[0]][curPos[1]] = i
        d = direction[curDir % 4]
        nextPos = (curPos[0] + d[0], curPos[1] + d[1])
        if outOfBounds(nextPos) or m[nextPos[0]][nextPos[1]] != 0:
            # change direction
            curDir += 1
            d = direction[curDir % 4]
            nextPos = (curPos[0] + d[0], curPos[1] + d[1])
        curPos = nextPos
    return m

    
