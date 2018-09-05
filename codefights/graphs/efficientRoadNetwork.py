from collections import defaultdict

def makeAdjList(edgeList):
    """make an adjacency list out of a list of edges"""
    adjList = defaultdict(set)
    for edge in edgeList:
        adjList[edge[0]].add(edge[1])
        adjList[edge[1]].add(edge[0])
    return adjList
    
def efficientRoadNetwork(n, roads):
    adjList = makeAdjList(roads)
    if len(adjList) == 0 and n > 1:
        return False
        
    # compute secondary neighbors
    for vertex in adjList:
        newSet = set(adjList[vertex])
        for firstNeighbor in adjList[vertex]:
            newSet |= adjList[firstNeighbor]
        reached = len(newSet)
        if reached < n:
            return False
    return True
    
def test():
    testeql(efficientRoadNetwork(6, [[3,0], 
                                     [0,4], 
                                     [5,0], 
                                     [2,1], 
                                     [1,4], 
                                     [2,3], 
                                     [5,2]]), True)
    testeql(efficientRoadNetwork(6, [[0,4], 
                                     [5,0], 
                                     [2,1], 
                                     [1,4], 
                                     [2,3], 
                                     [5,2]]), False)
    testeql(efficientRoadNetwork(2, []), False)
