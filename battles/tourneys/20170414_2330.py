def bfsConnectedComponents(matrix):
    pass

def rectangleRotation(a, b):
    def sqr(x):
        return x * x
    answer = 0
    for x in range(-a - b, a + b + 1):
        for y in range(-a - b, a + b + 1):
            if 2 * sqr(x - y) <= sqr(a) and 2 * sqr(x + y) <= sqr(b):
                answer += 1

    return answer

def test():
    testeql(bfsConnectedComponents([[False,True,False], 
                                    [True,False,False], 
                                    [False,False,False]]), 2)
    testeql(rectangleRotation(6, 4), 23)
