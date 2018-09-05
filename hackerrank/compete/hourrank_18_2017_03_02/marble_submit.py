#!/bin/python3

import sys


m,n = input().strip().split(' ')
m,n = [int(m),int(n)]

cups = [0 for i in range(11)]
cups[m] = 1

for a0 in range(n):
    a,b = input().strip().split(' ')
    a,b = [int(a),int(b)]
    # your code goes here
    cups[a], cups[b] = cups[b], cups[a]
    
print(cups.index(1))
