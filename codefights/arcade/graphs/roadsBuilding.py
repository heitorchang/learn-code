def roadsBuilding(cities, roads):
    grid = [[False for c in range(cities)] for r in range(cities)]

    for road in roads:
        if road[0] > road[1]:
            grid[road[1]][road[0]] = True
        else:
            grid[road[0]][road[1]] = True

    toBuild = []
    for i in range(cities):
        for j in range(i+1, cities):
            if not grid[i][j]:
                toBuild.append([i, j])
    return toBuild

def test():
    testeql(roadsBuilding(4, [[0,1], [1,2], [2,0]]), [[0,3], 
                                                      [1,3], 
                                                      [2,3]])
