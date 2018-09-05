# Python 2

# https://rosettacode.org/wiki/Last_letter-first_letter
class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        def order_words(words):
            byfirst = {}
            for word in words:
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
            return max((linkfirst(byfirst, [word]) for word in words), key=len)
        return len(llfl(map(str.lower, self.names))) == len(self.names)
        
def isCoolTeam(team):
    return bool(Team(team))
