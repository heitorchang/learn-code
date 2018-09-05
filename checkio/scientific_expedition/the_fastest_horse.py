def fastest_horse(horses):
    wins = [0] * len(horses[0])
    for race in horses:
        wins[race.index(min(race))] += 1
    return 1 + wins.index(max(wins))

def test():
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
