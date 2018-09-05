def test():
    testeql(bfsDistancesUnweightedGraph2([[False,False,True], 
                                          [False,False,True], 
                                          [True,True,False]], 0, 1), 2)
    testeql(bfsDistancesUnweightedGraph2([[False,True, False,False], 
                                          [True, False,True, True], 
                                          [False,True, False,True], 
                                          [False,True, True, False]], 2, 0), 2)
    testeql(bfsDistancesUnweightedGraph2([[False,True,True], 
                                          [True,False,False], 
                                          [True,False,False]], 0, 2), 1)

def bfsDistancesUnweightedGraph2(matrix, vertex1, vertex2):
    # ugly, uses "global state", still didn't pass all test cases :(
    vertices = len(matrix)
    global_steps = 0
    def navigate(current, destination, steps, visited):
        nonlocal global_steps
        print(current, destination, steps, visited)
        visited[current] = True
        if current == destination:
            print("reached", steps)
            global_steps = steps
            return steps 
        else:
            for i in range(vertices):
                if matrix[current][i] and not visited[i]:
                    navigate(i, destination, steps + 1, visited)
    navigate(vertex1, vertex2, 0, [False for _ in range(vertices)])
    return global_steps

def wrapper(matrix, vertex1, vertex2):
    paths = [[False,True, False,False], 
             [True, False,True, True], 
             [False,True, False,True], 
             [False,True, True, False]]

    paths = matrix
    vertices = len(paths)

    v1 = vertex1
    v2 = vertex2
    def navigate(current, destination, steps, visited):
        print(current, destination, visited)
        visited[current] = True
        if current == destination:
            print("reached", steps)
            return steps 
        else:
            for i in range(vertices):
                if paths[current][i] and not visited[i]:
                    return navigate(i, destination, steps + 1, visited)
    return navigate(v1, v2, 0, [False for _ in range(vertices)])
