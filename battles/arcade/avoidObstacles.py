def avoidObstacles(inputArray):
    obstacles = set(inputArray)
    last = max(obstacles)
    for jump in range(2, last+2):
        spot = jump
        pr('spot')
        reachesEnd = True
        while spot <= last:
            pr('spot last')
            if spot in obstacles:
                reachesEnd = False
                break
            spot += jump
        if reachesEnd:
            return jump
            

def test():
    testeql(avoidObstacles([5, 3, 6, 7, 9]), 4)
    testeql(avoidObstacles([1, 4, 10, 6, 2]), 7)
