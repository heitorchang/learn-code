def trapezoidalRule(l, r, p):
    pass
    
def matrixSum(matrix1, matrix2):

    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[0])):
            result[i].append(matrix1[i][j] + matrix2[i][j])
    return result


def test():
    testeql(trapezoidalRule(1,3,[0,1,0,4]), 92)
    testeql(matrixSum([[1,1,1], 
                       [0,0,0]],
                      [[2,1,1],
                       [2,1,1]]), [[3,2,2],
                                   [2,1,1]])

print(88842 - 88592)
