description = """
Blueberry (Indigo)
Coconut (White)
Grape (Purple)
Kiwi (Dark Green)
Lemon (Green)
Orange (Orange)
Pineapple (Yellow)
Strawberry (Red)

For each gumdrop, if it is the first time its flavor is seen, it will be given 128 tastiness points.

If its flavor is the same as the immediately preceding gumdrop, it is given half the number of points given to this previous gumdrop.

If its flavor has already appeared, but does not match the flavor of the immediately preceding gumdrop, it is given the amount of points already given to the nearest gumdrop of this flavor.

Return the total number of tastiness points of the entire 8-gumdrop roll.
"""

def gumdropTastiness(roll):
    scores = {"B": 128,
              "C": 128,
              "G": 128,
              "K": 128,
              "L": 128,
              "O": 128,
              "P": 128,
              "S": 128,
    }

    if len(roll) != 8:
        raise ValueError("not a valid length")
    
    for c in roll:
        if c not in scores.keys():
            raise ValueError("gumdrop not a flavor")

    tot = 128
    for i in range(1, 8):
        if roll[i] == roll[i-1]:
            scores[roll[i]] //= 2
        tot += scores[roll[i]]
    return tot


pairtest(gumdropTastiness("CGKPOLSB"), 1024,
         gumdropTastiness("SSSSSSSS"), 255,
         gumdropTastiness("SCCLSCPP"), 832,
         gumdropTastiness("GSSPGGLO"), 896,
         gumdropTastiness("CCCOKKCC"), 592,
         gumdropTastiness("PSLKGGOB"), 960,
         gumdropTastiness("GCBKLLOL"), 896,
         gumdropTastiness("LLLLOOOL"), 480)
