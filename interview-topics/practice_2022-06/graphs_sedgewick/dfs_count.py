def count(G, start):
    ct = 0
    def dfs(v):
        nonlocal ct
        marked[v] = True
        ct += 1
        print("visiting", v)
        for w in G[v]:
            if not marked[w]:
                dfs(w)

    marked = [False] * len(G)
    dfs(start)
    return ct


graph = [
    [1, 2, 3, 4], # 0
    [2, 3], # 1
    [3], # 2
    [],  # 3
    [1], # 4
    [6], # 5
    []   # 6
]

print(count(graph, 5))
