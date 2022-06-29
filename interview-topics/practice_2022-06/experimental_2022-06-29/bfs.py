from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while len(queue) > 0:
        current = queue.popleft()
        print("visiting", current)
        for v in graph[current]:
            if v not in visited:
                queue.append(v)
                visited.add(v)


def dfs(graph, start):
    stack = [start]
    visited = set([start])
    while len(stack) > 0:
        current = stack.pop()
        print("visiting", current)
        for v in graph[current]:
            if v not in visited:
                stack.append(v)
                visited.add(v)


def test_bfs():
    graph = {
        0: [2],
        1: [3, 4, 5],
        2: [3],
        3: [0],
        4: [0],
        5: [1],
    }
    bfs(graph, 1)


def test_dfs():
    graph = {
        0: [2],
        1: [3, 4, 5],
        2: [3],
        3: [0],
        4: [0],
        5: [1],
    }
    dfs(graph, 1)
