from collections import deque

# G = (V, E)

graph = {
    0: [1, 3],
    1: [0, 6],
    2: [4, 5],
    3: [0, 4],
    4: [2, 3, 5],
    5: [2, 4],
    6: [1]
}

def bfs(G, start):
    queue = deque([start])
    visited = set([start])

    while len(queue) > 0:
        cur = queue.popleft()
        print("processing", cur)
        for v in G[cur]:
            if v not in visited:
                visited.add(v) # marking visited here avoids duplicates when a vertex can be reached from multiple sources
                queue.append(v)


# bfs(graph, 0)


def dfs(G, start):
    stack = [start]
    visited = set([start])

    while len(stack) > 0:
        cur = stack.pop()
        print("processing", cur)
        for v in G[cur]:
            if v not in visited:
                visited.add(v) # marking visited here avoids duplicates when a vertex can be reached from multiple sources
                stack.append(v)


dfs(graph, 0)
