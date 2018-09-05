def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        return upperBound

    return found

def test():
    testeql(mexFunction([0,4,2,3,1,7], 10), 5)
