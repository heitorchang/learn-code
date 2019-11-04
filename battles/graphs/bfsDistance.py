def bfsDistancesUnweightedGraph2(matrix, vertex1, vertex2):
    # copyfights, totally teh cheatz
    
    visited = []
    queue = []
    distance = []

    for i in range(len(matrix)):
        visited.append(False)
        distance.append(0)

    visited[vertex1] = True
    queue.append(vertex1)
    while len(queue) > 0:
        currentVertex = queue[0]
        queue = queue[1:]
        visited[currentVertex] = True
        for nextVertex in range(len(matrix)):
            if matrix[currentVertex][nextVertex] and not visited[nextVertex]:
                visited[nextVertex] = True
                distance[nextVertex] = distance[currentVertex] + 1
                queue.append(nextVertex)

    return  distance[vertex2]

def test():
    false = False
    true = True
    
    testeql(bfsDistancesUnweightedGraph2([[false,false,true], 
 [false,false,true], 
 [true,true,false]], 0, 1), 2)

    testeql(bfsDistancesUnweightedGraph2([[false,false,true], 
 [false,false,true], 
 [true,true,false]], 1, 0), 2)

    testeql(bfsDistancesUnweightedGraph2([[false,true,false,false], 
 [true,false,true,true], 
 [false,true,false,true], 
 [false,true,true,false]], 2, 0), 2)
