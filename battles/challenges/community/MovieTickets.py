from decimal import Decimal

def MovieTicketsICanBuy(ticketPrice, comboPrice, myMoney):
    t = Decimal(ticketPrice)
    c = Decimal(comboPrice)
    m = Decimal(myMoney)
    tot = 0
    cpr = 2 * t + c
    print(type(t), type(cpr))

    combos = m // cpr
    print("combos", combos)

    tot += 2 * combos
    m -= combos * cpr
    
    if m >= t:
        tot += 1
    return tot


    """
test(MovieTicketsICanBuy(8.5, 12.5, 100), 7,
"""

test(MovieTicketsICanBuy(5, 10, 50), 5)


"""
     MovieTicketsICanBuy(1, 0, 1), 1,
     MovieTicketsICanBuy(2, 0, 2), 1,
     MovieTicketsICanBuy(1, 1, 3), 2,
     MovieTicketsICanBuy(1,1,0), 0,
     )
"""
