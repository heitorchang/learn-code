
def strangeCode(s, e):
    out = ""
    lastProduced = "b"

    while True:
        if s >= e - 1:
            return out
        s += 1
        e -= 1
        if lastProduced == "b":
            out += "a"
            lastProduced = "a"
        else:
            out += "b"
            lastProduced = "b"
    return out

def binaryGenerator(s):
    n = int(s, 2)
    limit = 2 ** len(s)
    out = []
    for i in range(limit):
        if i & n == n:
            out.append(bin(i)[2:].zfill(len(s)))
    return sorted(out)

def digitCharactersSum(ch1, ch2):
    x1 = ord(ch1) - ord('0')
    x2 = ord(ch2) - ord('0')
    if x1 + x2 < 10:
        return chr(x1 + x2 + ord('0'))
    else:
        return '1' + chr(ord('0') + (x1 + x2) % 10)


def tennisSet(score1, score2):
    scs = sorted([score1, score2])
    if scs[1] > 7:
        return False
    if scs[1] == 7:
        if scs[0] == 5 or scs[0] == 6:
            return True
        else:
            return False
    if scs[1] == 6:
        if scs[0] == 5:
            return False
        else:
            return True
    return False

def stringsCrossover(inputArray, result):
    # passed bugfix
    answer = 0

    for i in range(len(inputArray)):
        for j in range(i + 1, len(inputArray)):
            correct = True
            for k in range(len(result)):
                if (result[k] != inputArray[i][k]
                  and result[k] != inputArray[j][k]):
                    correct = False
                    break
            if correct:
                answer += 1
    return answer

def runLengthEncoding(inputString):

    repeatLength = 1
    answer = []
    for i in range(1, len(inputString)):
        if inputString[i] != inputString[i - 1]:
            answer.append(str(repeatLength))
            answer.append(inputString[i - 1])
            repeatLength = 1
        else:
            repeatLength += 1
    answer.append(str(repeatLength))
    answer.append(inputString[len(inputString) - 1])
    return ''.join(answer)


def capitalizeVowelsRegExp(input):
    out = ""
    v = {'a': 'A',
         'e': 'E',
         'i': 'I',
         'o': 'O',
         'u': 'U',
         'y': 'Y'}
    for c in input:
        try:
            out += v[c]
        except KeyError:
            out += c
    return out


def specialNumbers(l, r):

    ans = 0
    for i in range(l, r + 1):
        digits = str(i)
        ok = True
        for j in range((len(digits) + 1) // 2):
            if digits[j] == '6' or digits[j] == '9':
                ok &= ord(digits[len(digits) - 1 - j]) == ord('9') - ord(digits[j]) + ord('6')
            elif digits[j] == '8' or digits[j] == '0':
                ok &= digits[j] == digits[len(digits) - 1 - j]
            else:
                ok = False
        if ok:
            ans += 1

    return ans

def bfsComponentSize(matrix):
    visited = [False for i in range(len(matrix))]
    queue = []
    componentSize = 0

    visited[1] = True
    queue.append(1)
    while len(queue) > 0:
        currentVertex = queue.pop()
        visited[currentVertex] = True
        componentSize += 1
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] = True
                queue.append(nextVertex)

    return componentSize


def test():
    # testeql(strangeCode(4, 8), "ab")

    # testeql(binaryGenerator("01101"), ["01101", "01111", "11101", "11111"])
    # testeql(digitCharactersSum('2', '5'), '7')
    # testeql(stringsCrossover(["aa", "ab", "ba"], "bb"), 1)

    # testeql(runLengthEncoding("abbaaaac"), "1a2b4a1c")
