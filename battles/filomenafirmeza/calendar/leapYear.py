def leapYear(year):
    """Go from most specific to least"""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def test():
    testeql(leapYear(2000), True)
    testeql(leapYear(2001), False)
    testeql(leapYear(1000), False)
    testeql(leapYear(100), False)
    testeql(leapYear(124), True)
