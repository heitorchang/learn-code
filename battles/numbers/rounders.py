def myround(x):
    # builtin round returns even numbers
    n = x % 10
    if n >= 5:
        return 10 - n
    else:
        return -n
        
def rounders(value):
    steps = len(str(value))
    for i in range(1, steps):
        value += myround(value)
        value //= 10
    return value * 10 ** (steps - 1)

test(rounders(1445), 2000)
