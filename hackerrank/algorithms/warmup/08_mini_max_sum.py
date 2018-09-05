def minmax(arr):
    minSum = float('inf')
    maxSum = float('-inf')
    arrSum = sum(arr)
    
    for n in arr:
        partSum = arrSum - n
        if partSum < minSum:
            minSum = partSum
        if partSum > maxSum:
            maxSum = partSum
    return "%d %d" % (minSum, maxSum)

def main():
    line = input()
    arr = list(map(int, line.split()))
    out = minmax(arr)
    print(out)

def test():
    testeql(minmax([1,2,3,4,5]), "10 14")
               
