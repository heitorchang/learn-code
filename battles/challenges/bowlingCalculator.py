def frameBuilder(rolls):
    frames = [[] for i in range(10)]
    fptr = 0
    rptr = 0

    while rptr < len(rolls):
        frames[fptr].append(rolls[rptr])
        if fptr < 9 and (sum(frames[fptr]) == 10 or len(frames[fptr]) == 2):
            fptr += 1
        rptr += 1
    return frames


def frameScore(frames, i):
    if i == 9:
        if len(frames[9]) > 0:
            if frames[9][0] == 10:
                if len(frames[9]) != 3:
                    return 0
            if frames[9][0] + frames[9][1] == 10:
                if len(frames[9]) != 3:
                    return 0
        return sum(frames[9])
        
    else:
        if len(frames[i]) == 1 and frames[i][0] == 10:  # strike
            try:
                if len(frames[i+1]) > 1:
                    return 10 + sum(frames[i+1][:2])  # regular frame
                elif len(frames[i+1]) == 1:
                    if len(frames[i+2]) > 0:
                        return 10 + frames[i+1][0] + frames[i+2][0]
                    else:
                        return 0
                else:
                    return 0
            except IndexError:
                return 0
        elif sum(frames[i]) == 10:  # spare
            try:
                return 10 + frames[i+1][0]
            except IndexError:
                return 0
        else:
            return sum(frames[i])
            

def bowlingCalculator(rolls):
    frames = frameBuilder(rolls)
    tot = 0
    for i in range(len(frames)):
        tot += frameScore(frames, i)
    return tot
        
    

# [20, 10, 0, 5, 6, 20, 17, 7]              


test(
    bowlingCalculator([0, 10, 10, 0, 0, 5, 0, 1, 5, 10, 8, 2, 7]), 85,
    bowlingCalculator([1,2,3,4]), 10,
    bowlingCalculator([5, 1, 6, 2, 6, 2, 5, 1, 5, 2, 6, 2, 7, 3, 4, 4, 4, 0, 7, 3, 7]), 86,
    bowlingCalculator([10, 10, 10]), 30,
    bowlingCalculator([10, 1, 7, 3, 6, 6, 3, 4, 0, 10, 6, 1, 7, 0, 6, 0, 1, 9, 0]), 95,
    bowlingCalculator([3, 7, 7, 3, 8, 0, 9, 0, 7, 3, 7, 3, 9, 1, 7, 3, 7, 3, 6, 4, 6]), 154,
    bowlingCalculator([10, 6, 3, 8, 0, 3, 6, 10, 10, 6, 0, 7, 1, 8, 2, 10, 10, 8]), 149,
    bowlingCalculator([1, 9]), 0,
    bowlingCalculator([10, 6, 3, 8, 0, 3, 6, 10, 10, 6, 0, 7, 1, 8, 1, 10,  2, 8]), 130,
    bowlingCalculator([10, 6, 3, 8, 0, 3, 6, 10, 10, 6, 0, 7, 1, 8, 1, 1,   9, 8]), 128,
    bowlingCalculator([10, 6, 3, 8, 0, 3, 6, 10, 10, 6, 0, 7, 1, 8, 1, 10, 10, 8]), 138,
)

test(bowlingCalculator([10] * 12), 300)




