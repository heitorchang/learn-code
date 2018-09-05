# https://rosettacode.org/wiki/Last_letter-first_letter#Python

def order_words(words):
    byfirst = {}
    for word in words:

        try:
            byfirst[word[0]].add(word)
        except KeyError:
            byfirst[word[0]] = set([word])
    return byfirst

def linkfirst(byfirst, sofar):
    chmatch = sofar[-1][-1]
    try:
        options = byfirst[chmatch] - set(sofar)
        alternatives = (linkfirst(byfirst, list(sofar) + [word]) for word in options)
        mx = max(alternatives, key=len)
        return mx
    except KeyError:
        return sofar
    except ValueError:
        return []

def llfl(words):
    byfirst = order_words(words)
    return max((linkfirst(byfirst, [word]) for word in words), key=len)

def test():
    l = llfl(["mark", 
 "kelly", 
 "kurt", 
 "terk"])
    print(len(l))
