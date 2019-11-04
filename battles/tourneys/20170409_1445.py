def allVisited(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = True
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == False:
                result = False
    return result

def findPath(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    visited = [[False for col in range(cols)] for row in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                cur_row = r
                cur_col = c
                break
    pr('matrix')
    pr('r c')

    cur_val = 1
    visited[cur_row][cur_col] = True
    while not allVisited(visited):
        if cur_row > 0:
            valUp = matrix[cur_row-1][cur_col]
            if valUp == cur_val + 1:
                cur_row -= 1
                visited[cur_row][cur_col] = True
        elif cur_row < rows - 1:
            valDown = matrix[cur_row+1][cur_col]
            if valDown == cur_val + 1:
                cur_row += 1
                visited[cur_row][cur_col] = True
        elif cur_col < cols - 1:
            val = matrix[cur_row][cur_col + 1]
            if val == cur_val + 1:
                cur_col += 1
                visited[cur_row][cur_col] = True
        elif cur_row > 0:
            valDown = matrix[cur_row][cur_col - 1]
                if valDown == cur_val + 1:
                cur_col -= 1
                visited[cur_row][cur_col] = True
        else:
            return False
    return allVisited(visited)

def test():
    testeql(1,1)
