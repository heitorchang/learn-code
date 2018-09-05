description = """
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second column. Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1 through 9 one time.

Input/Output

[time limit] 4000ms (py3)
[input] array.array.char grid

A 9 × 9 array of characters, in which each character is either a digit from '1' to '9' or a period '.'.

[output] boolean

Return true if grid represents a valid Sudoku puzzle, otherwise return false.
"""

def test():
    testeql(sudoku2([[".",".",".",".","2",".",".","9","."], 
 [".",".",".",".","6",".",".",".","."], 
 ["7","1",".",".","7","5",".",".","."], 
 [".","7",".",".",".",".",".",".","."], 
 [".",".",".",".","8","3",".",".","."], 
 [".",".","8",".",".","7",".","6","."], 
 [".",".",".",".",".","2",".",".","."], 
 [".","1",".","2",".",".",".",".","."], 
 [".","2",".",".","3",".",".",".","."]]), False)

def sudoku2(grid):
    rows = 9
    cols = 9
    nums = [row[:] for row in [[0] * cols] * rows]

    # read grid
    for r in range(len(grid)):
        row = grid[r]
        for c in range(len(row)):
            char = grid[r][c]
            if char == ".":
                nums[r][c] = 0
            else:
                nums[r][c] = int(char)

    def hasDuplicates(lst):
        lst = list(filter(lambda n: n > 0, lst))
        return len(set(lst)) < len(lst)
    
    # check rows
    for r in range(9):
        if hasDuplicates(nums[r]):
            return False

    # check columns
    for c in range(9):
        col = []
        for r in range(9):
            col.append(nums[r][c])
        if hasDuplicates(col):
            return False

    # check grids
    def threeByThree(grid, startRow, startCol):
        arr = []
        for r in range(startRow, startRow+3):
            for c in range(startCol, startCol+3):
                arr.append(grid[r][c])
        return arr
    
    for startR in range(0, 9, 3):
        for startC in range(0, 9, 3):
            box = threeByThree(nums, startR, startC)
            if hasDuplicates(box):
                return False
            
    return True
