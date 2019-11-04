description_draft = """
It's field trip day for Ms. Venmore's Art class! Upon reaching the art festival, her students will be assigned to various booths such as Gooey Pottery, Patchy Pastels and I-Can't-Believe-it's-Not-Popsicle-Sticks.

Before getting on the bus, Ms. Venmore asked all her students to rate each of the available activities from `1` (Hate it!) to `10` (Love it!).

She asked you, the school's algorithms whiz, to help her maximize fun-ness for everyone. 

You will help her divide the students into the most suitable activities so that as a whole, her students get the most enjoyment.

She stipulated that **every booth should have at least two students** so that everyone works with a buddy and can later share their experience with their classmates.

Because you're not so good with names, **you will report to the principal only a tally of how many students went to each booth.**

In case there is a tie between multiple booths, **you should favor the activities toward the left of the ratings' lists.**

TODO
Generate test cases

Brute force assign each student to a booth
```
students >= len(prefs[0]) * 2
prefs = [
[10, 2, 3],
[3, 2, 1],
[9, 4, 10],
[3,3,3],
[1,2,2],
[4,4,5],
]

activities = len(prefs[0])
maxEnjoyment = 0
for assignments in product(range(activities)):
 # somehow calc sum from assign to prefs matrix
```

__Input/Output__
"""

from itertools import product
from collections import Counter
import random


def checkAtLeastTwo(activitiesCount, counter):
    if len(counter) != activitiesCount:
        # exclude if there's an empty booth
        return False

    for activity in counter:
        if counter[activity] < 2:
            # activity must have at least two students
            return False

    return True


def activityBuddies(ratings):
    print(ratings)
    
    studentsCount = len(ratings)
    activitiesCount = len(ratings[0])

    assignments = product(range(activitiesCount), repeat=studentsCount)

    maxFun = 0
    maxAssignment = None
    maxCounter = None
    
    for assignment in assignments:
        # count totals for each booth
        boothTallies = Counter(assignment)

        if checkAtLeastTwo(activitiesCount, boothTallies):

            # add up total student enjoyment
            assignmentFun = 0
            for i, activityIndex in enumerate(assignment):
                # match student's interest to current assignment
                assignmentFun += ratings[i][activityIndex]

            print(assignment, assignmentFun)
            if assignmentFun > maxFun:  # update max
                maxFun = assignmentFun
                maxAssignment = assignment
                maxCounter = boothTallies

    print("Max Fun", maxFun)

    # Convert max counter to array
    tallyArray = []
    for key in sorted(maxCounter):
        tallyArray.append(maxCounter[key])

    print("Max assignment", maxAssignment)
    
    return tallyArray


def generateRatingsTestCases(activitiesCount, studentsCount):
    if studentsCount < 2 * activitiesCount:
        raise ValueError("Number of students must be at least twice the number of activities")

    ratings = []

    for i in range(studentsCount):
        student = []
        for j in range(activitiesCount):
            student.append(random.randint(1, 10))
        ratings.append(student)

    return ratings
    
    

    """
test(activityBuddies([
    [1,1,1],
    [3,3,3],
    [2,3,2],
    [2,3,4],
    [5,5,3],
    [9,9,3]]), [2,2,2],
"""

test(
    activityBuddies([
         [10, 4],
         [10, 9],
         [9, 10],
         [8, 9],
         [3, 3],
         ]), [3, 2],

    activityBuddies([
        [9, 3],
[8, 2],
[10, 1],
[7, 5],
[8, 2]]), [3, 2])
