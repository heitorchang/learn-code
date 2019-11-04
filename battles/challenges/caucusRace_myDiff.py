def buildTable(cycle, values):
    len_cycle = len(cycle)
    len_circle = len_cycle // 2
    
    result = []
    circle = cycle[:len_circle]
    curMin = min(circle)
    idx = circle.index(curMin)

    for i in range(len_circle):
        if i > idx:
            curCircle = cycle[i:i+len_circle]
            curMin = min(curCircle)
            idx = i + curCircle.index(curMin)
        result.append(curMin)
    return result
        
def computeCycle(values):
    cycle = []
    runningSum = 0
    for n in values:
        runningSum += n
        cycle.append(runningSum)
    for n in values:
        runningSum += n
        cycle.append(runningSum)
    return cycle

def caucusRace(values):
    winners = []
    cycle = computeCycle(values)
    len_cycle = len(cycle)
    len_values = len(values)
    myDiffTable = buildTable(cycle, values)
    pr('myDiffTable')
    offset = 0
    for i in range(len(values)):
        if myDiffTable[i] + offset > 0:
            winners.append(i)
        offset = -cycle[i]
    return winners

def test():
    # testeql(buildSegTree([2,5,1,4,9,3], 0, len([2,5,1,4,9,3])), None)
    # testeql(RMQ(buildSegTree([2,5,1,4,9,3], 0, 6), 2, 2), 1)
    # testeql(RMQ(buildSegTree([2,5,1,4,9,3], 0, 6), 1, 4), 1)
    testeql(caucusRace([-1, 4, -1, 3, -2, 2, 2, -3, 1, 3, -2]), [1,3,5,8])
