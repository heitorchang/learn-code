def leftover(s):
    u = s.upper()
    su = sum(map(ord, u))
    return sum(map(ord, s)) % su

def trymod(a, c):
    solutions = []
    for i in range(2, a):
        if a % i == c:
            solutions.append(i)
    return solutions


def test():
    testeql(leftover("antidisestablishmentarianism"), 27)
    testeql(leftover("supercalifragilisticexpialidocious"), 27)
    testeql(leftover("appetite"), 4)
    testeql(leftover("hello"), 2)
    testeql(leftover("cb"), 1)
    testeql(leftover("2017"), 2)
    testeql(leftover("watcher"), 1)
