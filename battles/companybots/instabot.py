def delivery(order, shoppers):
    dist_to_store = order[0]
    customer_ready = order[1]
    customer_late = order[2]

    result = []
    for s in shoppers:
        speed = s[1]
        dist = s[0]
        est_time_in_store = s[2]

        time_in_store = (dist+dist_to_store) / speed + est_time_in_store
        if time_in_store >= customer_ready and time_in_store <= customer_ready+customer_late:
            result.append(True)
        else:
            result.append(False)
    return result                          

def parseNote(paid, note):
    words = note.split()
    if words[0] == "Same":
        return paid
    percentage = words[0]
    n = float(percentage[:-1]) / 100
    isHigher = 1 if words[1] == 'higher' else -1
    return paid / (1 + isHigher * n)

def isAdmissibleOverpayment(prices, notes, x):
    paid = sum(prices)
    real = [parseNote(p, n) for (p, n) in zip(prices, notes)]
    total_real = sum(real)
    pr('real')
    print(paid - total_real - x)
    return (paid - total_real - x) < 0.0001

def parseTime(t):
    parts = t.split(":")
    hours = int(parts[0])
    mins = int(parts[1])
    return hours * 60 + mins

def shopperCanDoIt(shopper, order, leadTime):
    order_start = parseTime(order[0])
    order_end = parseTime(order[1])
    shopper_start = parseTime(shopper[0])
    shopper_end = parseTime(shopper[1])

    if order_start + leadTime <= shopper_end and max(shopper_start, order_start) + leadTime <= order_end:
        return True
    return False

class Shopper:
    def __init__(self, start, finish):
        self.start = parseTime(start)
        self.finish = parseTime(finish)
        self.busy = False

    def canDoIt(self, orders):
        result = []
        for o in orders:
            if o.fulfilled:
                result.append(False)
            else:
                result.append(o.start + o.leadTime <= self.finish and max(self.start, o.start) + o.leadTime <= o.finish)
        return result

    def __repr__(self):
        return "Shopper " + str(self.start) + " to " + str(self.finish) + " " + str(self.busy)
        
class Order:
    def __init__(self, start, finish, leadTime):
        self.start = parseTime(start)
        self.finish = parseTime(finish)
        self.leadTime = leadTime
        self.fulfilled = False
        self.howManyShoppersCanFulfill = 0

    def canBeDone(self, shoppers):
        result = []
        for s in shoppers:
            if s.busy:
                result.append(False)
            else:
                result.append(self.start + self.leadTime <= s.finish and max(s.start, self.start) + self.leadTime <= self.finish)
        self.howManyShoppersCanFulfill = result.count(True)
        return result

    def __repr__(self):
        return "Order " + str(self.start) + " to " + str(self.finish) + " " + str(self.fulfilled)

def busyHolidays(shoppers, orders, leadTime):
    myShoppers = []
    myOrders = []
    for s in shoppers:
        myShoppers.append(Shopper(s[0], s[1]))
    for i in range(len(orders)):
        myOrders.append(Order(orders[i][0], orders[i][1], leadTime[i]))

    for o in myOrders:
        print(o.canBeDone(myShoppers))
        print(o.howManyShoppersCanFulfill)
        if o.howManyShoppersCanFulfill == 0:
            return False

    myOrders = sorted(myOrders, key=lambda o: o.howManyShoppersCanFulfill)
    pr('myOrders')

def test():
    #testeql(delivery([200, 20, 15], [[300,40,5], [600,40,10]]), [False, True])
    #testeql(parseNote(165, "10.0% higher than in-store"), 150)
    testeql(isAdmissibleOverpayment([24.42, 24.42, 24.2424, 85.23], ["13.157% higher than in-store", 
 "13.157% lower than in-store", 
 "Same as in-store", 
 "19.24% higher than in-store"], 24.24), True)
    testeql(isAdmissibleOverpayment([110, 95, 70], ["10.0% higher than in-store", 
 "5.0% lower than in-store", 
 "Same as in-store"], 5), True)
    testeql(isAdmissibleOverpayment([220], ["120.0000% higher than in-store"], 120), True)
    testeql(parseTime("15:10"), 910)
    testeql(busyHolidays([["23:00","23:59"], ["22:30","23:30"]], [["23:15","23:35"], ["23:00","23:31"]], [20, 31]), False)
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
