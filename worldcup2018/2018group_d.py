# date: 22 jun 2018
# group D: ARG, ICE, CRO, NIG

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
    if result == -1:
        # teamA wins
        teamA.win()
    elif result == 0:
        # tie
        teamA.tie()
        teamB.tie()
    elif result == 1:
        teamB.win()
    else:
        raise ValueError("Unknown match result", result)

def simulate(optimistic=False):
    """Assume optimistically that in every tie (between 2nd and 3rd places) Argentina comes ahead (it is first alphabetically in this group"""

    arg = Team("ARG")
    ice = Team("ICE")
    cro = Team("CRO")
    nig = Team("NIG")
    
    teams = [arg, ice, cro, nig]
    
    # match 6/16
    match(cro, nig, -1)

    match(arg, ice, 0)

    # match 6/21
    match(arg, cro, 1)

    # match 6/22
    match(nig, ice, -1)

    print("Current Standings")
    
    for team in teams:
        print(team)

    # simulate remaining games
    result_values = (-1, 0, 1)
    results = product(result_values, repeat=2)
    arg_in = 0
    print("""
Matches: 
    NIG x ARG , ICE x CRO
-1 means the left team wins
 0 means a tie
 1 means the right team wins
""")
    
    print("Optimistic? (assume in point ties ARG comes ahead)", optimistic)
    print()

    for result in results:
        arg_h, ice_h, cro_h, nig_h = [copy(team) for team in teams]
        match(nig_h, arg_h, result[0])
        match(ice_h, cro_h, result[1])
        
        standings_alpha = sorted([arg_h, ice_h, cro_h, nig_h], key=attrgetter('name'), reverse=(not optimistic)) 

        standings_pts = sorted(standings_alpha, key=attrgetter('pts'), reverse=True)

        print(format(str(tuple(result)), "17"), end="")

        if standings_pts[1].pts == standings_pts[2].pts:
            print("2nd Tie", end=" ")
        else:
            print("       ", end=" ")            

        if standings_pts.index(arg_h) < 2:
            print("*ADVANCE*", end=" ")
            arg_in += 1
        else:
            print("_go home_", end=" ")
        
        print(', '.join([str(team) for team in standings_pts]))

    print("'ARG in' in a total of", arg_in, "out of", 3**4, "scenarios")
    
print()
simulate()

