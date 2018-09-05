# date: 20 jun 2018
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
    """Assume optimistically that in every tie (between 2nd and 3rd places) Brazil comes ahead (it is first alphabetically in this group"""

    ser = Team("SER")
    swi = Team("SWI")
    cos = Team("COS")
    bra = Team("BRA")

    teams = [ser, swi, cos, bra]
    
    # match 6/17
    match(cos, ser, 1)

    # match 6/17
    match(bra, swi, 0)

    # 6/22
    match(bra, cos, -1)
    
    print("Current Standings")
    
    for team in teams:
        print(team)

    # simulate remaining games
    result_values = (-1, 0, 1)
    results = product(result_values, repeat=3)
    bra_in = 0
    print("""
Matches:

SERV X SWI , SERV x BRA , SWI X COS

-1 means the left team wins
 0 means a tie
 1 means the right team wins
""")
    
    print("Optimistic? (assume in point ties Brazil comes ahead)", optimistic)
    print()

    for result in results:
        serv_hypo, swi_hypo, cos_hypo, bra_hypo = [copy(team)
                                                  for team in teams]        
        match(serv_hypo, swi_hypo, result[0])
        match(serv_hypo, bra_hypo, result[1])
        match(swi_hypo, cos_hypo, result[2])
        
        standings_alpha = sorted([serv_hypo, swi_hypo, cos_hypo, bra_hypo], key=attrgetter('name'), reverse=(not optimistic)) 

        standings_pts = sorted(standings_alpha, key=attrgetter('pts'), reverse=True)

        print(format(str(tuple(result)), "17"), end="")

        if standings_pts[1].pts == standings_pts[2].pts:
            print("2nd Tie", end=" ")
        else:
            print("       ", end=" ")            

        if standings_pts.index(bra_hypo) < 2:
            print("*ADVANCE*", end=" ")
            bra_in += 1
        else:
            print("_go home_", end=" ")
        
        print(', '.join([str(team) for team in standings_pts]))

    print("'BRA in' in a total of", bra_in, "out of", 3**4, "scenarios")
    
print()
simulate()

observations = """
I can't wait until Friday's Brazil X Costa Rica match so I ran a Python simulation of all 81 possible remaining match results between the Group E teams. There must be better analyses out there but all I wanted was a more "fun" programming exercise.

- In the most pessimistic scenario (if Brazil's goal difference puts them behind all other teams), supposing Brazil loses to Costa Rica, the only way for them to advance is: Brazil beats Serbia, and Switzerland beats both Serbia and Costa Rica. (standings: SWI: 7, BRA: 4, SER: 3, COS: 3)

- If Brazil ties with Costa Rica, then beats Serbia, Brazil advances.

- If Brazil beats Costa Rica and loses to Serbia, they advance in 4 out of the 9 possible scenarios

- If Brazil beats Costa Rica and ties with Serbia, only one scenario will send them home: being last in the goal difference, with Serbia tying with Switzerland and Switzerland beating Costa Rica (standings: SWI: 5, SER: 5, BRA: 5, COS: 0). With any better result, Brazil advances.

- In the most optimistic scenario (Brazil's goal difference is ahead of everyone else), they advance in 8 out of 9 scenarios if they lose to Costa Rica then beat Serbia

- Overall, with these optimistic assumptions about the goal difference, Brazil advances in 44 out of 81 scenarios.
"""

simulation_results = """

# OPTIMISTIC = FALSE
(Brazil's goal difference loses to everyone else)

Current Standings
SER: 3
SWI: 1
COS: 0
BRA: 1

Matches:

COS X BRA , SERV X BRA , SERV X SWI , SWI X COS

-1 means the left team wins
 0 means a tie
 1 means the right team wins

Optimistic? (assume in point ties Brazil comes ahead) False

(-1, -1, -1, -1)         _go home_ SER: 9, SWI: 4, COS: 3, BRA: 1
(-1, -1, -1, 0)          _go home_ SER: 9, COS: 4, SWI: 2, BRA: 1
(-1, -1, -1, 1)          _go home_ SER: 9, COS: 6, SWI: 1, BRA: 1
(-1, -1, 0, -1)          _go home_ SER: 7, SWI: 5, COS: 3, BRA: 1
(-1, -1, 0, 0)           _go home_ SER: 7, COS: 4, SWI: 3, BRA: 1
(-1, -1, 0, 1)           _go home_ SER: 7, COS: 6, SWI: 2, BRA: 1
(-1, -1, 1, -1)          _go home_ SWI: 7, SER: 6, COS: 3, BRA: 1
(-1, -1, 1, 0)           _go home_ SER: 6, SWI: 5, COS: 4, BRA: 1
(-1, -1, 1, 1)           _go home_ SER: 6, COS: 6, SWI: 4, BRA: 1
(-1, 0, -1, -1)          _go home_ SER: 7, SWI: 4, COS: 3, BRA: 2
(-1, 0, -1, 0)           _go home_ SER: 7, COS: 4, SWI: 2, BRA: 2
(-1, 0, -1, 1)           _go home_ SER: 7, COS: 6, BRA: 2, SWI: 1
(-1, 0, 0, -1)           _go home_ SWI: 5, SER: 5, COS: 3, BRA: 2
(-1, 0, 0, 0)            _go home_ SER: 5, COS: 4, SWI: 3, BRA: 2
(-1, 0, 0, 1)            _go home_ COS: 6, SER: 5, SWI: 2, BRA: 2
(-1, 0, 1, -1)           _go home_ SWI: 7, SER: 4, COS: 3, BRA: 2
(-1, 0, 1, 0)    2nd Tie _go home_ SWI: 5, SER: 4, COS: 4, BRA: 2
(-1, 0, 1, 1)    2nd Tie _go home_ COS: 6, SWI: 4, SER: 4, BRA: 2
(-1, 1, -1, -1)  2nd Tie _go home_ SER: 6, SWI: 4, BRA: 4, COS: 3
(-1, 1, -1, 0)   2nd Tie _go home_ SER: 6, COS: 4, BRA: 4, SWI: 2
(-1, 1, -1, 1)           _go home_ SER: 6, COS: 6, BRA: 4, SWI: 1
(-1, 1, 0, -1)   2nd Tie _go home_ SWI: 5, SER: 4, BRA: 4, COS: 3
(-1, 1, 0, 0)    2nd Tie _go home_ SER: 4, COS: 4, BRA: 4, SWI: 3
(-1, 1, 0, 1)    2nd Tie _go home_ COS: 6, SER: 4, BRA: 4, SWI: 2
(-1, 1, 1, -1)           *ADVANCE* SWI: 7, BRA: 4, SER: 3, COS: 3
(-1, 1, 1, 0)    2nd Tie _go home_ SWI: 5, COS: 4, BRA: 4, SER: 3
(-1, 1, 1, 1)    2nd Tie _go home_ COS: 6, SWI: 4, BRA: 4, SER: 3
(0, -1, -1, -1)          _go home_ SER: 9, SWI: 4, BRA: 2, COS: 1
(0, -1, -1, 0)   2nd Tie _go home_ SER: 9, SWI: 2, COS: 2, BRA: 2
(0, -1, -1, 1)           _go home_ SER: 9, COS: 4, BRA: 2, SWI: 1
(0, -1, 0, -1)           _go home_ SER: 7, SWI: 5, BRA: 2, COS: 1
(0, -1, 0, 0)            _go home_ SER: 7, SWI: 3, COS: 2, BRA: 2
(0, -1, 0, 1)            _go home_ SER: 7, COS: 4, SWI: 2, BRA: 2
(0, -1, 1, -1)           _go home_ SWI: 7, SER: 6, BRA: 2, COS: 1
(0, -1, 1, 0)            _go home_ SER: 6, SWI: 5, COS: 2, BRA: 2
(0, -1, 1, 1)    2nd Tie _go home_ SER: 6, SWI: 4, COS: 4, BRA: 2
(0, 0, -1, -1)           _go home_ SER: 7, SWI: 4, BRA: 3, COS: 1
(0, 0, -1, 0)            *ADVANCE* SER: 7, BRA: 3, SWI: 2, COS: 2
(0, 0, -1, 1)            _go home_ SER: 7, COS: 4, BRA: 3, SWI: 1
(0, 0, 0, -1)            _go home_ SWI: 5, SER: 5, BRA: 3, COS: 1
(0, 0, 0, 0)     2nd Tie _go home_ SER: 5, SWI: 3, BRA: 3, COS: 2
(0, 0, 0, 1)             _go home_ SER: 5, COS: 4, BRA: 3, SWI: 2
(0, 0, 1, -1)            _go home_ SWI: 7, SER: 4, BRA: 3, COS: 1
(0, 0, 1, 0)             _go home_ SWI: 5, SER: 4, BRA: 3, COS: 2
(0, 0, 1, 1)     2nd Tie _go home_ SWI: 4, SER: 4, COS: 4, BRA: 3
(0, 1, -1, -1)           *ADVANCE* SER: 6, BRA: 5, SWI: 4, COS: 1
(0, 1, -1, 0)            *ADVANCE* SER: 6, BRA: 5, SWI: 2, COS: 2
(0, 1, -1, 1)            *ADVANCE* SER: 6, BRA: 5, COS: 4, SWI: 1
(0, 1, 0, -1)            *ADVANCE* SWI: 5, BRA: 5, SER: 4, COS: 1
(0, 1, 0, 0)             *ADVANCE* BRA: 5, SER: 4, SWI: 3, COS: 2
(0, 1, 0, 1)     2nd Tie *ADVANCE* BRA: 5, SER: 4, COS: 4, SWI: 2
(0, 1, 1, -1)            *ADVANCE* SWI: 7, BRA: 5, SER: 3, COS: 1
(0, 1, 1, 0)             *ADVANCE* SWI: 5, BRA: 5, SER: 3, COS: 2
(0, 1, 1, 1)     2nd Tie *ADVANCE* BRA: 5, SWI: 4, COS: 4, SER: 3
(1, -1, -1, -1)  2nd Tie _go home_ SER: 9, SWI: 4, BRA: 4, COS: 0
(1, -1, -1, 0)           *ADVANCE* SER: 9, BRA: 4, SWI: 2, COS: 1
(1, -1, -1, 1)           *ADVANCE* SER: 9, BRA: 4, COS: 3, SWI: 1
(1, -1, 0, -1)           _go home_ SER: 7, SWI: 5, BRA: 4, COS: 0
(1, -1, 0, 0)            *ADVANCE* SER: 7, BRA: 4, SWI: 3, COS: 1
(1, -1, 0, 1)            *ADVANCE* SER: 7, BRA: 4, COS: 3, SWI: 2
(1, -1, 1, -1)           _go home_ SWI: 7, SER: 6, BRA: 4, COS: 0
(1, -1, 1, 0)            _go home_ SER: 6, SWI: 5, BRA: 4, COS: 1
(1, -1, 1, 1)    2nd Tie _go home_ SER: 6, SWI: 4, BRA: 4, COS: 3
(1, 0, -1, -1)           *ADVANCE* SER: 7, BRA: 5, SWI: 4, COS: 0
(1, 0, -1, 0)            *ADVANCE* SER: 7, BRA: 5, SWI: 2, COS: 1
(1, 0, -1, 1)            *ADVANCE* SER: 7, BRA: 5, COS: 3, SWI: 1
(1, 0, 0, -1)    2nd Tie _go home_ SWI: 5, SER: 5, BRA: 5, COS: 0
(1, 0, 0, 0)             *ADVANCE* SER: 5, BRA: 5, SWI: 3, COS: 1
(1, 0, 0, 1)             *ADVANCE* SER: 5, BRA: 5, COS: 3, SWI: 2
(1, 0, 1, -1)            *ADVANCE* SWI: 7, BRA: 5, SER: 4, COS: 0
(1, 0, 1, 0)             *ADVANCE* SWI: 5, BRA: 5, SER: 4, COS: 1
(1, 0, 1, 1)     2nd Tie *ADVANCE* BRA: 5, SWI: 4, SER: 4, COS: 3
(1, 1, -1, -1)           *ADVANCE* BRA: 7, SER: 6, SWI: 4, COS: 0
(1, 1, -1, 0)            *ADVANCE* BRA: 7, SER: 6, SWI: 2, COS: 1
(1, 1, -1, 1)            *ADVANCE* BRA: 7, SER: 6, COS: 3, SWI: 1
(1, 1, 0, -1)            *ADVANCE* BRA: 7, SWI: 5, SER: 4, COS: 0
(1, 1, 0, 0)             *ADVANCE* BRA: 7, SER: 4, SWI: 3, COS: 1
(1, 1, 0, 1)             *ADVANCE* BRA: 7, SER: 4, COS: 3, SWI: 2
(1, 1, 1, -1)            *ADVANCE* SWI: 7, BRA: 7, SER: 3, COS: 0
(1, 1, 1, 0)             *ADVANCE* BRA: 7, SWI: 5, SER: 3, COS: 1
(1, 1, 1, 1)             *ADVANCE* BRA: 7, SWI: 4, SER: 3, COS: 3
'BRA in' in a total of 32 out of 81 scenarios


>>> simulate(True)

# OPTIMISTIC = TRUE
(Brazil's goal difference beats everyone else)


Current Standings
SER: 3
SWI: 1
COS: 0
BRA: 1

Matches:

COS X BRA , SERV X BRA , SERV X SWI , SWI X COS

-1 means the left team wins
 0 means a tie
 1 means the right team wins

Optimistic? (assume in point ties Brazil comes ahead) True

(-1, -1, -1, -1)         _go home_ SER: 9, SWI: 4, COS: 3, BRA: 1
(-1, -1, -1, 0)          _go home_ SER: 9, COS: 4, SWI: 2, BRA: 1
(-1, -1, -1, 1)          _go home_ SER: 9, COS: 6, BRA: 1, SWI: 1
(-1, -1, 0, -1)          _go home_ SER: 7, SWI: 5, COS: 3, BRA: 1
(-1, -1, 0, 0)           _go home_ SER: 7, COS: 4, SWI: 3, BRA: 1
(-1, -1, 0, 1)           _go home_ SER: 7, COS: 6, SWI: 2, BRA: 1
(-1, -1, 1, -1)          _go home_ SWI: 7, SER: 6, COS: 3, BRA: 1
(-1, -1, 1, 0)           _go home_ SER: 6, SWI: 5, COS: 4, BRA: 1
(-1, -1, 1, 1)           _go home_ COS: 6, SER: 6, SWI: 4, BRA: 1
(-1, 0, -1, -1)          _go home_ SER: 7, SWI: 4, COS: 3, BRA: 2
(-1, 0, -1, 0)           _go home_ SER: 7, COS: 4, BRA: 2, SWI: 2
(-1, 0, -1, 1)           _go home_ SER: 7, COS: 6, BRA: 2, SWI: 1
(-1, 0, 0, -1)           _go home_ SER: 5, SWI: 5, COS: 3, BRA: 2
(-1, 0, 0, 0)            _go home_ SER: 5, COS: 4, SWI: 3, BRA: 2
(-1, 0, 0, 1)            _go home_ COS: 6, SER: 5, BRA: 2, SWI: 2
(-1, 0, 1, -1)           _go home_ SWI: 7, SER: 4, COS: 3, BRA: 2
(-1, 0, 1, 0)    2nd Tie _go home_ SWI: 5, COS: 4, SER: 4, BRA: 2
(-1, 0, 1, 1)    2nd Tie _go home_ COS: 6, SER: 4, SWI: 4, BRA: 2
(-1, 1, -1, -1)  2nd Tie *ADVANCE* SER: 6, BRA: 4, SWI: 4, COS: 3
(-1, 1, -1, 0)   2nd Tie *ADVANCE* SER: 6, BRA: 4, COS: 4, SWI: 2
(-1, 1, -1, 1)           _go home_ COS: 6, SER: 6, BRA: 4, SWI: 1
(-1, 1, 0, -1)   2nd Tie *ADVANCE* SWI: 5, BRA: 4, SER: 4, COS: 3
(-1, 1, 0, 0)    2nd Tie *ADVANCE* BRA: 4, COS: 4, SER: 4, SWI: 3
(-1, 1, 0, 1)    2nd Tie *ADVANCE* COS: 6, BRA: 4, SER: 4, SWI: 2
(-1, 1, 1, -1)           *ADVANCE* SWI: 7, BRA: 4, COS: 3, SER: 3
(-1, 1, 1, 0)    2nd Tie *ADVANCE* SWI: 5, BRA: 4, COS: 4, SER: 3
(-1, 1, 1, 1)    2nd Tie *ADVANCE* COS: 6, BRA: 4, SWI: 4, SER: 3
(0, -1, -1, -1)          _go home_ SER: 9, SWI: 4, BRA: 2, COS: 1
(0, -1, -1, 0)   2nd Tie *ADVANCE* SER: 9, BRA: 2, COS: 2, SWI: 2
(0, -1, -1, 1)           _go home_ SER: 9, COS: 4, BRA: 2, SWI: 1
(0, -1, 0, -1)           _go home_ SER: 7, SWI: 5, BRA: 2, COS: 1
(0, -1, 0, 0)            _go home_ SER: 7, SWI: 3, BRA: 2, COS: 2
(0, -1, 0, 1)            _go home_ SER: 7, COS: 4, BRA: 2, SWI: 2
(0, -1, 1, -1)           _go home_ SWI: 7, SER: 6, BRA: 2, COS: 1
(0, -1, 1, 0)            _go home_ SER: 6, SWI: 5, BRA: 2, COS: 2
(0, -1, 1, 1)    2nd Tie _go home_ SER: 6, COS: 4, SWI: 4, BRA: 2
(0, 0, -1, -1)           _go home_ SER: 7, SWI: 4, BRA: 3, COS: 1
(0, 0, -1, 0)            *ADVANCE* SER: 7, BRA: 3, COS: 2, SWI: 2
(0, 0, -1, 1)            _go home_ SER: 7, COS: 4, BRA: 3, SWI: 1
(0, 0, 0, -1)            _go home_ SER: 5, SWI: 5, BRA: 3, COS: 1
(0, 0, 0, 0)     2nd Tie *ADVANCE* SER: 5, BRA: 3, SWI: 3, COS: 2
(0, 0, 0, 1)             _go home_ SER: 5, COS: 4, BRA: 3, SWI: 2
(0, 0, 1, -1)            _go home_ SWI: 7, SER: 4, BRA: 3, COS: 1
(0, 0, 1, 0)             _go home_ SWI: 5, SER: 4, BRA: 3, COS: 2
(0, 0, 1, 1)     2nd Tie _go home_ COS: 4, SER: 4, SWI: 4, BRA: 3
(0, 1, -1, -1)           *ADVANCE* SER: 6, BRA: 5, SWI: 4, COS: 1
(0, 1, -1, 0)            *ADVANCE* SER: 6, BRA: 5, COS: 2, SWI: 2
(0, 1, -1, 1)            *ADVANCE* SER: 6, BRA: 5, COS: 4, SWI: 1
(0, 1, 0, -1)            *ADVANCE* BRA: 5, SWI: 5, SER: 4, COS: 1
(0, 1, 0, 0)             *ADVANCE* BRA: 5, SER: 4, SWI: 3, COS: 2
(0, 1, 0, 1)     2nd Tie *ADVANCE* BRA: 5, COS: 4, SER: 4, SWI: 2
(0, 1, 1, -1)            *ADVANCE* SWI: 7, BRA: 5, SER: 3, COS: 1
(0, 1, 1, 0)             *ADVANCE* BRA: 5, SWI: 5, SER: 3, COS: 2
(0, 1, 1, 1)     2nd Tie *ADVANCE* BRA: 5, COS: 4, SWI: 4, SER: 3
(1, -1, -1, -1)  2nd Tie *ADVANCE* SER: 9, BRA: 4, SWI: 4, COS: 0
(1, -1, -1, 0)           *ADVANCE* SER: 9, BRA: 4, SWI: 2, COS: 1
(1, -1, -1, 1)           *ADVANCE* SER: 9, BRA: 4, COS: 3, SWI: 1
(1, -1, 0, -1)           _go home_ SER: 7, SWI: 5, BRA: 4, COS: 0
(1, -1, 0, 0)            *ADVANCE* SER: 7, BRA: 4, SWI: 3, COS: 1
(1, -1, 0, 1)            *ADVANCE* SER: 7, BRA: 4, COS: 3, SWI: 2
(1, -1, 1, -1)           _go home_ SWI: 7, SER: 6, BRA: 4, COS: 0
(1, -1, 1, 0)            _go home_ SER: 6, SWI: 5, BRA: 4, COS: 1
(1, -1, 1, 1)    2nd Tie *ADVANCE* SER: 6, BRA: 4, SWI: 4, COS: 3
(1, 0, -1, -1)           *ADVANCE* SER: 7, BRA: 5, SWI: 4, COS: 0
(1, 0, -1, 0)            *ADVANCE* SER: 7, BRA: 5, SWI: 2, COS: 1
(1, 0, -1, 1)            *ADVANCE* SER: 7, BRA: 5, COS: 3, SWI: 1
(1, 0, 0, -1)    2nd Tie *ADVANCE* BRA: 5, SER: 5, SWI: 5, COS: 0
(1, 0, 0, 0)             *ADVANCE* BRA: 5, SER: 5, SWI: 3, COS: 1
(1, 0, 0, 1)             *ADVANCE* BRA: 5, SER: 5, COS: 3, SWI: 2
(1, 0, 1, -1)            *ADVANCE* SWI: 7, BRA: 5, SER: 4, COS: 0
(1, 0, 1, 0)             *ADVANCE* BRA: 5, SWI: 5, SER: 4, COS: 1
(1, 0, 1, 1)     2nd Tie *ADVANCE* BRA: 5, SER: 4, SWI: 4, COS: 3
(1, 1, -1, -1)           *ADVANCE* BRA: 7, SER: 6, SWI: 4, COS: 0
(1, 1, -1, 0)            *ADVANCE* BRA: 7, SER: 6, SWI: 2, COS: 1
(1, 1, -1, 1)            *ADVANCE* BRA: 7, SER: 6, COS: 3, SWI: 1
(1, 1, 0, -1)            *ADVANCE* BRA: 7, SWI: 5, SER: 4, COS: 0
(1, 1, 0, 0)             *ADVANCE* BRA: 7, SER: 4, SWI: 3, COS: 1
(1, 1, 0, 1)             *ADVANCE* BRA: 7, SER: 4, COS: 3, SWI: 2
(1, 1, 1, -1)            *ADVANCE* BRA: 7, SWI: 7, SER: 3, COS: 0
(1, 1, 1, 0)             *ADVANCE* BRA: 7, SWI: 5, SER: 3, COS: 1
(1, 1, 1, 1)             *ADVANCE* BRA: 7, SWI: 4, COS: 3, SER: 3
'BRA in' in a total of 44 out of 81 scenarios
"""
