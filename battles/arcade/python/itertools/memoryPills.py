from itertools import dropwhile, chain, repeat

def memoryPills(pills):
    gen = chain(dropwhile(lambda x: len(x) % 2 == 1, pills), repeat("", 3))
    
    next(gen)
    return [next(gen) for _ in range(3)]

def test():
    testeql(memoryPills(["Notforgetan", 
 "Antimoron", 
 "Rememberin", 
 "Bestmedicen", 
                         "Superpillsus"]), ["Bestmedicen", 
 "Superpillsus", 
 ""])
