description = """
Given a matrix of mines, produce the matrix of numbers of mines in neighboring cells
"""

def test():
    true = True
    false = False
    testeql(minesweeper([[true,false,false], 
                         [false,true,false], 
                         [false,false,false]]),
            [[1,2,1], 
             [2,1,1],
             [1,1,1]])

def minesweeper(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    def inBounds(i, j):
        nonlocal rows, cols
        return 0 <= i < rows and 0 <= j < cols
    
    nums = []
    for r in range(rows):
        tmpRow = []
        for c in range(cols):
            # each cell in matrix
            mines = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if inBounds(r+i, c+j) and not (i == 0 and j == 0):
                        pr('r+i c+j')

                        if matrix[r+i][c+j]:
                            mines += 1
            tmpRow.append(mines)
        nums.append(tmpRow)
    return nums
