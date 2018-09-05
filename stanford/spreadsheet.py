# Stanford 1-2-3

from collections import deque

def test():
    pass

def indicesToName(row, col):
    return chr(ord('a') + col) + str(row + 1)

# PROBLEM: if two paths point to the same target cell, a BFS method
# using a 'visited' approach will incorrectly say a cycle exists
# DFS is needed

def hasCycle(cells, source):
    # Still broken, 's' should return a cycle and 't' should not
    for cellName in cells:
        cells[cellName].visited = False
    cells[source].visited = True
    stack = []
    stack.append(source)
    print(stack)
    ctr = 0
    # while stack:
    while ctr < 10 and stack:
        print('while', stack)
        u = cells[stack.pop()]
        for vName in u.adjList:
            print(vName, stack)
            # if vName in stack:
            if cells[vName].visited:
                return True
            cells[cellName].visited = True
            stack.append(vName)
        ctr += 1
    return False
    
class Cell:
    def __init__(self, value=None):
        self.value = None
        self.visited = False
        self.adjList = []

    def __repr__(self):
        return str(self.value)

class Spreadsheet:
    def __init__(self):
        self.dim = 3
        self.cells = {}
        for row in range(self.dim):
            for col in range(self.dim):
                cellName = indicesToName(row, col)
                # print("Creating cell", cellName)
                self.cells[cellName] = Cell()

    def set(self, cellName, value):
        print("Setting", cellName, "to", value)
        t = type(value)
        if t is str:
            for r in value.split():
                print('appending', r)
                self.cells[cellName].adjList.append(r)
            # detect cycle
            if hasCycle(self.cells, cellName):
                print("Cycle detected in setting cell", cellName)
                self.cells[cellName].adjList = []
            else:
                self.cells[cellName].value = self.get(value)
        else:
            self.cells[cellName].value = value
            self.cells[cellName].adjList = []

    def get(self, cellName):
        out = ""
        for c in cellName.split():
            out += str(self.cells[c]) + ";"
        return out

    def display(self):
        print()
        for row in range(self.dim):
            for col in range(self.dim):
                print(str(self.get(indicesToName(row, col))).rjust(6), end=' ')
            print()

        print()

        for row in range(self.dim):
            for col in range(self.dim):
                pass
                # print(str(self.get(indicesToName(row, col)).adjList).ljust(6), end=' ')
            print()                

s = Spreadsheet()
# s.set('b1', 10)
# s.set('b2', 9)
# s.set('c3', 'b1')

s.set('a1', 'c1')
s.set('c1', 'a3')
s.set('a3', 'a1')
s.set('a3', 33)
s.display()

# https://stackoverflow.com/questions/2869647/why-dfs-and-not-bfs-for-finding-cycle-in-graphs

# multipath = """
t = Spreadsheet()
#     3 - 4       0 = a2  3 = b1 
# 0 <       > 2   1 = a3  4 = b2
#     1 ---/      2 = c2

t.set('c2', 2)
t.set('a3', 'c2')
t.set('b1', 'b2')
t.set('b2', 'c2')
t.set('a2', 'b1 a3')

t.display()
# """
