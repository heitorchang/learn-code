from itertools import combinations

def crazyball(players, k):
    return sorted([sorted(row) for row in list(combinations(players, k))])
