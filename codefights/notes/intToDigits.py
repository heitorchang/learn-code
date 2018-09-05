n = 123
digitsMap = map(int, str(n))
digitsList = list(digitsMap)

def evenDigitsOnly(n):
    return all([d % 2 == 0 for d in map(int, str(n))])

