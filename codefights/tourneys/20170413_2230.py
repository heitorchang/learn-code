def romanize(n):
    u = n % 10
    t = n // 10
    c = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    return 'X' * t + c[u]

def deromanize(s):
    c = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
         'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX',
         'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI']
    try:
        return c.index(s)
    except ValueError:
        return -1
    
def dateEncryption(date):
    r = romanize(date)
    rr = r[::-1]
    return deromanize(rr)
    

def factorialTrailingZeros(n):
    result = 0
    for i in range(5, n + 1, 5):
        number = i
        while number % 2 == 0:
            number /= 5
            result += 1
    return result

def test():
    testeql(dateEncryption(7), -1)
    testeql(romanize(8), 'VIII')
    testeql(romanize(25), "XXV")
    testeql(deromanize('XXXX'), -1)
    testeql(factorialTrailingZeros(29), 6)
