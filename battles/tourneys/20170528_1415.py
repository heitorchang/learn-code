def alternatingSums(a):
    a1 = 0
    a2 = 0
    for i in range(0, len(a), 2):
        a1 += a[i]
    for i in range(1, len(a), 2):
        a2 += a[i]
    return [a1, a2]


def test():

    testeql(alternatingSums([50, 60, 60, 45, 70]), [180, 105])
