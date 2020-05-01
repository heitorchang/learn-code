from collections import defaultdict

class Politician:
    def __init__(self, name, lv, days):
        self.name = name
        self.bribe = 1000 * int(lv)
        self.available = map(int, days.split(","))
        self.met = False

    def __str__(self):
        print("{} {} {}", self.name, self.bribe, str(self.available))
        
        
def stingOp(cash, politicians):
    def traverse(cash, nabbed, remaining):
        if cash < 0 or len(remaining) == 0:
            return nabbed
        print(cash, nabbed, remaining)
        
        return max([0] + [traverse(cash - nextpol.bribe, nabbed + 1, remaining[1:]) for nextpol in remaining[0]])

    ps = []
    ds = defaultdict(list)
    rem = []
    
    for p in politicians:
        Pol = Politician(p[0], p[1], p[2])
        for d in p[2].split(","):
            ds[int(d)].append(Pol)

    for day in sorted(ds):
        rem.append(ds[day])
        
    # return traverse(cash, 0, ds)
    
    traverse(10000000, 0, rem)
    return 3


pairtest(stingOp(100000, [["Joe Smithen", "50", "1,2,3,5,10"],
                          ["Jack Russell", "22", "3,5"],
                          ["Jenna MacGregor", "92", "7"]]),
         3,
)

