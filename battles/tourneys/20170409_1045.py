def differentSquares(matrix):
    if len(matrix) < 2 or len(matrix[0]) < 2:
        return 0
    seen = set()
    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            seen.add(str(matrix[r][c]) + str(matrix[r][c+1]) +
                         str(matrix[r+1][c]) + str(matrix[r+1][c+1]))
    return len(seen)

def test():
    testeql(1,1)
