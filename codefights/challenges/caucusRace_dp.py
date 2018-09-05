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

def process(A):
    N = len(A)
    M = [[50000000 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        M[i][i] = A[i]
    for i in range(N):
        for j in range(i+1, N):
            if A[j] < M[i][j-1]:
                M[i][j] = A[j]
            else:
                M[i][j] = M[i][j-1]    
    return M

def caucusRace(values):
    winners = []
    cycle = computeCycle(values)
    len_cycle = len(cycle)
    len_values = len(values)
    M = process(cycle)

    def RMQ(i, j):
        return M[i][j]
    
    offset = 0
    for i in range(len(values)):
        if RMQ(i, i+len_values-1) + offset > 0:
            winners.append(i)
        offset = -cycle[i]
    return winners

def test():
    # testeql(buildSegTree([2,5,1,4,9,3], 0, len([2,5,1,4,9,3])), None)
    # testeql(RMQ(buildSegTree([2,5,1,4,9,3], 0, 6), 2, 2), 1)
    # testeql(RMQ(buildSegTree([2,5,1,4,9,3], 0, 6), 1, 4), 1)
    testeql(caucusRace([-1, 4, -1, 3, -2, 2, 2, -3, 1, 3, -2]), [1,3,5,8])
