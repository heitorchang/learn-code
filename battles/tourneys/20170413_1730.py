def adjacentElementsProduct(inputArray):
    t = [a*b for (a,b) in zip(inputArray, inputArray[1:])]
    return max(t)
 
def test:
    testeql(adjacentElementsProduct([3, 6, -2, -5, 7, 3]), 21)
        
