description = """

https://app.codesignal.com/challenge/5LLcpXLm9BgCAbpAW

You're practicing your [long drive](https://en.wikipedia.org/wiki/Drive_(golf)) with your pal who plays golf very accurately.

For each hole, your pal will always go first, and instead of taking turns, he will keep on playing until his ball goes into the hole.

Your challenge is to score a hole-in-one, and from your experience, you know that you can guarantee accuracy up to a distance of `300` meters.

There is no wind and no kind of obstacle between the tee and the hole.

Each test case will be a matrix of floats. A row of this array is one of your pal's strokes, in order that he played.

Each stroke is represented in [polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system), starting from the initial point of the stroke to the point where the ball stops. Overall, the very first point is the tee, and the last point is the hole.

In this representation, the first number is the distance (in meters) the ball traveled and the second number is the direction the ball traveled in degrees relative to the cardinal points (East, North, West and South). Combining cartographic and mathematical conventions, `0` degrees is East, `90` degrees is North, `180` degrees is West, and `270` degrees is South.

Your task is to output a Boolean, telling whether you can score a hole-in-one. In other words, is the straight-line distance from the tee to the hole less than or equal to `300` meters?

"""


import random
from math import cos, sin, radians, hypot

def genR(lim):
    return round(random.uniform(30, lim), 2)

def genInit():
    return round(random.uniform(0, 360))
    
def generateTrueTestCase():
    out = []

    initTh = genInit()
    initR = genR(120)
    
    out.append([initR, initTh])
    
    while holeInOne(out) < 300.0:
        out.append([genR(60), out[-1][-1] + round(random.uniform(-30, 30), 1)])

    return out[:-1]

def generateFalseTestCase():
    out = []

    initTh = genInit()
    initR = genR(120)
    
    out.append([initR, initTh])
    
    while holeInOne(out) < 450.0:
        out.append([genR(60), out[-1][-1] + round(random.uniform(-30, 30), 1)])

    return out


def generateNonsenseLim(limr):
    out = []

    initTh = genInit()
    initR = genR(90)
    
    out.append([initR, initTh])
    
    while holeInOne(out) < limr:
        out.append([genR(100), (out[-1][-1] + round(random.uniform(-60, 90), 1)) % 360])
        
    return out
    
    
def generateTrueTestCase2():
    out = []

    initTh = genInit()
    initR = genR(120)
    
    out.append([initR, initTh])
    
    while holeInOne(out) < 300.0:
        out.append([genR(60), out[-1][-1] + round(random.uniform(-20, 90), 1)])

    return out[:-1]

    

from math import cos, sin, radians, hypot
    

def holeInOne(palStrokes):
    curX = 0.0
    curY = 0.0
    
    for s in palStrokes:
        x = s[0] * cos(radians(s[1]))
        y = s[0] * sin(radians(s[1]))

        curX += x
        curY += y
        
    h = hypot(curX, curY)
    print("%.2f" % h)
    # return h <= 300.0
    return h
    
# T F F F T T
