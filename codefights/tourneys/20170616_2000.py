

def depositProfit(deposit, rate, threshold):
    cur = deposit
    factor = 1 + (rate / 100)
    yr = 0
    while cur < threshold:
        cur *= factor
        yr += 1
    return yr



def test():
    testeql(depositProfit(100, 20, 170), 3)
