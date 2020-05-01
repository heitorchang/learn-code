description = """
Signalia University's students are so methodical that they posted a sign-up sheet for using the laundry room.

Given the number of `washingMachines` and `dryers` as integers, and the sign-up sheet of student `arrivals` times (an array of strings in the format `hour:minute` without leading zeros), determine when the last student will have finished doing his or her laundry.

* Washing takes 30 minutes
* Drying takes 45 minutes
* Assume that the laundry room is empty at the moment the first student walks in
* Also assume that unloading and loading machines is instantaneous.
"""

from collections import deque

def time2mins(t):
    parts = t.split(":")
    return int(parts[0]) * 60 + int(parts[1])

def mins2time(m):
    h = m // 60
    mm = m % 60
    return "%d:%02d" % (h, mm)


def laundryRoom(washingMachines, dryers, arrivals):
    arrivals.sort()
    arr = deque(map(time2mins, arrivals))
    wwait = arr
    dwait = deque()

    tm = arr[0]
    wmach = deque()
    dmach = deque()
    done = 0
    
    # load washingMachines
    while True:
        if len(wwait) == 0 and len(wmach) == 0 and len(dwait) == 0 and len(dmach) == 0:
            return mins2time(done)
        
        while True:
            moved = False
            if wwait and wwait[0] <= tm and len(wmach) < washingMachines:
                wmach.append(tm + 30)
                wwait.popleft()
                moved = True
            if wmach and wmach[0] <= tm:
                dwait.append(tm)
                wmach.popleft()
                moved = True
            if dwait and dwait[0] <= tm and len(dmach) < dryers:
                dmach.append(tm + 45)
                dwait.popleft()
                moved = True
            if dmach and dmach[0] <= tm:
                done = max(done, tm)
                dmach.popleft()
                moved = True
            if not moved:
                break
            
        tm += 1
        if tm > 700:
            print("Time exceeded working hours")
            return None
    
pairtest(
    laundryRoom(2, 2, ["1:00", "1:15", "1:15"]), "3:00",  # 1
    laundryRoom(3, 2, ["1:00", "1:00", "1:15", "1:15", "1:30", "1:45", "2:00", "2:00"]), "4:30",  # 2
    laundryRoom(3, 5, ["2:00", "2:00", "2:00"]), "3:15",  # 3
    laundryRoom(2, 1, ["2:00", "2:00", "2:00", "2:00", "2:00"]), "6:15",  # 4
    laundryRoom(2, 1, ["7:15", "7:20", "7:30"]), "10:00",  # 5
    laundryRoom(1, 2, ["1:00", "1:15", "2:20"]), "3:35",  # 6
    laundryRoom(3, 3, ["1:00", "1:15", "3:00", "7:00"]), "8:15",  # 7
    laundryRoom(3, 3, ["1:15", "1:15", "1:30", "1:30", "1:30", "1:30", "1:30", "1:45", "2:00", "2:00", "2:00", "2:15", "2:15"]), "5:30",  # 8
    laundryRoom(3, 2, ["1:00", "1:15", "1:15", "1:30"]), "3:15",  # 9
    laundryRoom(3, 2, ["1:00", "1:15", "1:15", "1:30", "2:15"]), "3:45",  # 10
    laundryRoom(2, 1, ["2:00", "2:00", "2:00", "2:00", "6:00"]), "7:15",  # 11
    laundryRoom(7, 5, ["1:15", "1:20", "1:30", "1:30", "1:30", "1:30", "1:30", "1:45", "1:45", "1:45", "1:45", "1:55", "2:00", "2:15"]), "4:15",  # 12
    laundryRoom(1, 1, ["5:20", "6:20"]), "7:35",  # 13
    laundryRoom(1, 2, ["1:00", "1:15", "1:15", "1:30"]), "3:45",
)
