# DOES NOT PASS A HIDDEN TEST (5/6)

def move(startx, starty, dir, dist):
    if dir == 0:
        # up
        return (startx, starty + dist)
    elif dir == 1:
        # right
        return (startx + dist, starty)
    elif dir == 2:
        return (startx, starty - dist)
    else:
        return (startx - dist, starty)
    
def points(sx, sy, ex, ey):
    ans = set()
    if sx == ex:
        if sy < ey:
            for yy in range(sy+1, ey+1):
                ans.add((sx, yy))
        else:
            for yy in range(sy-1, ey-1, -1):
                ans.add((sx, yy))
    else:
        if sx < ex:
            for xx in range(sx+1, ex+1):
                ans.add((xx, sy))
        else:
            for xx in range(sx-1, ex-1, -1):
                ans.add((xx, sy))
    print("pointsans", ans)
    return ans

def robotWalk(a):
    visited = set()
    startx = 0
    starty = 0
    visited.add((0,0))
    dir = 0
    for d in a:
        print(dir, d)
        oldx, oldy = startx, starty
        startx, starty = move(startx, starty, dir, d)
        dir += 1
        dir %= 4
        
        newpos = (startx, starty)
        print(oldx, oldy, startx, starty)
        newpts = points(oldx, oldy, startx, starty)
        for p in newpts:
            print(p)
            if p in visited:
                return True
        visited |= newpts
        print("vis", visited)
        visited.add(newpos)
    return False

def test():
    testeql(robotWalk([4,3,2]), False)
    testeql(robotWalk([4,4,3,2,2,3]), True)
    testeql(robotWalk([5,5,5,5]), True)
