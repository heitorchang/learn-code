def buildSparseTable(a):
    n = len(a)

    logTable = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        logTable[i] = logTable[i >> 1] + 1

    rmq = [[0 for _ in range(n)] for _ in range(logTable[n]+1)]

    for i in range(n):
        rmq[0][i] = i

    k = 1
    while (1 << k) < n:
        i = 0
        while (i + (1 << k)) <= n:
            x = rmq[k - 1][i]
            y = rmq[k - 1][i + (1 << k -1)]
            if a[x] <= a[y]:
                rmq[k][i] = x
            else:
                rmq[k][i] = y    
            i += 1
        k += 1
    pr('k i')
    print("len logTable, rmq", len(logTable), len(rmq))
    return logTable, rmq
    
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

    logTable, rmq = buildSparseTable(cycle)

    def minPos(i, j):
        k = logTable[j - i]
        x = rmq[k][i]
        y = rmq[k][j - (1 << k) + 1]
        if cycle[x] <= cycle[y]:
            return x
        else:
            return y
    
    offset = 0
    for i in range(len(values)):
        L = i
        R = i+len_values-1
        curMin = cycle[minPos(L, R)]
        
        if curMin + offset > 0:
            winners.append(i)
        offset = -cycle[i]
    return winners

def test():
    # testeql(buildSegTree([2,5,1,4,9,3], 0, len([2,5,1,4,9,3])), None)
    # testeql(RMQ(buildSegTree([2,5,1,4,9,3], 0, 6), 2, 2), 1)
    # testeql(RMQ(buildSegTree([2,5,1,4,9,3], 0, 6), 1, 4), 1)
    testeql(caucusRace([-1, 4, -1, 3, -2, 2, 2, -3, 1, 3, -2]), [1,3,5,8])

