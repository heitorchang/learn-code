class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        if len(self.names) < 2:
            return True
        def order_words(words):
            byfirst = {}
            for name in words:
                word = name.lower()
                try:
                    byfirst[word[0]].add(word)
                except KeyError:
                    byfirst[word[0]] = set([word])
            return byfirst
        def linkfirst(byfirst, sofar):
            assert sofar
            chmatch = sofar[-1][-1]
            options = byfirst[chmatch] - set(sofar)
            if not options:
                return sofar
            else:
                alternatives = (linkfirst(byfirst, list(sofar) + [word]) for word in options)
                mx = max(alternatives, key=len)
                return mx
            
        def llfl(words):
            byfirst = order_words(words)
            pr('byfirst')
            return max((linkfirst(byfirst, [word]) for word in words), key=len)
        return len(llfl(self.names)) == len(self.names)

def isCoolTeam(team):
    return bool(Team(team))

def test():
    testeql(isCoolTeam(["Mark", 
 "Kelly", 
 "Kurt", 
 "Terk"]), True)
    testeql(isCoolTeam(["Sophie", 
 "Boris", 
 "Eric", 
 "Charlotte", 
 "Cedric", 
 "Charlie"]), False)
    testeql(isCoolTeam(["Sophie", 
 "Boris", 
 "EriC", 
 "Charlotte"]), True)
    testeql(isCoolTeam(["Bob", 
 "Bobby", 
 "Billy"]), False)
