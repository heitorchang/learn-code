

def isIPv4Address(inputString):
    parts = inputString.split(".")
    if len(parts) != 4:
        return False
    for p in parts:
        if len(p) < 1:
            return False
        try:
            ip = int(p)
        except:
            return False
        if not (0 <= ip <= 255):
            return False
    return True

def test():
    testeql(
