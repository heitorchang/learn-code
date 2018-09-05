def compute_average(student):
    parts = student.split()
    name = parts[0]
    average = sum(map(float, parts[1:])) / (len(parts) - 1)
    return {name: "{:.2f}".format(average)}

def solution(n):
    students = {}
    for i in range(n):
        students.update(compute_average(input()))
    selected = input()
    print(students[selected])
    
if __name__ == "__main__":
    n = int(input())
    solution(n)
