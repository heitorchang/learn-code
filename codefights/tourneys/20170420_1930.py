def adjacentElementsProduct(inputArray):
    prods = [a * b for (a, b) in zip(inputArray, inputArray[1:])]
    return max(prods)

def doSomething(x):
    return x + 1

def test():
    testeql(doSomething(2), 3)
