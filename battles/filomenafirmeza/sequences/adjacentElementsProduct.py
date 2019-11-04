description = """
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.
"""

def adjacentElementsProduct(inputArray):
    maxprod = float('-inf')
    for i in range(len(inputArray)-1):
        maxprod = max(maxprod, inputArray[i] * inputArray[i+1])
    return maxprod
