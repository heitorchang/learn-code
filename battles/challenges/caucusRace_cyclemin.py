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

def computeMins(cycle):
    cycleLen = len(cycle) // 2
    mins = []
    mins.append(min(cycle))
    for i in range(1, cycleLen):
        if cycle[i] < mins[i-1]:
            mins.append(cycle[i])
        elif cycle[i+cycleLen-1] < mins[i-1]:
            mins.append(cycle[i+cycleLen])
        else:
            mins.append(min(cycle[i:i+cycleLen]))
    return mins

def caucusRace(values):
    winners = []
    cycle = computeCycle(values)
    mins = computeMins(cycle)
    offset = 0
    for i in range(len(values)):
        if mins[i] + offset > 0:
            winners.append(i)
        offset = -cycle[i]
    return winners

def test():
    testeql(caucusRace([-1, 4, -1, 3, -2, 2, 2, -3, 1, 3, -2]), [1,3,5,8])
    
cycleLst = """
cycle = [-1, 3, 2, 5, 3, 5, 7, 4, 5, 8, 6, 5, 9, 8, 11, 9, 11, 13, 10, 11, 14, 12], 
cycl2 = [-1, 3, 2, 5, 3, 5, 7, 4, 5, 8, 6, 5, 9, 8, 11, 9, 11, 13, 10, 11, 14, 12], 
        *                                 *
  min =  -1
    min =  2
      min = 2
cycle = [-1, 3, 2, 5, 3, 5, 7, 4, 5, 8, 6, 5, 9, 8, 11, 9, 11, 13, 10, 11, 14, 12], 
cycl2 = [0,  4, 3, 6, 4, 6, 8, 5, 6, 9, 7, 6, 10, 9, 12, 10, 12, 14, 11, 12, 15, 13], 
            *                                *
cycle = [-1, 3,  2, 5, 3, 5, 7, 4, 5, 8, 6, 5, 9, 8, 11, 9, 11, 13, 10, 11, 14, 12], 
cycl2 = [-4, 0, -1, 2, 0, 2, 4, 1, 2, 5, 3, 2, 6, 5, 8, 6, 8, 10, 7, 8, 11, 9], 
               *                                 *              
cycle = [-1, 3, 2, 5, 3, 5, 7, 4, 5, 8, 6, 5, 9, 8, 11, 9, 11, 13, 10, 11, 14, 12], 
cycl2 = [-3, 1, 0, 3, 1, 3, 5, 2, 3, 6, 4, 3, 7, 6, 9, 7, 9, 11, 8, 9, 12, 10], 

cycle = [-1, 3, 2, 5, 3, 5, 7, 4, 5, 8, 6, 5, 9, 8, 11, 9, 11, 13, 10, 11, 14, 12], 
cycl2 = [-6, -2, -3, 0, -2, 0, 2, -1, 0, 3, 1, 0, 4, 3, 6, 4, 6, 8, 5, 6, 9, 7], 
"""
