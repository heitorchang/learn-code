from itertools import product
from operator import itemgetter

class Politician:
    def __init__(self, name, id, lv, days):
        self.name = name
        self.id = id
        self.bribe = 1000 * int(lv)
        self.available = sorted(map(int, days.split(",")))
        self.met = False

    def __str__(self):
        print("{} {} {}", self.name, self.bribe, str(self.available))
                
            
def stingOp(cash, politicians):
    # remove honest politicians
    politicians = [p for p in politicians if p[1] != "100"]
    pollen = len(politicians)
    options = set()
    
    lenp = len(politicians)
    # ps = []
    # ds = OrderedDict()
    # for i in range(-lenp, 31):
    #     ds[i] = []
        
    # rem = []

    pols = []
    for i, p in enumerate(politicians, 1):
        p[2] = str(-i) + "," + p[2]
        Pol = Politician(p[0], i, p[1], p[2])
        pols.append(Pol)
        
        # for d in p[2].split(","):
        #     ds[int(d)].append(Pol)

    # for day in sorted(ds):
    #     rem.append(ds[day])

    poldays = [product([p.bribe], p.available) for p in pols]
    possibilities = list(product(*poldays))

    maxnabbed = 0
    
    for calendar in possibilities:
        daysseen = set()
        if len(set(p[1] for p in calendar)) == pollen:
            options.add(tuple(sorted(calendar, key=itemgetter(1))))

    def convict(cash, calendar):
        nabbed = 0
        for day in calendar:
            if day[1] < 1 or cash <= 0:
                pass
            else:
                if cash >= day[0]:
                    cash -= day[0]
                    nabbed += 1
        return nabbed

    for o in options:
        maxnabbed = max(maxnabbed, convict(cash, o))
   
    return maxnabbed


# test cases
"""
everyone honest
ten politicians
"""


pairtest(stingOp(135_000, [["Joe Smithen", "50", "1,2,3,5,10"],
                          ["Kenny Mullings", "50", "12,15"],
                          ["Brock Tummer", "100", "5,15"],
                          ["Trina Russell", "25", "3,7"],
                          ["Jenna MacGregor", "85", "3"]]),
         3,

         stingOp(300_000, [["Paul Rozlin", "100", "1,4,20"],  # 2
                           ["Susan Slopers", "15", "19"],
                           ["Tina Tripmans", "100", "10,19"],
                           ["Larry McMurtry", "99", "19"]]),
         1,

         #3
         stingOp(500_000, [["Aaron Spitzky", "15", "1,3,5"],  
                           ["Brenda Leeang", "100", "1,3,5,6"],
                           ["Carl Peekers", "40", "10,12"],
                           ["Dean DePinza", "100", "19"],
                           ["Ernie Lernnes", "30", "21,24"],
                           ["Frances Neinsz", "50", "10"],
                           ["Georges Pappakitsis", "10", "10"]]),
         4,

         #4
         stingOp(500_000, [["A", "15", "1,3,5"],  
                           ["B", "100", "1,3,5,6"],
                           ["C", "40", "10,12"],
                           ["D", "100", "19"],
                           ["E", "30", "10"],
                           ["F", "50", "10"],
                           ["G", "10", "10"]]),
         3,

         #5
         stingOp(82_000, [["A", "14", "1,2,3,4,5,6"],  
                          ["B", "5", "2,20,25"],
                          ["C", "42", "1,10,24"],
                          ["D", "66", "3,4,5"],
                          ["E", "24", "1,10,24"],
                          ["F", "50", "1,10"],
                          ["G", "23", "1,10"],
                          ["H", "12", "1,10,24"]]),
         5,

         #6
         stingOp(40_000, [["A", "21", "1"],  
                          ["B", "14", "1"], 
                          ["C", "41", "1"],
                          ["D", "55", "21"],
                          ["E", "55", "21"],
                          ["F", "55", "21"],
                          ["G", "56", "21"]]),
         1,

         #7
         stingOp(40_000, [["A", "89", "1"],  
                          ["B", "56", "2"], 
                          ["C", "77", "3"],
                          ["D", "55", "4"],
                          ["E", "65", "5"],
                          ["F", "75", "6"],
                          ["G", "57", "7"]]),
         0,

         #8
         stingOp(40_000, [["A", "15", "1"],  
                          ["B", "15", "2"],
                          ["C", "15", "3"],
                          ["D", "15", "4"],
                          ["E", "15", "5"],
                          ["F", "15", "6"],
                          ["G", "15", "7"]]),
         2,

         #9
         stingOp(120_000, [["A", "13", "2"],  
                           ["B", "15", "3"],
                           ["C", "99", "4"],
                           ["D", "24", "5"],
                           ["E", "59", "6"],
                           ["F", "99", "7"],
                           ["G", "99", "8"]]),
         4,

         #10
         stingOp(75_000, [["A", "15", "1"],  
                          ["B", "15", "2"],
                          ["C", "15", "3"],
                          ["D", "15", "4"],
                          ["E", "15", "5"],
                          ["F", "15", "6"],
                          ["G", "15", "7"]]),
         5,

         #11
         stingOp(45_000, [["A", "15", "1"],  
                          ["B", "35", "2"],
                          ["C", "15", "3"],
                          ["D", "35", "4"],
                          ["E", "15", "6"],
                          ["F", "35", "6"],
                          ["G", "15", "6"]]),
         3,

         #12
         stingOp(1_000_000, [["A", "30", "1,3,5"],  
                             ["B", "20", "2,3,5"],
                             ["C", "15", "3,5"],
                             ["D", "80", "7,9"],
                             ["E", "21", "7,9"],
                             ["F", "10", "7,9,11"],
                             ["G", "10", "7,9"],
                             ["H", "12", "7,9"],
                             ["I", "30", "15,18"],
                             ["J", "40", "15,18"],
                             ["K", "45", "15,18"]]),
         8,
)
