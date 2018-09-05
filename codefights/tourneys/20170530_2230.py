def extractMatrixColumn(matrix, column):
    result = []
    for row in matrix:
        result.append(row[column])
    return result


def test():
    testeql(
