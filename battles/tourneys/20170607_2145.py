def symbolsPermutation(word1, word2):
    a = sorted(list(word1))
    b = sorted(list(word2))
    return a == b

def fileNaming(names):
    def calculateHash(inputString):
        P = 997
        M = 28001
        hashValue = 0
        for i in range(len(inputString)):
            hashValue = (hashValue * P + ord(inputString[i])) % M
        return hashValue

    hashMapSize = len(names) * 2
    ##
    #     Information about the string in the hash map
    #     is stored in the following way:
    #     [string itself,
    #      its hash,
    #      the smallest possible integer to use with this name]
    ##
    hashMap = []
    result = []

    def searchHM(position, hashValue):
        while (hashMap[position][0] != ''
          and hashMap[position][1] != hashValue):
            position = (position + 1) % hashMapSize
        return position

    for i in range(hashMapSize):
        hashMap.append(['', -1, 0])

    for i in range(len(names)):
        hashValue = calculateHash(names[i])
        startPos = searchHM(hashValue % hashMapSize, hashValue)
        if hashMap[startPos][0] == '':
            hashMap[startPos] = [names[i], hashValue, 1]
            result.append(names[i])
        else:
            newName = names[i] + '(' + str(hashMap[startPos][2]) + ')'
            newNameHash = calculateHash(newName)
            position = searchHM(newNameHash % hashMapSize, newNameHash)

            while hashMap[position][0] != '':
                hashMap[startPos][2] += 1
                newName = names[i] + '(' + str(hashMap[startPos][2]) + ')'
                newNameHash = calculateHash(newName)
                position = searchHM(newNameHash % hashMapSize, newNameHash)
            hashMap[position] = [newName, newNameHash, 1]
            result.append(newName)
            hashMap[startPos][2] += 1

    return result

    

def chessKnightMoves(cell):

    def isValid(pos):
        if 0 <= pos and pos < 8:
            return True
        return False

    def getX(pos):
        return ord(pos) - ord('a')

    def getY(pos):
        return ord(pos) - ord('1')

    current_x = getX(cell[0])
    current_y = getY(cell[1])
    result = 0

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx * dy) == 2:
                if isValid(current_x + dx) and isValid(current_y + dy):
                    result += 1
    return result

def parkingCost(timeIn, timeOut):
    diff = (int(timeOut[:2]) * 60 +
        int(timeOut[3:]) -
        int(timeIn[:2]) * 60 -
        int(timeIn[3:]))
    if diff <= 30:
        return 0
    if diff <= 120:
        pr('diff')
        return (diff - 21) // 10
    return 9 + ((diff - 111) // 10) * 2


def test():
    # testeql(fileNaming(["doc", "doc"]), ["doc", "doc(1)"])
    testeql(chessKnightMoves('a1'), 2)
    testeql(parkingCost("08:23", "08:54"), 1)
