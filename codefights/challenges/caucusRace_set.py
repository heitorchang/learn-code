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
    elems = set(cycle)
    minElem = min(elems)

    pr('cycle')
    
    for i in range(len(values)):
        if i == 0:
            offset = 0
        else:
            offset = cycle[i-1]
            # elems.discard(cycle[i-1])
        pr('i offset elems')
        if minElem - offset <= 0:
            winners.append(i)
    return winners

def willLose(values, cycle, i):
    # stop looking after finding a losing value
    startValue = values[i]
    if i == 0:
        offset = 0
    else:
        offset = cycle[i-1]
    newCycleLen = len(cycle) // 2
    return any([n <= offset for n in cycle[i:i+newCycleLen]])

def test():
    testeql(caucusRace([-1, 4, -1, 3, -2, 2, 2, -3, 1, 3, -2]), [1,3,5,8])
