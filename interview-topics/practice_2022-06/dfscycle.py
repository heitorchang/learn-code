# Detect cycle in a directed graph

def solution(G):
    def iscyclic(v):
        visited[v] = True
        stack[v] = True
        for neighbor in G[v]:
            if not visited[neighbor]:
                if iscyclic(neighbor):
                    return True
            if stack[neighbor]:
                return True
        stack[v] = False
        return False

    V = len(G)
    visited = [False] * V
    stack = [False] * V
    for node in range(V):
        if not visited[node]:
            if iscyclic(node):
                return True
    return False


g = [[1],
 [2],
 [3,4],
 [4],
 [0]]

print(solution(g))

g2 = [[1,2,3],
 [2,3],
 [3],
 []]

print(solution(g2))
