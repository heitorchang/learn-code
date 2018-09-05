def checkio(data):
    isLongEnough = len(data) >= 10
    hasUpper = any(c.isupper() for c in data)
    hasLower = any(c.islower() for c in data)
    hasDigit = any(c.isdigit() for c in data)
    
    return isLongEnough and hasUpper and hasLower and hasDigit

def test():
    testeql(checkio('A1213pokl'), False)  # too short
    testeql(checkio('bAse730onE4'), True)  # Good
    testeql(checkio('asasasasasasasaas'), False)  # no upper
    testeql(checkio('QWERTYqwerty'), False)
    testeql(checkio('123456123456'), False)
    testeql(checkio('QwErTy911poqqqq'), True)
