def caesarBoxCipherEncoding(inputString):
    lines = round(len(inputString) ** 0.5)
    c = [[] for _ in range(lines)]

    for i in range(lines):
        c[i] = inputString[i*lines:i*lines+lines]

    result = ""
    for i in range(lines):
        for j in range(lines):
            result += c[j][i]
    return result
    # testeql(caesarBoxCipherEncoding("sixteenletters16"), "seerietsxnt1tle6")

def prefixFunctionNaive(s):
    P = [0]
    for i in range(1, len(s) + 1):
        for j in range(len(s), 0, -1):
            if s[j] = s[i - len(s) + j + 1]:
                P[i] = 0

    # phail
    return 0

def crossingSum(matrix, a, b):
    rowSum = sum(matrix[a])
    colSum = 0
    for r in range(len(matrix)):
        colSum += matrix[r][b]
    return rowSum + colSum - matrix[a][b]
    # PWNAGE

def arithmeticExpression(a, b, c):
    # 1415
    # add
    if a + b == c:
        return True
    if a - b == c:
        return True
    if a * b == c:
        return True
    if round(a/b) == c:
        return True
    return False

    
    
def test():
    pass
    
