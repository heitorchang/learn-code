description = """

After an exhausting day working with spreadsheets, you realize you replaced seven columns of sales data with the calendar's days corresponding to that month!

You only saved the totals for those columns, and now you have to figure out **which day of the week was the first day of that month**.

Given the totals for these seven columns (the week starts on **Monday**), figure out which day of the week it was on the first day of that month (return an integer, such that 0=Monday, 1=Tuesday, 2=Wednesday, ..., 6=Sunday).

__Example__

You have this month's calendar handy (Feb. 2019), and adding the totals, we get


```
      February
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28
--------------------
58 62 66 70 46 50 54 (Totals)
```

So, for `weekdayTotals` = `[58, 62, 66, 70, 46, 50, 54]`, you should output `4` (Friday).

"""


from datetime import date
from calendar import day_name, monthrange
from collections import defaultdict

s = [sum([7,14,21,28]), sum([1,8,15,22,29]), sum([2,9,16,23,30]), sum([3,10,17,24,31]), sum([4,11,18,25]), sum([5,12,19,26]), sum([6,13,20,27])]


def minindex(a):
    m = min(a)
    return a.index(m)
    

def generateTestCase(year, month):
    lastday = monthrange(year, month)[1]

    totals = [0] * 7
    
    for i in range(1, lastday+1):
        d = date(year, month, i)
        totals[d.weekday()] += i

    print(year, month, totals)

    lom = date(year, month, lastday)
    print("ans:", lom.weekday(), totals[lom.weekday()])
    # print('minindex:', minindex(totals))
    # if minindex(totals) == fom.weekday():
    #     print("match")
    return totals


def generateTestCaseTot(year, month):
    lastday = monthrange(year, month)[1]

    totals = [0] * 7
    
    for i in range(1, lastday+1):
        d = date(year, month, i)
        totals[d.weekday()] += i

    print(year, month, totals)

    lom = date(year, month, lastday)
    print("ans:", totals[lom.weekday()])
    # print('minindex:', minindex(totals))
    # if minindex(totals) == fom.weekday():
    #     print("match")
    return totals[lom.weekday()]
    

    
def xlsLastOfMonth(weekdayTotals):
    tot = sum(weekdayTotals)
    if tot == 496:
        lastday = 31
    elif tot == 465:
        lastday = 30
    elif tot == 435:
        lastday = 29
    else:
        lastday = 28

    print("last day:", lastday)
    
    for firstday in range(7):
        cal = [0] * 7
        for i in range(1, lastday+1):
            cal[(firstday + i - 1) % 7] += i
            
        if cal == weekdayTotals:
            return (firstday + lastday) % 7

    return "blarg"


def exhaust():
    s = set()
    for lastday in range(28, 32):
        for firstday in range(7):
            cal = [0] * 7
            for i in range(1, lastday+1):
                cal[(firstday + i - 1) % 7] += i
            
            s.add(tuple(cal))
            
    return len(s)

    
test(

    firstOfMonth(generateTestCase(2018, 1)), "Monday",
    firstOfMonth(generateTestCase(2018, 2)), "Thursday",
    firstOfMonth(generateTestCase(2018, 3)), "Thursday",
    firstOfMonth(generateTestCase(2018, 4)), "Sunday",
    firstOfMonth(generateTestCase(2018, 5)), "Tuesday",
    firstOfMonth(generateTestCase(2018, 6)), "Friday",
    firstOfMonth(generateTestCase(2018, 7)), "Sunday",
    firstOfMonth(generateTestCase(2018, 8)), "Wednesday",
    firstOfMonth(generateTestCase(2018, 9)), "Saturday",
    firstOfMonth(generateTestCase(2018, 10)), "Monday",
    firstOfMonth(generateTestCase(2018, 11)), "Thursday",
    firstOfMonth(generateTestCase(2018, 12)), "Saturday",

    firstOfMonth(generateTestCase(2016, 1)), "Friday",
    firstOfMonth(generateTestCase(2016, 2)), "Monday",
    firstOfMonth(generateTestCase(2016, 3)), "Tuesday",
    firstOfMonth(generateTestCase(2016, 4)), "Friday",
    firstOfMonth(generateTestCase(2016, 5)), "Sunday",
    firstOfMonth(generateTestCase(2016, 6)), "Wednesday",
    firstOfMonth(generateTestCase(2016, 7)), "Friday",
    firstOfMonth(generateTestCase(2016, 8)), "Monday",
    firstOfMonth(generateTestCase(2016, 9)), "Thursday",
    firstOfMonth(generateTestCase(2016, 10)), "Saturday",
    firstOfMonth(generateTestCase(2016, 11)), "Tuesday",
    firstOfMonth(generateTestCase(2016, 12)), "Thursday",

    firstOfMonth(generateTestCase(2017, 1)), "Sunday",
    firstOfMonth(generateTestCase(2017, 2)), "Wednesday",
    firstOfMonth(generateTestCase(2017, 3)), "Wednesday",
    firstOfMonth(generateTestCase(2017, 4)), "Saturday",
    firstOfMonth(generateTestCase(2017, 5)), "Monday",
    firstOfMonth(generateTestCase(2017, 6)), "Thursday",
    firstOfMonth(generateTestCase(2017, 7)), "Saturday",
    firstOfMonth(generateTestCase(2017, 8)), "Tuesday",
    firstOfMonth(generateTestCase(2017, 9)), "Friday",
    firstOfMonth(generateTestCase(2017, 10)), "Sunday",
    firstOfMonth(generateTestCase(2017, 11)), "Wednesday",
    firstOfMonth(generateTestCase(2017, 12)), "Friday",
    

)


def generateTestCases():
    anss = set()
    for year in range(2015, 2020):
        for month in range(1, 13):
            print()
            print()
            print("Y/M",year,month)
            anss.add(generateTestCase(year, month))

    return anss
