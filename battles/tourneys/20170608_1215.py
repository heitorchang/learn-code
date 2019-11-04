def bfsDistancesUnweightedGraph2(matrix, vertex1, vertex2):
    # solution by wohlganger
    d={}
    for i in range(len(matrix)):
        d[i]=set()
    for y,r in enumerate(matrix):
        d[y]=set()
        for x, v in enumerate(r):
            if v:
                d[y].add(x)
                d[x].add(y)
    visited=set()
    seen={vertex1}
    moves=0
    while seen:
        temp=set()
        visited|=seen
        for node in seen:
            if node==vertex2:
                return moves
            for nextnode in d[node]:
                if nextnode not in visited:
                    temp.add(nextnode)
        seen=set(temp)
        moves+=1
        

def test():
    testeql(bfsDistancesUnweightedGraph2([[False, False, True],
          [False, False, True],
                                          [True, True, False]], 0, 1), 2)
