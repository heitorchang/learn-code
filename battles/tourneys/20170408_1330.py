def test():
    testeql(addDigits(13), 4)
    testeql(digitalSumSort([13,20,7,4]), [20,4,13,7])

def addDigits(n):
    return sum(map(int, list(str(n))))

def digitalSumSort(a):
    temp_res = []
    for n in a:
        temp_res.append((addDigits(n), n))
    s = sorted(temp_res)
    answer = []
    for n in s:
        answer.append(n[1])
    return answer

def chessKnight(cell):
    row = ord(cell) - ord('0')
    column = ord(cell[0]) - ord('a') + 1
    steps = [
            [-2, -1], [-1, -2], [1, -2], [2, -1],
            [2, 1], [1, 2], [-1, 2], [-2, 1]
            ]
    answer = 0

    for i in range(len(steps)):
        tmpRow = row + steps[i][0]
        tmpColumn = column + steps[i][1]
        print(tmpRow, tmpColumn)
        if (tmpRow >= 1 and tmpRow <= 8 and
            tmpColumn >= 1 and tmpColumn <= 8):
            answer += 1

    return answer
