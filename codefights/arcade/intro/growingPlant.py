def growingPlant(upSpeed, downSpeed, desiredHeight):
    day = 0
    ht = 0
    while True:
        ht += upSpeed
        day += 1
        if ht >= desiredHeight:
            return day
        ht -= downSpeed

def test():
    testeql(growingPlant(100,10,910), 10)
    testeql(growingPlant(10, 9, 4), 1)
