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
    len_v = len(values)
    offset = 0
    
    for i in range(len_v):
        win = True
        cycl2 = [c + offset for c in cycle]
        pr('cycle')
        pr('cycl2')
        print()
        for j in range(i, len_v * 2):
            if offset + cycle[j] <= 0:
                win = False
                break
        if win:
            winners.append(i)
        offset = -cycle[i]
    return winners

def test():
    testeql(caucusRace([-1, 4, -1, 3, -2, 2, 2, -3, 1, 3, -2]), [1,3,5,8])
