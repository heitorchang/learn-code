from functools import reduce

def mathPracticeLong(numbers):
    s = numbers[0]
    for i in range(1, len(numbers)):
        if i % 2 == 1:
            s += numbers[i]
        else:
            s *= numbers[i]
    return s

def mathPracticePy2(numbers):
    # works only in Python 2
    return reduce(lambda x,(i,y): x + y if i % 2 == 1 else x * y, numbers, 1)

def mathPractice(numbers):
    # Python 3 wynn_v solution
    return reduce(lambda acc, x: (acc+x[1] if x[0]%2 else acc*x[1]), enumerate(numbers), 1)

def test():
    testeql(mathPractice([1,2,3,4,5,6]), 71)
    testeql( ( (1 * 1 + 2) * 3 + 4) * 5 + 6 , 71)
