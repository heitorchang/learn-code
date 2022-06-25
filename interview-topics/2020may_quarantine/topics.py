# Searching

## Binary search

def binarysearch(haystack, needle):
    # Sedgewick
    # Assume input list is sorted
    sortedlist = sorted(haystack)

    lo = 0
    hi = len(sortedlist) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if needle < sortedlist[mid]:
            hi = mid - 1
        elif needle > sortedlist[mid]:
            lo = mid + 1
        else:
            return mid
    return -1

bslist = [3, 5, 9, 11, 29, 230, 2300, 19200]
assert binarysearch(bslist, 11) == 3
assert binarysearch(bslist, 3) == 0
assert binarysearch(bslist, 19200) == 7
assert binarysearch(bslist, 7) == -1
assert binarysearch(bslist, 0) == -1
assert binarysearch(bslist, 40000) == -1


# Sorting

## Quick sort

from random import shuffle

def qsort(alist):
    shuffle(alist)

    qsorthelper(alist, 0, len(alist) - 1)


def qsorthelper(alist, first, last):
    # Miller
    if first < last:
        splitpoint = partition(alist, first, last)
        qsorthelper(alist, first, splitpoint-1)
        qsorthelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    while True:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1

        if rightmark < leftmark:
            break
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    # print(alist)

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


qslist = [3, 1, 2, 9, 8, 4, 7]
qsort(qslist)
assert qslist == [1, 2, 3, 4, 7, 8, 9]

qslist2 = [5, 4, 3, 2]
qsort(qslist2)
assert qslist2 == [2, 3, 4, 5]

# Trees

## Binary Heap / Priority Queue

# Miller


# Graphs

## Adjacency list representation

class Graph:
    adj = {}

    def __init__(self, vlist):
        # List of vertices
        for v in vlist:
            self.adj[v] = []

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def v(self):
        return len(self.adj)

    def __str__(self):
        return str(self.adj)


class Digraph:
    adj = {}

    def __init__(self, vlist):
        for v in vlist:
            self.adj[v] = []

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def v(self):
        return len(self.adj)

    def __str__(self):
        return str(self.adj)

## Depth-first search

def depth_first_search(G, s):
    # search for s in G
    numv = G.v()
    marked = [False] * numv
    found = False

    def dfs(G, v):
        nonlocal s, found
        print("visiting", v)
        if v == s:
            found = True
            return
        marked[v] = True
        for w in G.adj[v]:
            if not marked[w]:
                dfs(G, w)

    dfs(G, 0)
    if found:
        return "s found"
    return str(s) + " not found starting from 0"


## Breadth-first search

from collections import deque

def bfsConnectedComponent(G, start):
    queue = deque([start])
    visited = {start}
    component = []

    while len(queue) > 0:
        cur = queue.popleft()
        component.append(cur)

        for v in G.adj[cur]:
            if v not in visited:
                queue.append(v)
                visited.add(v)
    return component


## Cycle detection

def directed_cycle(G):
    numv = G.v()
    onStack = [False] * numv
    edgeTo = [0] * numv
    cycle = None
    marked = [False] * numv

    def dfs(G, v):
        nonlocal cycle

        onStack[v] = True
        marked[v] = True
        for w in G.adj[v]:
            if cycle is not None:
                return True
            if not marked[w]:
                edgeTo[w] = v
                dfs(G, w)
            elif onStack[w]:
                cycle = []
                x = v
                while x != w:
                    cycle.append(x)
                    x = edgeTo[x]
                cycle.append(w)
                cycle.append(v)

        onStack[v] = False

    def hasCycle():
        return cycle is not None

    v = 0
    while v < numv:
        if not marked[v]:
            dfs(G, v)
        v += 1
    return hasCycle()


## Topological sorting

"""Call dfs(G) and compute the finish times for each vertex (the point where all edges for that vertex have been explored). Then, sort the list in decreasing order of finish time."""
