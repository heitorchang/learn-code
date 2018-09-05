# undirected graph

# Number of nodes
# Edges

GRAPH1 = """
5
0 1
0 2
1 3
1 4
"""

GRAPH2 = """
7
0 2
0 1
2 3
2 4
4 5
1 6
"""

GRAPH3 = """
6
0 1
1 3
0 4
0 2
3 5
"""

def buildAdjMatrix(s):
    lines = filter(lambda line: len(line.strip()) > 0, s.split("\n"))
    nodes = int(next(lines))
    m = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for edgeStr in lines:
        ends = list(map(int, edgeStr.split()))
        m[ends[0]][ends[1]] = m[ends[1]][ends[0]] = 1
    return m

def dfsIterative(m, start):
    """Given an adjacency matrix and starting node,
    traverse the graph"""
    
    s = [start]  # list, use as stack
    visited = {start}  # set
    out = []
    
    while len(s) > 0:
        cur = s.pop()
        pr('cur')
        out.append(cur)
            
        for vertex, connected in enumerate(m[cur]):
            # vertex is column in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                s.append(vertex)
                visited.add(vertex)
    return out

def dfsRecursive(m, start):
    visited = set()
    out = []
    def dfsRecursiveStep(start):
        visited.add(start)
        out.append(start)
        for vertex, connected in enumerate(m[start]):
            # vertex is column in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                dfsRecursiveStep(vertex)
    dfsRecursiveStep(start)
    return out
            
def test():
    # testeql(buildAdjMatrix(GRAPH1), [[0, 1, 0, 0, 0],
    #                                [1, 0, 1, 0, 0],
    #                                [0, 1, 0, 0, 0],
    #                                [0, 0, 0, 0, 1],
    #                                [0, 0, 0, 1, 0]])

    testeql(dfsIterative(buildAdjMatrix(GRAPH2), 0), [0,2,4,5,3,1,6])
    testeql(dfsRecursive(buildAdjMatrix(GRAPH1), 0), [0,1,3,4,2])
