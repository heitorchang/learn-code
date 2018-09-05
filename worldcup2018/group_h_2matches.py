# date: 24 jun 2018
# group H : JPN, SEN, COL, POL

from copy import copy
from itertools import product
from operator import attrgetter

class Team:
    def __init__(self, name, favorite=0):
        self.pts = 0
        self.name = name
        self.favorite = favorite

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
    """Assume optimistically that in every tie (between 2nd and 3rd places) JPN comes ahead (it is second to arg in this group"""

    jpn = Team("JPN", favorite=1)
    sen = Team("SEN")
    col = Team("COL")
    pol = Team("POL")
    
    teams = [jpn, sen, col, pol]
    
    match(col, jpn, 1)

    match(pol, sen, 1)

    match(jpn, sen, 0)

    match(pol, col, 1)

    print("Current Standings")
    
    for team in teams:
        print(team)

    # simulate remaining games
    result_values = (-1, 0, 1)
    results = product(result_values, repeat=2)
    jpn_in = 0
    print("""
Matches:
    JPN x POL, SEN x COL
-1 means the left team wins
 0 means a tie
 1 means the right team wins
""")
    
    print("Optimistic? (assume in point ties JPN comes ahead)", optimistic)
    print()

    for result in results:
        jpn_h, sen_h, col_h, pol_h = [copy(team) for team in teams]
        match(jpn_h, pol_h, result[0])
        match(sen_h, col_h, result[1])
        
        standings_favorite = sorted([jpn_h, sen_h, col_h, pol_h], key=attrgetter('favorite'), reverse=optimistic)

        
        standings_pts = sorted(standings_favorite, key=attrgetter('pts'), reverse=True)

        print(format(str(tuple(result)), "17"), end="")

        if standings_pts[1].pts == standings_pts[2].pts:
            print("2nd Tie", end=" ")
        else:
            print("       ", end=" ")            

        if standings_pts.index(jpn_h) < 2:
            print("*ADVANCE*", end=" ")
            jpn_in += 1
        else:
            print("_go home_", end=" ")
        
        print(', '.join([str(team) for team in standings_pts]))

    print("'JPN in' in a total of", jpn_in, "out of", 3**2, "scenarios")
    
print()
simulate()

