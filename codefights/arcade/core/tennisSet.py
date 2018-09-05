def tennisSet(score1, score2):
    if score1 > 7 or score2 > 7:
        return False
    if score1 == 7 and score2 == 7:
        return False
    if score1 == 7 and score2 >= 5:
        return True
    if score2 == 7 and score1 >= 5:
        return True
    if score1 == 6 and score2 < 5:
        return True
    if score2 == 6 and score1 < 5:
        return True
    return False
    
