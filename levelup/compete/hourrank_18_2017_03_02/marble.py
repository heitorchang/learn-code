import sys


#m,n = input().strip().split(' ')
#m,n = [int(m),int(n)]
m, n = [5, 3]

swaps = [[2, 5],
         [7, 10],
         [2, 9]]

cups = [0 for i in range(11)]
cups[m] = 1

#for a0 in range(n):
    # a,b = input().strip().split(' ')
#    a,b = [int(a),int(b)]
    # your code goes here

for s in swaps:
    cups[s[0]], cups[s[1]] = cups[s[1]], cups[s[0]]


