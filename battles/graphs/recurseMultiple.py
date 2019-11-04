# given an adjacency matrix, count how many nodes are connected to
# a given node, including itself

#  (0)   (3)
# / | \
# 1 2 4
#     !
#     5

F = False
T = True

adj = [[F, T, T, F, T, F],
       [T, F, F, F, F, F],
       [T, F, F, F, F, F],
       [F, F, F, F, F, F],
       [T, F, F, F, F, T],
       [F, F, F, F, T, F]]


# 0-1-2 3-4

#        0  1  2  3  4
adj2 = [[F, T, F, F, F],
        [T, F, T, F, F],
        [F, T, F, F, F],
        [F, F, F, F, T],
        [F, F, F, T, F]]

#        0  1  2  3  4
adj3 = [[F, T, F, F, F],
        [T, F, T, F, F],
        [F, T, F, T, F],
        [F, F, T, F, T],
        [F, F, F, T, F]]

# m = matrix
# v = vertex
# ct = count

def traverse(m, v, visited):
    # if there are no possible paths, return ct
    validPaths = []
    for i in range(len(m[v])):
        if m[v][i] == True and i not in visited:
            validPaths.append(i)
    if not validPaths:
        # print("no more paths", v)
        return 1
    ct = 1
    for p in validPaths:
        ct += traverse(m, p, visited + [v])
    return ct

def countNodes(m, v):
    return traverse(m, v, [])

def test():
    testeql(countNodes(adj, 0), 5)
    testeql(countNodes(adj2, 0), 3)
    testeql(countNodes(adj2, 3), 2)
    testeql(countNodes(adj3, 2), 5)
    
