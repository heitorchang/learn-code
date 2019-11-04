def parseTime(t):
    parts = t.split(":")
    hours = int(parts[0])
    mins = int(parts[1])
    return hours * 60 + mins

def canComplete(shopper, order, leadTime):
    order_start = parseTime(order[0])
    order_end = parseTime(order[1])
    shopper_start = parseTime(shopper[0])
    shopper_end = parseTime(shopper[1])

    if order_start + leadTime <= shopper_end and max(shopper_start, order_start) + leadTime <= order_end:
        return True
    return False

def busyHolidays(shoppers, orders, leadTime):
    # still not good enough, but beat the bot 800:753
    if len(orders) == 0:
        return True
    orderCanBeCompleted = []
    orderShoppersAvail = []
    for i in range(len(orders)):
        orderCanBeCompleted.append([])
        for s in shoppers:
            orderCanBeCompleted[i].append(canComplete(s, orders[i], leadTime[i]))
        orderShoppersAvail.append((orderCanBeCompleted[i].count(True), i))
    for osa in orderShoppersAvail:
        if osa[0] == 0:
            return False
    oss = sorted(orderShoppersAvail)
    orderToClear = oss[0][1]
    shopperToClear = orderCanBeCompleted[orderToClear].index(True)

    del shoppers[shopperToClear]
    del orders[orderToClear]
    del leadTime[orderToClear]
    return busyHolidays(shoppers, orders, leadTime)

def test():
    # testeql(canComplete(["15:10", "16:00"], ["15:00", "15:45"], 15), True)
    # testeql(canComplete(["15:10", "16:00"], ["15:00", "15:45"], 36), False)
    testeql(busyHolidays(
        [["23:00","23:20"], 
         ["23:10","23:30"], 
         ["23:15","23:35"]],

        [["23:05","23:30"], 
         ["23:05","23:30"], 
         ["23:05","23:30"]],
        [15, 15, 15]), True)

    testeql(busyHolidays(
        [["01:00","02:00"], 
         ["01:01","01:30"]],
        
        [["01:00","02:00"], 
         ["01:11","02:00"]],
        
        [20, 20]), True)

    testeql(busyHolidays(
[["15:10","16:00"], 
 ["17:50","22:30"], 
 ["13:00","14:40"]],
[["14:30","15:00"]], [15]), False)
