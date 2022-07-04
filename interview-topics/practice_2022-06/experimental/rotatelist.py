def rotateleft(alist, n):
    # find first element of result
    # ex. f([1, 2, 3, 4, 5], 2) => 3
    return alist[n:] + alist[:n]


def rotateright(alist, n):
    # find first element of result
    # ex. f([1, 2, 3, 4, 5, 6], 2) => [5, 6, 1, 2, 3, 4]
    return alist[len(alist) - n:] + alist[:len(alist) - n]

# rotateleft with negative n has the same effect
