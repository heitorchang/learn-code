from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(edges, start, destination):
    graph = defaultdict(list)
    for source, sink, cost in edges:
        graph[source].append((cost, sink))

    q = [(0, start, ())]
    seen = set()

    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == destination:
                path_list = []
                while path[1]:
                    path_list.append(path[0])
                    path = path[1]
                path_list.append(start)
                return path_list[::-1]
                # return (cost, path)

            for c, v2 in graph.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))
    return float('inf')

def hasEdge(n, m):
    """If n and m differ in only one digit, there is an edge"""
    str_n = str(n)
    str_m = str(m)
    diffs = sum([a != b for (a, b) in zip(str_n, str_m)])
    return diffs == 1
    
def checkio(numbers):
    """
    Idea: build an undirected graph and run a pathfinding algorithm
    
    Using this implementation of Dijkstra's algorithm
    https://gist.github.com/kachayev/5990802
    """
    edges = []
    for n in numbers:
        for m in numbers:
            if hasEdge(n, m):
                edges.append((n, m, 1))
    return dijkstra(edges, numbers[0], numbers[-1])

def test():
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]
    
    testeql(hasEdge(911, 912), True)
    testeql(hasEdge(900, 923), False)
    
    
    testeql(checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]), [123, 121, 921, 991, 999])
    testeql(checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]), [111, 121, 127, 727, 777])
    testeql(checkio([456, 455, 454, 356, 656, 654]), [456, 454, 654])

