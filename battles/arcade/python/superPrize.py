class Prizes():
    def __init__(self, purchases, n, d):
        self.purchases = [0] + purchases
        self.n = n
        self.d = d
        self.counter = 0
        
    def __iter__(self):
        while self.purchases:
            if self.counter > 0 and self.counter % self.n == 0 and self.purchases[0] % self.d == 0:
                yield self.counter
            self.purchases = self.purchases[1:]
            self.counter += 1

def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

def test():
    testeql(superPrize([12, 43, 13, 465, 1, 13], 2, 3), [4])
