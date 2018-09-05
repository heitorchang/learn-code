from operator import attrgetter
from collections import namedtuple

Student = namedtuple("Student", "name score")

test_case = [Student("Harry", 37.21),
             Student("Berry", 37.21),
             Student("Tina", 37.2),
             Student("Ken", 37.2),
             Student("Akriti", 41),
             Student("Harsh", 39)]

def parse(n):
    students = []
    for i in range(n):
        name = input()
        score = float(input())
        students.append(Student(name, score))
    return students

def solution(students):
    students.sort(key=attrgetter('score', 'name'))
    lowest_score = students[0].score
    
    # discard all lowest scores
    while students[0].score == lowest_score:
        students.pop(0)

    second_lowest_score = students[0].score

    # print all second_lowest_score names
    while students[0].score == second_lowest_score:
        print(students[0].name)
        students.pop(0)
    
if __name__ == "__main__":
    n = int(input())
    arr = parse(n)
    solution(arr)

