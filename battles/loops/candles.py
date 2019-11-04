def candles(candlesNumber, makeNew):
    burned = 0
    leftovers = 0   
    while candlesNumber > 0:
        burned += candlesNumber
        leftovers += candlesNumber
        candlesNumber, leftovers = divmod(leftovers, makeNew)
    return burned

test(candles(5, 2), 9,
     candles(1, 2), 1,
     candles(3, 3), 4)
