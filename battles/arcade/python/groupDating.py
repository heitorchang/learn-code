def groupDating(male, female):
    # http://stackoverflow.com/questions/6473679/transpose-list-of-lists
    # return list(map(list, zip(*filter(lambda t: t[0] != t[1], zip(male,female)))))
    return ([[m for (i, m) in enumerate(male) if male[i] != female[i]], [f for (i, f) in enumerate(female) if male[i] != female[i]]])

def test():
    testeql(groupDating([5, 28, 14, 99, 17], [5, 14, 28, 99, 16]), [[28, 14, 17], [14, 28, 16]])
    testeql(groupDating([1,2,3],[1,2,3]), [[], []])
