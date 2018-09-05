def neighboringCells(matrix):
    r = len(matrix)
    c = len(matrix[0])
    pr('r c')
    result = [[0 for _ in range(c)] for _ in range(r)]
    for rr in range(r):
        for cc in range(c):
            tot = 0
            # top
            if rr > 0:
                if matrix[rr-1][cc] == 0:
                    tot += 1
            # bottom
            if rr < r-1:
                if matrix[rr+1][cc] == 0:
                    tot += 1
            # left
            if cc > 0:
                if matrix[rr][cc-1] == 0:
                    tot += 1
            # right
            if cc < c-1:
                if matrix[rr][cc+1] == 0:
                    tot += 1
            result[rr][cc] = tot
    return result


def test():
    testeql(neighboringCells([[0,0,0]]), [[1,2,1]])
