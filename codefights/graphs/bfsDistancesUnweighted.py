description = """
Given the adjacency matrix of the connected undirected graph with no loops or multiple edges and the index of the start vertex, find the distances between the start vertex and each vertex of the graph.

Example

For

matrix = [[false, false, true],
          [false, false, true],
          [true, true, false]]
and startVertex = 0, the output should be
bfsDistancesUnweightedGraph(matrix, startVertex) = [0, 2, 1].
"""

from collections import deque

def bfsDistancesUnweightedGraph(matrix, startVertex):
    q = deque()
    q.append(startVertex)
    
    visited = set()
    visited.add(startVertex)

    traveled = 0
    distances = [0] * len(matrix)
    
    while q:
        cur = q.popleft()
        # print(cur)
        traveled += 1
        
        for vertex, linked in enumerate(matrix[cur]):
            if linked and vertex not in visited:
                # print('v', vertex, traveled)
                visited.add(vertex)
                q.append(vertex)
                distances[vertex] = traveled

    return distances

def test():
    false = False
    true = True

    testeql(bfsDistancesUnweightedGraph([[false,false,true], 
 [false,false,true], 
 [true,true,false]], 0), [0,2,1])

    
    testeql(bfsDistancesUnweightedGraph([[false,true,false,false], 
 [true,false,true,true], 
 [false,true,false,true], 
 [false,true,true,false]], 3), [2,1,1,0])
    testeql(bfsDistancesUnweightedGraph([[false,true,true], 
 [true,false,false], 
 [true,false,false]], 0), [0, 1,1])


    testeql(bfsDistancesUnweightedGraph( [[false,true,false,false,false,false,false,false], 
 [true,false,true,false,false,false,false,false], 
 [false,true,false,true,false,false,false,false], 
 [false,false,true,false,true,false,false,false], 
 [false,false,false,true,false,true,false,false], 
 [false,false,false,false,true,false,true,false], 
 [false,false,false,false,false,true,false,true], 
 [false,false,false,false,false,false,true,false]], 7), [7, 6, 5, 4, 3, 2, 1, 0])
