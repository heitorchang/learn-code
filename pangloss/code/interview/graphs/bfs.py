# undirected graph

# Number of nodes
# Edges

GRAPH1 = """
5
0 1
1 2
3 4
"""

GRAPH2 = """
5
0 1
0 2
0 3
1 3
1 4
"""

GRAPH3 = """
6
0 1
1 3
0 4
0 2
3 5
"""

GRAPH4 = """
7
0 2
0 1
2 3
2 4
4 5
1 6
"""

from collections import deque

def buildAdjMatrix(s):
    lines = filter(lambda line: len(line.strip()) > 0, s.split("\n"))
    nodes = int(next(lines))
    m = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for edgeStr in lines:
        ends = list(map(int, edgeStr.split()))
        m[ends[0]][ends[1]] = m[ends[1]][ends[0]] = 1
    return m

def bfsConnectedComponent(m, start):
    """Given an adjacency matrix and starting node, return the set
    of vertices connected to the starting node"""
    
    q = deque([start])  # queue, use append and popleft
    
    visited = {start}  # set
        
    component = []  # output
    
    while len(q) > 0:
        cur = q.popleft()
        component.append(cur)
        # print(cur)
        
        for vertex, connected in enumerate(m[cur]):
            # vertex is column in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                q.append(vertex)
                visited.add(vertex)

                # pr('q')
                # pr('visited')
        
    return component
    
def test():
    # testeql(buildAdjMatrix(GRAPH1), [[0, 1, 0, 0, 0],
    #                                [1, 0, 1, 0, 0],
    #                                [0, 1, 0, 0, 0],
    #                                [0, 0, 0, 0, 1],
    #                                [0, 0, 0, 1, 0]])

    testeql(bfsConnectedComponent(buildAdjMatrix(GRAPH2), 0), [0, 1, 2, 3, 4])

    testeql(bfsConnectedComponent(buildAdjMatrix(GRAPH3), 0), [0, 1, 2, 4, 3, 5])
    testeql(bfsConnectedComponent(buildAdjMatrix(GRAPH4), 0), [0, 1, 2, 6, 3, 4, 5])
