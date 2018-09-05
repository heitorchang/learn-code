"""
Idea:

o o o o 
o o o o
o o o o
o o o o

 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

look for every single horizontal segment in the first three rows,
and check if it has the |_| segments to match and make a square

then look for _o_ segments, and finally the big outer square
"""

def checkio(lines_list):
    """Return the quantity of squares"""
    lines_tuples = [tuple(sorted(line)) for line in lines_list]
    lines_set = set(lines_tuples)
    total = 0
    # check small square
    for row in range(1, 10, 4):
        for col in range(3):
            top_left = row + col
            top_right = row + col + 1
            bottom_left = 4 + top_left
            bottom_right = 4 + top_right

            # check if all 4 edges are present
            check_small_square = set([(top_left, top_right),
                                      (top_right, bottom_right),
                                      (top_left, bottom_left),
                                      (bottom_left, bottom_right)])
            pr('check_small_square')
            # pr('lines_set')
            if check_small_square <= lines_set:
                total += 1

    # check medium square
    if set([(1, 2), (2, 3), (3, 7), (7, 11),
            (9, 10), (10, 11), (1, 5), (5, 9)]) <= lines_set:
        total += 1
    if set([(3, 4), (2, 3), (4, 8), (8, 12),
            (11, 12), (10, 11), (2, 6), (6, 10)]) <= lines_set:
        total += 1
    if set([(5, 6), (6, 7), (7, 11), (11, 15),
            (13, 14), (14, 15), (9, 13), (5, 9)]) <= lines_set:
        total += 1
    if set([(6, 7), (7, 8), (8, 12), (12, 16),
            (14, 15), (15, 16), (6, 10), (10, 14)]) <= lines_set:
        total += 1

    # check large square
    if set([(1, 2), (2, 3), (3, 4),
            (4, 8), (8, 12), (12, 16),
            (13, 14), (14, 15), (15, 16),
            (1, 5), (5, 9), (9, 13)]) <= lines_set:
        total += 1
    return total

def test():
    testeql(checkio([[1, 2], [2, 6], [5, 6], [1, 5]]), 1)
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
