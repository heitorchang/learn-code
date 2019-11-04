#!/bin/python3

import sys
from collections import defaultdict

def fib(n, memo):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    else:
        v = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = v
        return v

def gFirstAttempt(path, treeVals, adjList, memo):
    """path is a (u, v) tuple"""
    if path[0] == path[1]:
        return treeVals[path[0]]
    elif path in memo:
        return memo[path]
    else:
        return treeVals[path[0]] + 0  # hmm, which path to take?

def addToAdjMatrix(matrix, u, v):
    matrix[u-1][v-1] = 1
    matrix[v-1][u-1] = 1

def buildFromStart(adjMatrix, startNode, treeVals, curNode, curSum, visited, pathMemo):
    paths = adjMatrix[curNode]
    pathsLeft = []
    pathMemo[(startNode, curNode)] = curSum
    visited.append(curNode)

    for v, path in enumerate(paths):
        if path == 1 and v not in visited:
            pathsLeft.append(v)
    # pr('startNode curNode curSum paths pathsLeft')
    if len(pathsLeft) == 0:
        return
    for path in pathsLeft:
        buildFromStart(adjMatrix, startNode, treeVals, path, curSum + treeVals[path], visited, pathMemo)
    
def buildPathMemo(adjMatrix, treeVals, pathMemo):
    for startNode in range(len(adjMatrix)):
        buildFromStart(adjMatrix, startNode, treeVals, startNode, treeVals[startNode], [], pathMemo)
        
submission = """
if __name__ == "__main__":
    vertices = int(input())
    adjMatrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
    for i in range(vertices-1):
        u, v = input().strip().split()
        u, v = [int(u), int(v)]
        addToAdjMatrix(adjMatrix, u, v)
    treeVals = list(map(int, input().strip().split()))
    pathMemo = defaultdict(int)
    buildPathMemo(adjMatrix, treeVals, pathMemo)
    total = 0
    fibMemo = defaultdict(int)
    for path in pathMemo:
        total += fib(pathMemo[path], fibMemo) % (10 ** 9 + 7)
    print(total % (10 ** 9 + 7))

        """
def main():
    vertices = 3
    treeVals = [2, 1, 1]                   

    adjMatrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    addToAdjMatrix(adjMatrix, 1, 2)
    addToAdjMatrix(adjMatrix, 1, 3)

    # pr('adjMatrix')
    pathMemo = defaultdict(int)
    buildPathMemo(adjMatrix, treeVals, pathMemo)
    # pr('pathMemo')
    total = 0
    fibMemo = defaultdict(int)
    for path in pathMemo:
        total += fib(pathMemo[path], fibMemo) % (10 ** 9 + 7)
    return total % (10 ** 9 + 7)
    # print(total % (10 ** 9 + 7))

def test():
    testeql(main(), 26)
