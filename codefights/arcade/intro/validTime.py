def validTime(time):
    hh = int(time[:2])
    mm = int(time[-2:])
    return 0 <= hh <= 23 and 0 <= mm <= 59
