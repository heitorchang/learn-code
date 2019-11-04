def tasksTypes(deadlines, day):
    today = [d for d in deadlines if d <= day]
    upcoming = [d for d in deadlines if day + 1 <= d <= day + 7]
    later = [d for d in deadlines if d > day + 7]
    return [len(today), len(upcoming), len(later)]

from collections import namedtuple
from operator import itemgetter

Person = namedtuple("Person", "name vacationStatus projects tasks")

def smartAssigning(names, statuses, projects, tasks):
    people = []
    for i in range(len(names)):
        statusInt = 1 if statuses[i] else 0
        people.append(Person(names[i], statusInt, projects[i], tasks[i]))
    sortedList = sorted(people, key=itemgetter(1, 3, 2))
    pr('sortedList')
    return(sortedList[0].name)

from datetime import datetime, timedelta

def getWkdy(s):
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return weekdays.index(s)

def dateWkdy(d):
    return int(d.strftime("%w"))

def recurringTask(firstDate, k, daysOfTheWeek, n):
    f = datetime.strptime(firstDate, "%d/%m/%Y")
    fwkday = dateWkdy(f)
    desiredWkdays = list(map(getWkdy, daysOfTheWeek))
    
    d = f
    datesAdded = 0
    result = []
    while n > 0:
        if dateWkdy(d) in desiredWkdays:
            result.append(d.strftime("%d/%m/%Y"))
            n -= 1
            datesAdded += 1
        if datesAdded % len(desiredWkdays) == 0:
            d = f + timedelta(weeks=k)
            f = d
        else:
            d += timedelta(days=1)
    return result
                    
def test():
    # testeql(tasksTypes([4, 14, 16], 7), [1,1,1])
    # testeql(smartAssigning(["John", "Martin"], [False, True], [2, 1], [6, 5]), "John")
    # testeql(smartAssigning(["John", "Martin"], [False, False], [2, 1], [16, 5]), "Martin")
    testeql(recurringTask("01/02/2100", 4, ["Sunday", "Monday"], 4), ["01/02/2100", 
                                                                      "07/02/2100", 
                                                                      "01/03/2100", 
                                                                      "07/03/2100"])
    
