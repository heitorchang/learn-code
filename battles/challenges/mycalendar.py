from datetime import date

def daysInFeb(y):
    if y == 2100:
        return 28
    if y % 4 == 0:
        return 29
    return 28

def calendar(m, y):
    firstDay = date(y, m, 1)
    # monday is 0, while in the description sunday should be 0
    curWkday = firstDay.weekday() + 1
    if curWkday == 7:
        curWkday = 0
    cal = [wk[:] for wk in [[0] * 7] * 6]
    days = [0, 31, daysInFeb(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    limit = days[m]
    for i in range(1, limit+1):
        cal[curWkday // 7][curWkday % 7] = i
        curWkday += 1
    return cal
           
def test():
    testeql(calendar(5, 2017), [[0,1,2,3,4,5,6], 
 [7,8,9,10,11,12,13], 
 [14,15,16,17,18,19,20], 
 [21,22,23,24,25,26,27], 
 [28,29,30,31,0,0,0], 
 [0,0,0,0,0,0,0]])
