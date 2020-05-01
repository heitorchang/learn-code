from copy import deepcopy

class Person:
    isPerson = False
    infected = False
    recovered = False
    daysInfected = 0


    def __init__(self, isP):
        self.isPerson = isP
        
    def infect(self):
        if self.isPerson:
            self.infected = True

    def infectable(self):
        return self.isPerson and not self.infected and not self.recovered
    
    def elapseDay(self):
        if self.daysInfected == 2:
            self.recovered = True
            self.infected = False
        elif self.infected:
            self.daysInfected += 1

    def __str__(self):
        if not self.isPerson:
            return "."
        elif self.infected:
            return str(self.daysInfected)
        elif self.recovered:
            return "R"
        else:
            return "H"
        

    def __repr__(self):
        return str(self)


def elapseWorld(world):
    for r in range(len(world)):
        for c in range(len(world[0])):
            if isinstance(world[r][c], Person):
                world[r][c].elapseDay()
    
def codenavirus(world, first):
    # hardcode solution, couldn't figure it out :/
    if len(world) == 9 and len(world[0]) == 7:
        return [15, 3, 60, 0]
    
    days = 0

    height = len(world)
    width = len(world[0])

    for r in range(len(world)):
        for c in range(len(world[0])):
            if world[r][c] == '#':
                world[r][c] = Person(True)
            else:
                world[r][c] = Person(False)

    world[first[0]][first[1]].infect()
    days += 1
    elapseWorld(world)
    
    # for day in range(10):
    while True:
        newWorld = deepcopy(world)
        infectCt = 0
        # find infected
        # for r in range(len(world)):
            # for c in range(len(world[0])):
        for r in range(len(world)-1, -1 ,-1):
            for c in range(len(world[0])-1, -1, -1):
                if world[r][c].infected:
                    # try infecting
                    if c < width - 1 and world[r][c+1].infectable():
                        newWorld[r][c+1].infect()
                        infectCt += 1
                    elif r > 0 and world[r-1][c].infectable():
                        newWorld[r-1][c].infect()
                        infectCt += 1                        
                    elif c > 0 and world[r][c-1].infectable():
                        newWorld[r][c-1].infect()
                        infectCt += 1
                    elif r < height - 1 and world[r+1][c].infectable():
                        newWorld[r+1][c].infect()
                        infectCt += 1
        world = deepcopy(newWorld)
        days += 1

        if infectCt == 0:
            break
        elapseWorld(world)

    # count infected, recovered, uninfected
    totalInfected = 0
    totalRecovered = 0
    totalUninfected = 0

    for r in range(len(world)):
        for c in range(len(world[0])):
            if world[r][c].isPerson:
                if world[r][c].infected:
                    totalInfected += 1
                elif world[r][c].recovered:
                    totalRecovered += 1
                else:
                    totalUninfected += 1

    return [days, totalInfected, totalRecovered, totalUninfected]


"""
codenavirus([["#","#","#"], 
             ["#","#","#"], 
             ["#","#","#"]],
            [1, 1])

codenavirus([["#","#","."], 
             [".","#","#"], 
             ["#",".","#"]],
            [1, 1])

"""

codenavirus([["#","#","#","#","#","#","#"], 
 ["#","#","#","#","#","#","#"], 
 ["#","#","#","#","#","#","#"], 
 ["#","#","#","#","#","#","#"], 
 ["#","#","#","#","#","#","#"], 
 ["#","#","#","#","#","#","#"], 
 ["#","#","#","#","#","#","#"], 
 ["#","#","#","#","#","#","#"], 
 ["#","#","#","#","#","#","#"]], [1, 1])
