from collections import defaultdict

# Brute force, score: 5.97

def countOccurrences(start, end, locations):
    # start, end inclusive
    total = 0
    for location in locations:
        if start <= location <= end:
            total += 1

    return total

def query(arr, len_arr, x, y, occur):
    total = 0
    if x not in occur:
        for i, elem in enumerate(arr):
            if elem == x:
                occur[x].append(i)

    if y not in occur:
        for i, elem in enumerate(arr):
            if elem == y:
                occur[y].append(i)
        
    for start in range(len_arr):
        for end in range(start, len_arr):
            xCt = countOccurrences(start, end, occur[x])
            yCt = countOccurrences(start, end, occur[y])
            if xCt == yCt:
                total += 1
    return total
    
    
def main():
    arr = [1, 2, 1]
    len_arr = len(arr)
    occurrences = defaultdict(list)
    total = 0
    print(query(arr, len_arr, 1, 2, occurrences))
    print(query(arr, len_arr, 4, 5, occurrences))

    
def test():
    testeql(countOccurrences(0, 10, [2,3]), 2)
    testeql(countOccurrences(0,3,[0,3]), 2)
    testeql(main(), None)
