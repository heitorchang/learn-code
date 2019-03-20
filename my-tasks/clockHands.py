from operator import itemgetter

# at what times are the two hands closest together?

def handAngles(hrs, mins):
    """12 o'clock is 0, 3 o'clock is 90"""
    minHand = 360 * (mins / 60)

    hrHand = 360 * (hrs / 12) + 30 * (mins / 60)

    return (hrHand, minHand)


def closest():
    ans = []
    for h in range(12):
        for m in range(60):
            angles = handAngles(h, m)
            ans.append(((h, m), abs(angles[0] - angles[1])))
    ans.sort(key=itemgetter(1))

    # for t in ans:
    #     print("{}:{} {}".format(t[0][0], t[0][1], t[1]))
        
    return ans


def perHour():
    allTimes = closest()
    byHour = [-1] * 12
    for i in range(12):
        # brute force
        for t in allTimes:
            if t[0][0] == i:
                if byHour[i] == -1:
                    byHour[i] = t[0][1]
                else:
                    break
    return byHour
        

pairtest(handAngles(3, 0), (90, 0),
         handAngles(0, 15), (30/4, 90),

         handAngles(6, 30), (180 + 15, 180))
