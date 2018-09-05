# https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python

def array1D(n):
    return [0] * n

def array2D(r, c):
    # r Rows x c Columns
    return [row[:] for row in [[0] * c] * r]

def test():
    testeql(array1D(3), [0, 0, 0])

    # make sure changing a row does not affect the other
    arr2D = array2D(2, 3)
    arr2D[0][0] = 999
    testeql(arr2D, [[999, 0, 0], [0, 0, 0]])
