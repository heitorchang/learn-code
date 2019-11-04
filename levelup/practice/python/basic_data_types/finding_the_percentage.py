# if __name__ == '__main__':
if False:
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

def my_average(scores):
    print("{:.2f}".format(sum(scores) / len(scores)))
    
def solve(name):
    return my_average(student_marks[name])
