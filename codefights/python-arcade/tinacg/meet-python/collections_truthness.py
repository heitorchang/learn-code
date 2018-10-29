# What will res be?

xs = [()]
res = [False] * 2
if xs:
    res[0] = True
if xs[0]:
    res[1] = True

# my initial answer: [True, False] => OK
