
def trapRooms(museum):
    visited = []
    answer = []
    trapsNumber = 0
    componentSize = [0]
 
    def dfs(x, y):
        if (x < 0 or x >= len(museum) or
            y < 0 or y >= len(museum[0])):
            return True
        if visited[x][y]:
            return answer[x][y]
        visited[x][y] = True
        componentSize[0] += 1
        if museum[x][y] == 'L':
            answer[x][y] = dfs(x, y - 1)
        elif museum[x][y] == 'U':
            answer[x][y] = dfs(x - 1, y)
        elif museum[x][y] == 'R':
            answer[x][y] = dfs(x, y + 1)
        elif museum[x][y] == 'D':
            answer[x][y] = dfs(x + 1, y)
        pr('visited[x][y]')
        return visited[x][y]

    answer = [[False for j in range(len(museum[0]))]
      for i in range(len(museum))]
    visited = [[False for j in range(len(museum[0]))]
      for i in range(len(museum))]

    for i in range(len(museum)):
        for j in range(len(museum[0])):
            if not visited[i][j]:
                print('not visited')
                pr('componentSize')
                pr('dfs')
                componentSize[0] = 0
                if not dfs(i, j):
                    trapsNumber += componentSize[0]
    return trapsNumber


def test():
    testeql(trapRooms([["U","L"], 
 ["R","L"]]), 2)
