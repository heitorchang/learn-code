def reduceString(inputString):
    if len(inputString) < 2:
        return inputString
    if inputString[0] == inputString[-1]:
        return reduceString(inputString[1:-1])
    else:
        return inputString

def test():
    testeql(reduceString("abacaba"), "")
