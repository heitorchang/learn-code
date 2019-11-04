description = """
Consider an undirected graph consisting of n nodes where each node is labeled from 1 to n and the edge between any two nodes is always of length 6. We define node s to be the starting position for a BFS. Given a graph, determine the distances from the start node to each of its descendants and return the list in node number order, ascending. If a node is disconnected, it's distance should be -1.

For example, there are n = 6 nodes in the graph with a starting node s = 1. The list of edges [[1,2], [2,3], [3,4], [1,5]], and each has a weight of 6.

(6)
    (2)-(3)-(4)
(1)<
    (5)

Starting from node 1 and creating a list of distances, for nodes 2 through 6 we have distances = [6, 12, 18, 6, -1].

Function Description

Complete the required methods below to implement
"""

from collections import deque

class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.dist = 0
        self.adjList = []

class Graph:
    def __init__(self, n):
        self.vertices = []
        for i in range(n):
            self.vertices.append(Node(i))

    def connect(self, u, v):
        self.vertices[u-1].adjList.append(v-1)
        self.vertices[v-1].adjList.append(u-1)

    def find_all_distances(self, s):
        source = self.vertices[s-1]
        q = deque()
        q.append(source)
        source.visited = True
        while q:
            u = q.popleft()
            for vIdx in u.adjList:
                v = self.vertices[vIdx]
                if not v.visited:
                    v.visited = True
                    # print("u.id",u.id)
                    v.dist += u.dist + 6
                    q.append(v)
        ans = ""
        for v in self.vertices:
            # print("v.id", v.id)
            if v.id != s-1:
                ans += str(v.dist) if v.dist > 0 else "-1"
                ans += " "
        print(ans.strip())           
            
            

hackerrank = """
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)

"""

def test():
    pass

test1 = """
g = Graph(4)
g.connect(1, 2)
g.connect(1, 3)
g.find_all_distances(1)
"""

g1 = Graph(4)
g1.connect(1, 2)
g1.connect(1, 3)
g1.find_all_distances(1)

# test 2
g = Graph(3)
g.connect(2, 3)
g.find_all_distances(2)
