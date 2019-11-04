desc = """
A tournament is a directed graph in which every pair of distinct vertices is connected by a single directed edge.

Determine if the graph with edges fromV -> toV is a tournament.
"""

def isTournament(n, fromV, toV):
    edges = {}
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            edges[(i, j)] = False
    for a, b in zip(fromV, toV):
        if a == b:
            return False
        c = tuple(sorted([a, b]))
        if edges[c]: 
            # already seen, tournament cannot repeat
            return False
        edges[c] = True
    return all(edges[k] for k in edges)
