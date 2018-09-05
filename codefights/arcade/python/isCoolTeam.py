def letterIdx(letter):
    return ord(letter) - 97

def buildDirectedMatrix(names):
    #   A B C D E
    # A 0 0 0 0 1
    # B 0 2 0 0 1
    # C ...
    # Bob, Bab, Ace and Bale
    
    m = [[0 for _ in range(26)] for _ in range(26)]
    for name in names:
        name = name.lower()
        m[letterIdx(name[0])][letterIdx(name[-1])] += 1
    return m

def printMatrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end="")
        print()

def countStartsAndEnds(names):
    listStarts = [0 for _ in range(26)]
    listEnds = [0 for _ in range(26)]
    for name in names:
        name = name.lower()
        listStarts[letterIdx(name[0])] += 1
        listEnds[letterIdx(name[-1])] += 1
    return (listStarts, listEnds)

def listDiff(ls, le):
    diff = [0 for _ in range(26)]
    for i in range(26):
        diff[i] = ls[i] - le[i]
    return diff

def checkValid(lst):
    one = lst.count(1)
    negOne = lst.count(-1)
    zeros = lst.count(0)
    if zeros == 24 and one == 1 and negOne == 1:
        return True
    return False

class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        def letterIdx(letter):
            return ord(letter) - 97

        def countStartsAndEnds(names):
            listStarts = [0 for _ in range(26)]
            listEnds = [0 for _ in range(26)]
            for name in names:
                name = name.lower()
                listStarts[letterIdx(name[0])] += 1
                listEnds[letterIdx(name[-1])] += 1
            return (listStarts, listEnds)

        def listDiff(ls, le):
            diff = [0 for _ in range(26)]
            for i in range(26):
                diff[i] = ls[i] - le[i]
            return diff

        def checkValid(lst):
            one = lst.count(1)
            negOne = lst.count(-1)
            zeros = lst.count(0)
            if (zeros == 24 and one == 1 and negOne == 1) or (zeros == 26 and one == 0 and negOne == 0):
                return True
            return False

        ls, le = countStartsAndEnds(self.names)
        d = listDiff(ls, le)
        return checkValid(d)

    def testTeam(self):
        # m = buildDirectedMatrix(self.names)
        # printMatrix(m)
        ls, le = countStartsAndEnds(self.names)
        d = listDiff(ls, le)
        return checkValid(d)
        
def isCoolTeam(team):
    return bool(Team(team))
    # return Team(team).testTeam()
    
def test():
    testeql(isCoolTeam(["Bob", 
 "Bobby", 
 "Billy"]), False)

    testeql(isCoolTeam(["Mark", 
 "Kelly", 
 "Kurt", 
 "Terk"]), True)

    testeql(isCoolTeam(["Ana", "Ada"]), True)
