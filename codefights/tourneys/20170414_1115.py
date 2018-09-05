def digitalNumber(k):
    #      0  1  2  3  4  5  6  7  8  9
    seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def gravitation(rows):

    minTimer = len(rows)
    answer = []
    for i in range(len(rows[0])):
        finish = len(rows) - 1
        timer = 0
        for j in range(len(rows) - 1, -1, -1):
            if rows[j][i] == '#':
                timer = j - finish
                finish -= 1
        if timer == minTimer:
            answer.append(i)
        if timer < minTimer:
            minTimer = timer
            answer = [i]
    return answer


def test():
    testeql(digitalNumber(0), 0)
    testeql(gravitation(["#..##", 
 ".##.#", 
 ".#.##", 
 "....."]), [1,4])
