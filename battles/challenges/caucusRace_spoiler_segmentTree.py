from collections import namedtuple

Node = namedtuple('Node', 'value L R LRng RRng')

def buildSegTree(arr, LRange, RRange):
    curMin = min(arr)
    len_arr = len(arr)
    if len_arr == 1:
        return Node(curMin, None, None, LRange, LRange)
    else:
        len_child = len_arr // 2
        return Node(curMin,
                    buildSegTree(arr[:len_child], LRange, LRange + len_child),
                    buildSegTree(arr[len_child:], LRange + len_child, RRange),
                    LRange, LRange + len_arr - 1)

def RMQ(node, queryL, queryR):
    nodeL, nodeR = node.LRng, node.RRng;
    if queryL <= nodeL and queryR >= nodeR:
        return node.value
    if nodeR < queryL or nodeL > queryR:
        return 50000000   
    return min(RMQ(node.L, queryL, queryR),
               RMQ(node.R, queryL, queryR))

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
    segTree = buildSegTree(cycle, 0, len_cycle)
    
    offset = 0
    for i in range(len(values)):
        pr('i')
        if RMQ(segTree, i, i+len_values-1) + offset > 0:
            winners.append(i)
        offset = -cycle[i]
    return winners

def test():
    # testeql(buildSegTree([2,5,1,4,9,3], 0, len([2,5,1,4,9,3])), None)
    # testeql(RMQ(buildSegTree([2,5,1,4,9,3], 0, 6), 2, 2), 1)
    # testeql(RMQ(buildSegTree([2,5,1,4,9,3], 0, 6), 1, 4), 1)
    testeql(caucusRace([-1, 4, -1, 3, -2, 2, 2, -3, 1, 3, -2]), [1,3,5,8])
