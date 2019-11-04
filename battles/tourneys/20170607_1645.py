

def arrayConversion(inputArray):
    ct = 1
    while len(inputArray) > 1:
        tmp = []
        if ct % 2 == 1:
            for j in range(0,len(inputArray),2):
                tmp.append(inputArray[j] + inputArray[j+1])
        if ct % 2 == 0:
            for j in range(0,len(inputArray),2):
                tmp.append(inputArray[j] * inputArray[j+1])
        ct += 1
        inputArray = tmp
    return inputArray[0]


def test():
    testeql(arrayConversion([1, 2, 3, 4, 5, 6, 7, 8]), 186)
