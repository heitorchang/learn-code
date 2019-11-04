#

from collections import defaultdict

def midnightOil(alertLevel, coffee, candy):
    MAX_ALERT = 100
    
    JAVA = 15
    JAVA_WAIT = 20
    JAVA_IN_BELLY = False
    
    MARS = 10
    MARS_WAIT = 15
    MARS_IN_BELLY = False

    time = 0
    
    javas = defaultdict(int)
    marses = defaultdict(int)

    pending = 0  # alertness consumed but not yet activated
    
    while True:
        # print("time", time, "alert", alertLevel, marses)

        # alertness boost is the priority
        if javas[time]:
            alertLevel = min(100, alertLevel + javas[time])
            pending -= javas[time]
            JAVA_IN_BELLY = False

        if marses[time]:
            alertLevel = min(100, alertLevel + marses[time])
            pending -= marses[time]
            MARS_IN_BELLY = False

        # See if we should consume something
        if (alertLevel + pending) <= (MAX_ALERT - JAVA) and coffee > 0 and not JAVA_IN_BELLY:
            print("Consume JAVA", time)
            coffee -= 1
            javas[time + JAVA_WAIT] = JAVA
            JAVA_IN_BELLY = True

        if (alertLevel + pending) <= (MAX_ALERT - MARS) and candy > 0 and not MARS_IN_BELLY:
            print("Consume MARS", time)
            candy -= 1
            marses[time + MARS_WAIT] = MARS
            MARS_IN_BELLY = True

        if alertLevel == 0:
            return time
            
        # time takes its toll
        alertLevel -= 1        
        time += 1


def midnightOilDummy(a, j, m):
    return a + 15 * j + 10 * m
    

test(
    midnightOil(10, 0, 0), 10,
    midnightOil(50, 1, 0), 65,
    midnightOil(5, 9, 9), 5,
    midnightOil(90, 1, 1), 115,
    midnightOil(15, 0, 1), 25,
    midnightOil(20, 0, 2), 40,
    midnightOil(50, 5, 0), 50 + 5 * 15,
    )

# test(midnightOil(20, 0, 2), 40)

test(
    midnightOilDummy(10, 0, 0), 10,
    midnightOilDummy(50, 1, 0), 65,
    midnightOilDummy(5, 9, 9), 5,
    midnightOilDummy(90, 1, 1), 115,
    midnightOilDummy(15, 0, 1), 25,
    midnightOilDummy(20, 0, 2), 40,
    midnightOilDummy(50, 5, 0), 50 + 5 * 15,
    )
