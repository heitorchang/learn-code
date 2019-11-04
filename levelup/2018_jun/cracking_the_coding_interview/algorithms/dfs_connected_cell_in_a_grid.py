description = """
Consider a matrix where each cell contains either a 0 or a 1 and any cell containing a 1 is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the diagram below, the two colored regions show cells connected to the filled cells. Black on white are not connected.

Cells adjacent to filled cells: 000
                                010
                                000

If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.

Given an  matrix, find and print the number of cells in the largest region in the matrix.


Input Format

The first line contains an integer, n, the number of rows in the matrix, . 
The second line contains an integer, m, the number of columns in the matrix.

Each of the following n lines contains a row of m space-separated integers, grid[i][j].
"""

hackerrank = """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
"""

class Vertex:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.adjList = []

    def __repr__(self):
        return str(self.value)

def maxRegion(grid):
    graph = {}
    sizes = {}
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            graph[(r, c)] = Vertex(grid[r][c])

    for vTuple in graph:
        v = graph[vTuple]
        r = vTuple[0]
        c = vTuple[1]
        # print("vtuple", vTuple, r, c)
        for neighborRow in range(r-1, r+2):
            for neighborCol in range(c-1, c+2):
                # print(" nc ", neighborRow, neighborCol, end=" ")
                if (neighborRow, neighborCol) != (r, c) and 0 <= neighborRow < len(grid) and 0 <= neighborCol < len(grid[0]):
                    neighborVal = grid[neighborRow][neighborCol]
                    if grid[r][c] == 1 and neighborVal == 1:
                        graph[(r, c)].adjList.append((neighborRow, neighborCol))
                        # print("appended", neighborRow, neighborCol)
        # print("--")

    # traverse graph
    for uTuple in graph:
        u = graph[uTuple]
        if not u.visited:
            stack = []
            stack.append(u)
            u.visited = True
            size = 1
            while stack:
                v = stack.pop()
                for cTuple in v.adjList:
                    # print(v.adjList)
                    c = graph[cTuple]
                    if not c.visited:
                        c.visited = True
                        stack.append(c)
                        size += 1
                        # print(size)
            sizes[uTuple] = size
    # print(sizes)
    return max(sizes.values())
    
grid = [[1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0]]

print(maxRegion(grid))
