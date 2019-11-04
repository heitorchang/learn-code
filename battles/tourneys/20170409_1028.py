def maxZeros(n):
    pass

def pagesNumbering(n):

    tenPower = 1
    digitsPerPage = 1
    result = 0

    while tenPower * 10 <= n:
        result += tenPower * 9
        tenPower *= 10
        digitsPerPage += 1
    pr('result tenPower digitsPerPage')
    print(2897 - result)
    result += (tenPower) * digitsPerPage

    return result


    
    
def test():
    testeql(
