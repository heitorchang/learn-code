description = """
Given the adjacency matrix of an undirected graph with no loops or multiple edges, find the size of the connected component of vertex 1 (0-based).

Example

For

matrix = [[false, true, false],
          [true, false, false],
          [false, false, false]]

the output should be
bfsComponentSize(matrix) = 2.
"""

from collections import deque

def bfsComponentSize(matrix):
    visited = set()
    q = deque()

    # the problem definition asks to start with index 1
    q.append(1)
    visited.add(1)
    
    size = 1
    
    while q:
        curnode = q.popleft()
        for i, connected in enumerate(matrix[curnode]):
            if connected and i not in visited:
                visited.add(i)
                q.append(i)
                size += 1
    return size


def test():
    true = True
    false = False
    testeql(bfsComponentSize([[false,true,false], 
                              [true,false,false], 
                              [false,false,false]]), 2)
    testeql(bfsComponentSize([[false,false,true,false], 
                              [false,false,false,false], 
                              [true,false,false,true], 
                              [false,false,true,false]]), 1)
    testeql(bfsComponentSize([[false,false,false], 
                              [false,false,false], 
                              [false,false,false]]), 1)
    testeql(bfsComponentSize([[false,true,true], 
                              [true,false,false], 
                              [true,true,false]]), 3)
    
