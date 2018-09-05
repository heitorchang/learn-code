"""
You have a record of n students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer n followed by the names and marks for n students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format

The first line contains the integer n, the number of students. The next n lines contains the name and marks obtained by that student separated by a  space. The final line contains the name of a particular student previously listed.

Constraints

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

"""

def average(scores):
    return round(sum(scores) / len(scores), 2)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("{:.2f}".format(average(student_marks[query_name])))
