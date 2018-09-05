def sumUpNumbers(inputString):
    p = re.compile('[^\d]+')
    nums = p.split(inputString)
    nums = filter(lambda s: len(s) > 0, nums)
    nums = map(int, nums)
    return sum(nums)

def test():
    testeql(sumUpNumbers("2 apples, 12 oranges"), 14)
