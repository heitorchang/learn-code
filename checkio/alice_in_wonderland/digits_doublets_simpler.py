from collections import defaultdict
from heapq import heappop, heappush

def min_bfs(edges, start, destination):
    """Renamed variables for better understanding
    Using algorithm found here (claims to be Dijkstra, but more likely
    it is merely BFS with a priority queue where heap[0] is smallest)
    https://gist.github.com/kachayev/5990802
    """
    
    graph = defaultdict(list)
    for source, sink, cost in edges:
        graph[source].append((cost, sink))

    heap = [(0, start, ())]  # cost, start, path
    seen = set()

    while heap:
        cost, current_vertex, path = heappop(heap)
        if current_vertex not in seen:
            seen.add(current_vertex)
            # path.append(current_vertex)  # list requires a shallow copy 
            path += (current_vertex,)  # add to end of tuple
            if current_vertex == destination:
                return (cost, path)

            for (edge_cost, neighbor) in graph.get(current_vertex, ()):
                if neighbor not in seen:
                    heappush(heap, (cost+edge_cost, neighbor, path))
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
    
    """
    edges = []
    for n in numbers:
        for m in numbers:
            if hasEdge(n, m):
                edges.append((n, m, 1))
    cost, path = min_bfs(edges, numbers[0], numbers[-1])
    return list(path)

def test():    
    testeql(hasEdge(911, 912), True)
    testeql(hasEdge(900, 923), False)
    
    
    testeql(checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]), [123, 121, 921, 991, 999])
    testeql(checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]), [111, 121, 127, 727, 777])
    testeql(checkio([456, 455, 454, 356, 656, 654]), [456, 454, 654])

