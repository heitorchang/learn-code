from itertools import combinations

# math.isclose, available in 3.5
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def countVisibleTowerPairs(position, height):
    towers = sorted([(x, y) for (x, y) in zip(position, height)])
    total = 0
    for pair in combinations(range(len(towers)), 2):
        if pair[1] - pair[0] == 1:
            # adjacent pairs see each other
            total += 1
        else:
            # check towers in between
            leftTower = towers[pair[0]]
            rightTower = towers[pair[1]]
            
            rise = rightTower[1] - leftTower[1]
            run = rightTower[0] - leftTower[0]
            slope = rise / run

            pr('pair rise run')
            towerHits = False
            for towerIndex in range(pair[0] + 1, pair[1]):
                towerInBetween = towers[towerIndex]
                dy = slope * (towerInBetween[0] - leftTower[0]) + leftTower[1]
                diff = dy - towerInBetween[1]
                pr('towerInBetween diff')
                if diff < 0:
                    print("TRUE")
                    towerHits = True
                    break
            if not towerHits:
                total += 1
                pr('towerInBetween dy')
    return total

def test():
    testeql(countVisibleTowerPairs([3,0,6,10], [2,1,4,6]), 5)
