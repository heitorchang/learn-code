def studentsAge(students):
    diff = 0
    tmp = {students[0]:1}
    for i in range(1,len(students)):
        if students[i]-1 in tmp:
            diff +=  tmp[students[i]-1]    
        if students[i] not in tmp:
            tmp[students[i]] = 1
        else:
            tmp[students[i]] += 1
        print(tmp)
    return diff

def test():
    testequal(studentsAge([2, 4, 3, 4, 6]), 2)
