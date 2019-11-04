from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(filter(lambda s: int(s) % d == 0, [createNumber(c) for c in product(digits, repeat=k)]))
    
def test():
    testeql(crackingPassword([1,5,2], 2, 3), ["12", 
 "15", 
 "21", 
 "51"])
