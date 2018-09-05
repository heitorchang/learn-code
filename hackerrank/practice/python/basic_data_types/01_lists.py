def parse(line, lst):
    parts = line.split()
    command = parts[0]
    arguments = map(int, parts[1:])

    if command == "insert":
        lst.insert(*arguments)
    elif command == "print":
        print(lst)
    elif command == "remove":
        lst.remove(*arguments)
    elif command == "append":
        lst.append(*arguments)
    elif command == "sort":
        lst.sort()
    elif command == "pop":
        lst.pop()
    elif command == "reverse":
        lst.reverse()
        
def solution(n):
    lst = []
    for i in range(n):
        parse(input(), lst)

if __name__ == "__main__":
    n = int(input())
    solution(n)
