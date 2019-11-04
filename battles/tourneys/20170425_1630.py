def matrixMultiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    rows2 = len(matrix2)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for r in range(rows1):
        for c in range(cols2):
            s = 0
            for i in range(cols1):
                s += matrix1[r][i] * matrix2[i][c]
            result[r][c] = s
    return result
    


def test():
    testeql(matrixMultiplication([[1,1,1], 
 [0,0,0]], [[2,1], [1,2], [2,1]]), [[5,4], 
 [0,0]])
