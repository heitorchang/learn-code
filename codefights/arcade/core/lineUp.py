def lineUp(commands):
    """Idea: first student mixes up L/R
    0 = facing front
    1 = facing right
    2 = facing back
    3 = facing left
    """
    students = [0, 0]
    tot = 0
    for i, c in enumerate(commands, 1):
        if c == "L":
            students[0] = (students[0] - 1) % 4
            students[1] = (students[1] + 1) % 4
        elif c == "R":
            students[0] = (students[0] - 1) % 4
            students[1] = (students[1] + 1) % 4
        else:
            for j in range(2):
                students[j] = (students[j] + 2) % 4
                
        if len(set(students)) == 1:
            tot += 1
    return tot
    
test(lineUp("RLR"), 1,
     lineUp("LLARL"), 3,
     lineUp(""), 0)
