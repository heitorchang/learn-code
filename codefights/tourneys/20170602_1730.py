
def fixedPointsPermutation(permutation):
    s = range(1, len(permutation)+1)
    total = 0
    for i in range(len(permutation)):
        if s[i] == permutation[i]:
            total += 1
    return total


def findPath(matrix):

    positionX = -1
    positionY = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # insert code here
            
    for i in range(1, len(matrix) * len(matrix[0])):
        found = False
        nextX = -1
        nextY = -1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx * dy == 0:
                    if (positionX + dx >= 0 and positionX + dx < len(matrix)
                    and positionY + dy >= 0 and positionY + dy < len(matrix[0])):
                        if matrix[positionX + dx][positionY + dy] == i + 1:
                            found = True
                            nextX = positionX + dx
                            nextY = positionY + dy
        if found:
            positionX = nextX
            positionY = nextY
        else:
            return False
    return True

def test():
    testeql(findPath([[1,4,5], [2,3,6]]), True)
