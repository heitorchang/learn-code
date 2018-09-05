"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.
"""

def manipulateList(commands):
    LIST = []
    for command in commands:
        tokens = command.split()
        cmd = tokens[0]

        if cmd == "insert":
            LIST.insert(int(tokens[1]), int(tokens[2]))
        elif cmd == "print":
            print(LIST)
        elif cmd == "remove":
            LIST.remove(int(tokens[1]))
        elif cmd == "append":
            LIST.append(int(tokens[1]))
        elif cmd == "sort":
            LIST.sort()
        elif cmd == "pop":
            LIST.pop()
        elif cmd == "reverse":
            LIST.reverse()

if __name__ == "__main__":
    N = int(input())
    cmds = []
    for i in range(N):
        cmds.append(input())
    manipulateList(cmds)

def test():
    testeql(manipulateList(["insert 0 1", "print"]), None)
