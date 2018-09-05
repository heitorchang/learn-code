def correctLineup(athletes):
    # http://stackoverflow.com/questions/7946798/interleaving-two-lists-in-python
    a = athletes[1::2]
    b = athletes[::2]
    pr('a b')
    print(list(zip(a,b)))
    print([val for pair in zip(a,b) for val in pair])
def test():
    testeql(correctLineup([1,2,3,4,5,6]), [2,1,4,3,6,5])
