def arithmeticProgression(element1, element2, n):
    diff = element2 - element1
    return element1 + (n-1) * diff

def knapsackLight(value1, weight1, value2, weight2, maxW):

    if weight1 + weight2 <= maxW:
        return value1 + value2
    if min(weight1, weight2) > maxW:
        return 0
    if weight1 <= maxW and (value1 >= value2 or weight2 > maxW):
        return value1
    return value2

def countNeighbouringPairs(inputString):
    pairs = 0
    cur = None
    for c in inputString:
        if c == cur:
            pairs += 1
        cur = c
    return pairs

def coolString(inputString):
    if not all([c.isalpha() for c in list(inputString)]):
        return False
    curState = inputString[0].islower()
    for i in range(1, len(inputString)):
        newState = inputString[i].islower()
        if newState == curState:
            return False
        curState = newState
    return True

def dfsComponentSize(matrix, vertex):
    # does not pass
    def dfs(currentVertex, visited):
        visited[currentVertex] = True
        componentSize = 1
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                return dfs(nextVertex, visited)
        return componentSize

    visited = []

    for i in range(len(matrix)):
        visited.append(False)

    componentSize = dfs(vertex, visited)

    return componentSize

    
def test():
    testeql(arithmeticProgression(3,2,4), 0)
    testeql(arithmeticProgression(2,2,100), 2)

    testeql(coolString("aAaAaAa"), True)
