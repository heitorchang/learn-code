def checkParticipants(participants):
    e = list(enumerate(participants))
    pr('e')
    return [e[0] for e in enumerate(participants) if e[1] < e[0]]

def test():
    testeql(checkParticipants([0,1,1,5,4,8]), [2])
