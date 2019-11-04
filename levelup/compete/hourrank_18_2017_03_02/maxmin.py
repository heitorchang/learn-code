n,q = [4, 3]
# a = list(map(int, input().strip().split(' ')))
a = [1, 2, 1, 4]

#for a0 in range(q):
#    low = int(input().strip())
#    high = int(input().strip())
    # your code goes here

    #split

queries = [[1, 1],
           [2, 2],
           [2, 3]]

def max_be(b, e):
    return max(a[b:e+1])

def min_be(b, e):
    return min(a[b:e+1])

def diff_be(b, e):
    return max_be(b, e) - min_be(b, e)

# build table
diffs = []
len_a = len(a)
for b in range(len(a)):
    for e in range(b, len(a)):
        diffs.append(diff_be(b, e))
    
for q in queries:
    low = q[0]
    high = q[1]
    print(list(map(lambda n: low <= n <= high, diffs)).count(True))
