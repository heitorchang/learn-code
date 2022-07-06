# https://pythonalgos.com/dijkstras-algorithm-in-5-steps-with-python/

import heapq

# create our graph using an adjacency list representation
# each "node" in our list should be a node name and a distance
graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}

graph_pyds3 = {
    0: [(1, 2), (2, 1), (3, 5)],
    1: [(0, 2), (2, 2), (3, 3)],
    2: [(0, 1), (1, 2), (3, 3), (4, 1)],
    3: [(1, 3), (0, 5), (2, 3), (4, 1), (5, 5)],
    4: [(2, 1), (3, 1), (5, 1)],
    5: [(3, 5), (4, 1)]
}


def lazy_dijkstras(graph, root):
    n = len(graph)
    # set up "inf" distances
    dist = [float('inf') for _ in range(n)]
    # set up root distance
    dist[root] = 0
    # set up visited node list
    visited = [False for _ in range(n)]
    # set up priority queue
    pq = [(0, root)]
    # while there are nodes to process
    while len(pq) > 0:
        # get the root, discard current distance
        _, u = heapq.heappop(pq)
        # if the node is visited, skip
        if visited[u]:
            continue
        # set the node to visited
        visited[u] = True
        # check the distance and node and distance
        for v, l in graph[u]:
            # if the current node's distance + distance to the node we're visiting
            # is less than the distance of the node we're visiting on file
            # replace that distance and push the node we're visiting into the priority queue
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
                heapq.heappush(pq, (dist[v], v))
    return dist


from priorityqueue import PriorityQueue, Graph

def dijkstra_pyds3(agraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in agraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)
