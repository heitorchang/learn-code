# date: 24 jun 2018
# group E: Serbia, Switzerland, Costa Rica, Brazil

from copy import copy
from itertools import product
from operator import attrgetter

class Team:
    def __init__(self, name):
        self.pts = 0
        self.name = name

    def win(self):
        self.pts += 3

    def tie(self):
        self.pts += 1

    def __repr__(self):
        # return "Team('{}') # {}".format(self.name, self.pts)
        return "{} ({})".format(self.name, self.pts)
        
    def __str__(self):
        return "{}: {}".format(self.name, self.pts)
        
def match(teamA, teamB, result):
    # Left, Tie, Right
    if result == 'L':
        # teamA wins
        teamA.win()
        return teamA.name
    elif result == 'T':
        # tie
        teamA.tie()
        teamB.tie()
        return 'TIE'
    elif result == 'R':
        teamB.win()
        return teamB.name
    else:
        raise ValueError("Unknown match result", result)

def simulate(optimistic=False):
    """Assume optimistically that in every tie (between 2nd and 3rd places) Brazil comes ahead (it is first alphabetically in this group"""

    ser = Team("SER")
    swi = Team("SWI")
    cos = Team("COS")
    bra = Team("BRA")

    teams = [ser, swi, cos, bra]
    
    # match 6/17
    match(cos, ser, 'R')

    # match 6/17
    match(bra, swi, 'T')

    # 6/22
    match(bra, cos, 'L')

    # 6/22
    match(ser, swi, 'R')
    
    print("Current Standings")
    
    for team in teams:
        print(team)

    # simulate remaining games
    result_values = ('L', 'T', 'R')
    results = product(result_values, repeat=2)
    bra_in = 0
    print("""
Matches:

SERV x BRA , SWI X COS

L means the left team wins
T means a tie
R means the right team wins
""")
    
    print("Optimistic? (assume in point ties Brazil comes ahead)", optimistic)
    print()

    for result in results:
        serv_hypo, swi_hypo, cos_hypo, bra_hypo = [copy(team)
                                                  for team in teams]

        winners = ""
        winners += match(serv_hypo, bra_hypo, result[0]) + ", "
        winners += match(swi_hypo, cos_hypo, result[1])
        
        standings_alpha = sorted([serv_hypo, swi_hypo, cos_hypo, bra_hypo], key=attrgetter('name'), reverse=(not optimistic)) 

        standings_pts = sorted(standings_alpha, key=attrgetter('pts'), reverse=True)

        print(format(winners, "14"), end="")

        if standings_pts[1].pts == standings_pts[2].pts:
            print("pts.tie", end=" ")
        else:
            print("       ", end=" ")            

        if standings_pts.index(bra_hypo) < 2:
            print("*ADVANCE*", end=" ")
            bra_in += 1
        else:
            print("_go home_", end=" ")
        
        print(', '.join([str(team) for team in standings_pts]))

    print("'BRA in' in a total of", bra_in, "out of", 3**2, "scenarios")
    
print()
simulate()

