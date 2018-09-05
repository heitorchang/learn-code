data = data.concat([

////////////////////////////////////////////////////////////
//
// GRAPHS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Graphs',
    title: 'Detect a cycle in an undirected graph',
    reference: 'https://algocoding.wordpress.com/2015/04/02/detecting-cycles-in-an-undirected-graph-with-dfs-python/',
    description: ``,
    code: `
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
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'Representation, Adjacency List',
    reference: '',
    description: `An adjacency list may be a list of lists or a dictionary, where the source (initial) vertex is the key and sink (terminal) vertices are stored in a corresponding list.`,
    code: `
adjLists = [[1, 2], [2, 3], [4], [4, 5], [5], []]

adjListsDict = {}
adjListsDict[0] = [1, 2]
adjListsDict[1] = [3]
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'Representation, Adjacency Matrix',
    reference: '',
    description: `The adjacency matrix is an n x n matrix with True or False values, where True represents an edge between the row-numbered vertex and the column-numbered vertex. An undirected graph is symmetric.<br><br>In the example below, the first line is the number of vertices and each subsequent line, an edge.`,
    code: `
GRAPH = """
3
0 1
1 2
2 0
"""

def buildAdjMatrix(s):
    lines = filter(lambda line: len(line.strip()) > 0, s.split("\n"))
    nodes = int(next(lines))
    m = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for edgeStr in lines:
        ends = list(map(int, edgeStr.split()))
        m[ends[0]][ends[1]] = m[ends[1]][ends[0]] = 1
    return m
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'BFS (Breadth-First Search)',
    reference: '',
    description: `<code>visited</code> is updated with a vertex at the same time as it's added to the queue in order to avoid it being added twice to the queue.`,
    code: `
from collections import deque
    
def bfsConnectedComponent(m, start):
    """Given an adjacency matrix and starting node, return the set
    of vertices connected to the starting node"""
    
    q = deque([start])  # queue, use append and popleft
    visited = {start}  # set
    component = []  # output
    
    while len(q) > 0:
        cur = q.popleft()
        component.append(cur)
            
        for vertex, connected in enumerate(m[cur]):
            # vertex is the column index in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                q.append(vertex)
                visited.add(vertex)        
    return component    
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'DFS (Depth-First Search), iterative',
    reference: 'https://www.hackerearth.com/pt-br/practice/algorithms/graphs/depth-first-search/tutorial/',
    description: `The difference between DFS and BFS is that DFS uses a stack (vertices encountered last are processed first), while BFS uses a queue (vertices encountered first as immediate neighbors are processed first)`,
    code: `
def dfsIterative(m, start):
    """Given an adjacency matrix and starting node,
    traverse the graph"""
    
    s = [start]  # list, use as stack
    visited = {start}  # set
    out = []
    
    while len(s) > 0:
        cur = s.pop()
        out.append(cur)
            
        for vertex, connected in enumerate(m[cur]):
            # vertex is column in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                s.append(vertex)
                visited.add(vertex)
    return out    
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'DFS (Depth-First Search), recursive',
    reference: 'https://www.hackerearth.com/pt-br/practice/algorithms/graphs/depth-first-search/tutorial/',
    description: ``,
    code: `
def dfsRecursive(m, start):
    visited = {start}  # set
    out = []
    def dfsRecursiveStep(start):
        out.append(start)
        for vertex, connected in enumerate(m[start]):
            # vertex is column in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                visited.add(vertex)
                dfsRecursiveStep(vertex)
    dfsRecursiveStep(start)
    return out

    `
  },


]);
