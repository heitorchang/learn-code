def test():
    testeql(parkingCost("12:20", "14:54"), 17)

def easyAssignmentProblem(skills):
    if skills[0][0] > skills[1][0]:
        return [1, 2]
    elif skills[0][0] < skills[1][0]:
        return [2, 1]
    else:
        if skills[0][1] > skills[1][1]:
            return [2, 1]
        else:
            return [1, 2]

def parkingCost(timeIn, timeOut):
    diff = (int(timeOut[:2]) * 60 +
        int(timeOut[3:]) -
        int(timeIn[:2]) * 60 -
        int(timeIn[3:]))
    if diff <= 30:
        return 0
    if diff <= 120:
        return (diff - 21) // 10  # 21
    return 10 + ((diff - 120) // 10) * 2 + 2
