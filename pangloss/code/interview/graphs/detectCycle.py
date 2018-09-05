# undirected graph

# Number of nodes
# Edges

# 0 -> 1 -> 2 -> 0
GRAPH1 = """
3
0 1
1 2
2 0
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
1 5
4 5
3 4
1 3
1 2
"""

def buildAdjMatrix(s):
    lines = filter(lambda line: len(line.strip()) > 0, s.split("\n"))
    nodes = int(next(lines))
    m = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for edgeStr in lines:
        ends = list(map(int, edgeStr.split()))
        m[ends[0]][ends[1]] = m[ends[1]][ends[0]] = 1
    return m

def isCyclic(m):
    visited = set()
    found = False
   
    def isCyclicStep(v, parent):
        nonlocal found
        
        if found:
            return
        visited.add(v)
        for vertex, connected in enumerate(m[v]):
            if connected and vertex in visited and vertex != parent:
                found = True
            if connected and not vertex in visited:
                isCyclicStep(vertex, v)

    for i in range(len(m)):
        if not i in visited:
            isCyclicStep(i, i)
        if found:
            break
    return found

def test():
    # testeql(buildAdjMatrix(GRAPH1), [[0, 1, 0, 0, 0],
    #                                [1, 0, 1, 0, 0],
    #                                [0, 1, 0, 0, 0],
    #                                [0, 0, 0, 0, 1],
    #                                [0, 0, 0, 1, 0]])

    testeql(isCyclic(buildAdjMatrix(GRAPH1)), True)
    testeql(isCyclic(buildAdjMatrix(GRAPH2)), False)
    testeql(isCyclic(buildAdjMatrix(GRAPH3)), True)
    
