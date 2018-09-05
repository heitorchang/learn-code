description = """
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
"""

def centuryFromYear(year):
    # realize that the edge case is a multiple of 100
    # normally it is year//100 + 1, so we subtract 1 from year
    # then compute the quotient
    
    return ((year - 1) // 100) + 1

def test():
    testeql(centuryFromYear(1700), 17)
    testeql(centuryFromYear(1905), 20)
    testeql(centuryFromYear(2000), 20)
    testeql(centuryFromYear(1), 1)
    
