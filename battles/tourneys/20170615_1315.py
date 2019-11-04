def avoidObstacles(inputArray):
    for trial in range(2, max(inputArray)):
        pos = 0
        while pos < max(inputArray):
            if pos in inputArray:
                break
            pos += trial
            if pos > max(inputArray):
                return trial
    return max(inputArray) + 1



def test():
    testeql(avoidObstacles([5,3,6,7,9]), 4)
        
