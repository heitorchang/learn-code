from itertools import product
from operator import itemgetter

possibilities = list(product(product("J", [0,1,3,5]), product("M", [0,2,3])))
pollen = 2  # len(politicians)
options = set()

for calendar in possibilities:
    daysseen = set()
    if len(set(p[1] for p in calendar)) == pollen:
        options.add(tuple(sorted(calendar, key=itemgetter(1))))

for o in options:
    print(o)
