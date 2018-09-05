def differentSquares(matrix):
    squares = set()
    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            sq = "%d.%d.%d.%d" % (matrix[r][c], matrix[r][c+1], matrix[r+1][c], matrix[r+1][c+1])
            squares.add(sq)
    return len(squares)            


def test():
    testeql(differentSquares([[1,2,1], 
 [2,2,2], 
 [2,2,2], 
 [1,2,3], 
 [2,2,1]]), 6)
