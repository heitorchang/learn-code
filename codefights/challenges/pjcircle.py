from collections import deque as d

def pjCircle(s,w):
    q = d(range(1, s+1))
    a = []
    while q:
        q.rotate(-2)
        a.append(q.pop())
    return a[-w:]
