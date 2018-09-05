
def isMAC48Address(inputString):
    parts = inputString.split("-")
    if len(parts) != 6:
        return False
    for p in parts:
        try:
            _ = int(p, 16)
        except ValueError:
            return False
    return True

def waterTubes(water, flowPerMinute):
    result = 0

    for i in range(len(water)):
        minutes = water[i] // flowPerMinute[i]
        if water[i] % flowPerMinute[i] != 0:
            minutes += 1

        if result < minutes:
            result = minutes
            
    return result
    
def test():
    testeql(waterTubes([1,2,5], [1,1,2]), 3)
    testeql(waterTubes([1, 1, 1], [3,4,5]), 1)
