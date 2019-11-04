from itertools import permutations

def niceFractions(n):
    total = 0
    for p in permutations('1234567890', 5):
        a = int("".join(p))
        if len(str(n * a)) == 5 and len(set(str(n*a)) - set(str(a))) == 5:
            print(n*a, a)
            total += 1
    return total

def tennisGamePoints(score):
    mid = score.find('-')
    parseScore = (score[:mid], score[mid + 1:])
    scores = ['love', 'all', '15', '30', '40']
    if parseScore[0] == 'all':
        return scores.index(parseScore[0]) * 2
    return scores.index(parseScore[0]) + scores.index(parseScore[1])


def test():
    testeql(niceFractions(22), 1)
