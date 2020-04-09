desc = """
There is no shortage of fight against the coronavirus, but funds are drying up rapidly.

The Minister of Health hopes to convince the intransigent president to free up more federal money and bolster the coronavirus-fighting efforts.

To this end, the Minister is asking your help (once more) in analyzing the statistics for multiple cities. By convincing the government that a city is in trouble, you are more likely to receive aid, and on the contrary, if you can correlate working policies to decreasing rates of contagion, your credibility will rise.

You will be given the daily cumulative total of the number of victims as an array of integers, where one element represents a single day. This array will always be the data for the last 15 days.

From these numbers, you are to compute the geometric ratio between consecutive days (in other words, `A[i] / A[i-1]` where `i > 0` is an index of the array).

Because lives are at stake, we wish to err on the side of caution. You are to classify the epidemic activity of the city as one of these, in order of priority:

* uncontrolled_growth
* growing
* stable
* reducing

These criteria are to be based on averages because of erratic fluctuations from day to day.

Once you have the daily geometric ratios, we define two new values, called `olderAverage`, which is the average of the first seven ratios (corresponding to two weeks ago) and `newerAverage`, the average of the remaining seven values (last week).

If both averages are above `1.25`, the city has `uncontrolled_growth`. No matter in which direction things seem to be progressing, things look bad. Return the string `"uncontrolled_growth"`.

Otherwise, the other labels will apply:

If `newerAverage` is at least `0.1` higher than `olderAverage`, the epidemic's situation is `"growing"`.

If the absolute difference between `newerAverage` and `olderAverage` is less than `0.1`, the city is `"stable"`.

If `newerAverage` is at least `0.1` less than `olderAverage`, the epidemic is `"reducing"`.

__Example__

The cumulative number of victims in the last 15 days, in the state of São Paulo is:

`dailyVictims: [9,15,22,30,40,48,58,68,84,98,113,136,164,188,219]`.

From these numbers (all floats are rounded to 2 decimal places) the geometric ratios are:

`[1.67, 1.47, 1.36, 1.33, 1.20, 1.21, 1.17, 1.24, 1.17, 1.15, 1.20, 1.21, 1.15, 1.16]`

and the `olderAverage` and `newerAverage` values are:

`1.344, 1.182`.

The absolute value of the difference is `0.162`, so we conclude the epidemic is `"decreasing"` and return this string.
"""

from statistics import mean

def epidemicGrowth(dailyVictims):
    dailyVictims = dailyVictims[-15:]
    assert len(dailyVictims) == 15
    ratios = [b/a for a, b in zip(dailyVictims, dailyVictims[1:])]
    newerAverage = mean(ratios[7:])
    olderAverage = mean(ratios[:7])
    absdiff = abs(newerAverage - olderAverage)
    print(olderAverage, newerAverage)
    if newerAverage > 1.25 and olderAverage > 1.25:
        return "uncontrolled growth"
    elif newerAverage - olderAverage > 0.1:
        return "growing"
    elif olderAverage - newerAverage > 0.1:
        return "reducing"
    else:
        return "stable"
        
# real data ends at 219

from random import random

def randlim(lim):
    while True:
        val = random()
        if val < lim:
            return val
        
def generateTestData(init, rate):
    out = [init]
    for i in range(14):
        out.append(int(out[-1] * (1 + randlim(rate))))
    return out

print(epidemicGrowth([9,15,22,30,40,48,58,68,84,98,113,136,164,188,219,260,275,304,371,428,496]))
print(epidemicGrowth([120, 136, 179, 217, 263, 283, 345, 425, 527, 681, 695, 760, 829, 904, 1187]))
print(epidemicGrowth([25, 28, 42, 50, 74, 79, 92, 142, 157, 225, 275, 400, 501, 580, 873]))
print(epidemicGrowth([120, 122, 142, 160, 161, 162, 175, 204, 236, 258, 280, 296, 354, 419, 499]))
print(epidemicGrowth([923, 955, 990, 997, 1014, 1030, 1072, 1100, 1140, 1143, 1166, 1196, 1208, 1246, 1261]))
print(epidemicGrowth([39, 48, 63, 83, 101, 108, 123, 127, 192, 239, 310, 393, 490, 648, 957]))
print(generateTestData(923, 0.05))
