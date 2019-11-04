description = """

A robot battle tournament is underway!

You have seen hundreds of robot battles in your career and know exactly what will happen (so you will bet thousands of RoboDollars and be certain you will win).

You measure the *Winning Energy* of each competing robot with your top-secret scope, and know that the robot with more energy will win, but its energy level will decrease by exactly how much energy its opponent had. 

If two robots have the same initial level of energy, the battle will end in a draw, but judges will give the victory to the one listed first (towards the left of the list). The more stylish robots got assigned their places first in the list and are more appealing to the audience.

Your task is to determine the index (0-based) of who you know will be the robot champion (out of the initial list), so you can bet on it and win thousands more RoboDollars.

__Example__

In the diagram below, the input 

`bracket: [100, 25, 92, 22, 30, 30, 29, 22]` is shown vertically.

Battles proceed left to right.

For each round of battles, the winning robot's index is given inside square brackets and its remaining energy level.

```
[0] 100
     vs. [0] 75 
[1] 25
 
             vs. [0] 5
			  
[2] 92
     vs. [2] 70
[3] 22

          CHAMPION: [6] 2

[4] 30
     vs. [4] 0
[5] 30

             vs. [6] 7

[6] 29
     vs. [6] 7
[7] 22
```

Robot `[6]` who initially had 29 energy, wins, so return `6`.

"""


from collections import namedtuple

Robot = namedtuple("Robot", "index energy")

def fight(a, b):
    if a.energy >= b.energy:
        return Robot(a.index, a.energy - b.energy)
    else:
        return Robot(b.index, b.energy - a.energy)
    

def tourneyOfAttrition(bracket):
    robots = [Robot(i, e) for i, e in enumerate(bracket)]

    while len(robots) > 1:
        nextRound = []
        for i in range(0, len(robots), 2):
            nextRound.append(fight(robots[i], robots[i+1]))
        robots = nextRound
    print(robots[0].energy)
    return robots[0].index



pairtest(tourneyOfAttrition([100, 25, 92, 22, 30, 30, 29, 22]), 6,
         tourneyOfAttrition([0, 0, 0, 0]), 0,
         tourneyOfAttrition([1, 1, 0, 0]), 0,
         tourneyOfAttrition([0, 0, 1, 4, 2, 5, 9, 100]), 7)
