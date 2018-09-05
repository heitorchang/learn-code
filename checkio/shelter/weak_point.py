def weak_point(matrix):
    """find the coordinates of the weak point"""
    # number of columns equals number of rows
    rows = cols = len(matrix)
    row_sum = [0] * rows
    col_sum = [0] * cols
    for r in range(rows):
        for c in range(cols):
            row_sum[r] += matrix[r][c]
            col_sum[c] += matrix[r][c]

    # determine the minimum value's index
    # many ways given in SO, below I've used the easiest to understand
    # https://stackoverflow.com/questions/6193498/
    # ... pythonic-way-to-find-maximum-value-and-its-index-in-a-list
    min_row_value = min(row_sum)
    min_col_value = min(col_sum)

    min_row_index = row_sum.index(min_row_value)
    min_col_index = col_sum.index(min_col_value)
    return [min_row_index, min_col_index]

def test():
    # weak_point([[1,1,1],[1,1,1],[1,1,1]])
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
    print("Testing complete")
