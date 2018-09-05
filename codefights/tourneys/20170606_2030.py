

def howManySundays(n, startDay):

    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    startIndex = -1

    for i in range(len(week)):
        if week[i] == startDay:
            startIndex = i

    return (n + startIndex) // len(week)

def test():
    testeql(howManySundays(9, "Saturday"), 2)
