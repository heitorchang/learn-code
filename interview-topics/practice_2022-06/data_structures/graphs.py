from collections import deque

class Graph:
    adj = {}

    def __init__(self, vertices):
        for v in vertices:
            self.adj[v] = []

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def v(self):
        return len(self.adj)

    def __str__(self):
        return str(self.adj)


def bfsConnectedComponent(G, v):
    queue = deque([v])
    visited = set()
    component = set()

    while len(queue) > 0:
        current = queue.popleft()
        print(current)
        visited.add(current)
        component.add(current)
        for v in G.adj[current]:
            if v not in visited:
                queue.append(v)

    return component


def test_bfs():
    graph = Graph([1, 2, 3, 4, 5, 6])
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(2, 4)
    graph.addEdge(3, 4)
    graph.addEdge(5, 6)

    print(bfsConnectedComponent(graph, 1))


def dfsConnectedComponent(G, v):
    stack = [v]
    visited = set()
    component = set()

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        visited.add(current)
        component.add(current)
        for v in G.adj[current]:
            if v not in visited:
                stack.append(v)

    return component


def test_dfs():
    graph = Graph([1, 2, 3, 4, 5, 6])
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(2, 4)
    graph.addEdge(3, 4)
    graph.addEdge(5, 6)

    print(dfsConnectedComponent(graph, 1))
