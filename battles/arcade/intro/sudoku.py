description = """
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For the first example below, the output should be true. For the other grid, the output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.array.integer grid

    A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

    [output] boolean

    true if the given grid represents a correct solution to Sudoku, false otherwise.

"""

def test():
    testeql(sudoku([[1,3,2,5,4,6,9,8,7], 
 [4,6,5,8,7,9,3,2,1], 
 [7,9,8,2,1,3,6,5,4], 
 [9,2,1,4,3,5,8,7,6], 
 [3,5,4,7,6,8,2,1,9], 
 [6,8,7,1,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,3,6,5,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]), True)
    
def sudoku(grid):
    g = grid
    # 0 1 2   3 4 5   6 7 8
    subgrid = [None] * 9
    subgrid[0] = set([g[0][0], g[0][1], g[0][2], g[1][0], g[1][1], g[1][2], g[2][0], g[2][1], g[2][2]])
    subgrid[1] = set([g[0][3], g[0][4], g[0][5], g[1][3], g[1][4], g[1][5], g[2][3], g[2][4], g[2][5]])
    subgrid[2] = set([g[0][6], g[0][7], g[0][8], g[1][6], g[1][7], g[1][8], g[2][6], g[2][7], g[2][8]])
    
    subgrid[3] = set([g[3][0], g[3][1], g[3][2], g[4][0], g[4][1], g[4][2], g[5][0], g[5][1], g[5][2]])
    subgrid[4] = set([g[3][3], g[3][4], g[3][5], g[4][3], g[4][4], g[4][5], g[5][3], g[5][4], g[5][5]])
    subgrid[5] = set([g[3][6], g[3][7], g[3][8], g[4][6], g[4][7], g[4][8], g[5][6], g[5][7], g[5][8]])
    
    subgrid[6] = set([g[6][0], g[6][1], g[6][2], g[7][0], g[7][1], g[7][2], g[8][0], g[8][1], g[8][2]])
    subgrid[7] = set([g[6][3], g[6][4], g[6][5], g[7][3], g[7][4], g[7][5], g[8][3], g[8][4], g[8][5]])
    subgrid[8] = set([g[6][6], g[6][7], g[6][8], g[7][6], g[7][7], g[7][8], g[8][6], g[8][7], g[8][8]])

    for s in subgrid:
        if len(s) != 9:
            return False

    # check rows
    for row in grid:
        if len(set(row)) != 9:
            return False

    # check columns
    for colNum in range(9):
        colSet = set()
        for rowNum in range(9):
            colSet.add(g[rowNum][colNum])
        if len(colSet) != 9:
            return False
    return True










