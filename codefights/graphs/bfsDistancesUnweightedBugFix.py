def bfsDistancesUnweightedGraph(matrix, startVertex):

    visited = []
    queue = []
    distance = []

    for i in range(len(matrix)):
        visited.append(False)
        distance.append(0)

    visited[startVertex] = True
    queue.append(startVertex)
    
    while len(queue) > 0:
        # print(queue)
        currentVertex = queue.pop(0)
        visited[currentVertex] = True
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] = True
                distance[nextVertex] = distance[currentVertex] + 1
                queue.append(nextVertex)

    return distance

false = False
true = True
test(bfsDistancesUnweightedGraph([[false,false,true], 
                                  [false,false,true], 
                                  [true,true,false]], 0), [0, 2, 1])

