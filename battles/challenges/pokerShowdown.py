from operator import attrgetter
from collections import Counter
from itertools import combinations, product


class Card:
    def __init__(self, twochar):
        ranks = ['A', '2', '3', '4' ,'5' ,'6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        self.twochar = twochar
        self.rank = ranks.index(twochar[0])
        self.suit = twochar[1]

    def __str__(self):
        return str(self.rank) + self.suit
        
    def __repr__(self):
        return "Card({})".format(self.twochar)
        

class Table:
    """7 cards"""
    def __init__(self, holeCards, t):
        chars = holeCards + t
        self.cards = [Card(chars[i*2:(i+1)*2]) for i in range(7)]
    
class Hand:
    """5 cards"""
    # def __init__(self, tenchar):
    #     self.cards = [Card(tenchar[i*2:(i+1)*2]) for i in range(5)]
    #     self.cards.sort(key=attrgetter('rank'))

    def __init__(self, cards):
        self.cards = list(cards)
        self.cards.sort(key=attrgetter('rank'))
        

    def __repr__(self):
        return "[" + ", ".join(map(str, self.cards)) + "]"

    def hasFlush(self):
        ctr = Counter([c.suit for c in self.cards])
        return max(ctr.values()) == 5

    def hasStraight(self):
        handranks = {c.rank for c in self.cards}
        if len(handranks) < 5:
            return False

        sortedranks = [c.rank for c in self.cards]

        if sortedranks[-1] - sortedranks[0] == 4:
            return True
            
        if 0 in sortedranks:
            # consider T J Q K A
            if sortedranks == [0, 9, 10, 11, 12]:
                # self.cards = 
                return True

            # check wraparound
            # if (sortedranks == [0, 1, 2, 3, 12] or
            #     sortedranks == [0, 1, 2, 11, 12] or
            #     sortedranks == [0, 1, 10, 11, 12]):
            #     return True
        
        return False

    def hasRoyalStraight(self):
        sortedranks = [c.rank for c in self.cards]
        return self.hasStraight() and sortedranks == [0, 9, 10, 11, 12]
        
        
    def countRanks(self):
        ctr = Counter([c.rank for c in self.cards])
        return ctr
        
    def rankstring(self):
        revsortranks = [c.rank for c in self.cards]
        revsortranks.sort(reverse=True)
        return ''.join("%02d" % c for c in revsortranks)
        
        
    def what(self):
        # check royal flush
        if self.hasRoyalStraight() and self.hasFlush():
            return 9 # "royal flush"
            
        # check straight flush
        elif self.hasStraight() and self.hasFlush():
            return 8 # "straight flush"

        rankctr = self.countRanks()
        rankctrval = rankctr.values()
        
        # check 4-kind
        if 4 in rankctrval:
            return 7 # "4 of a kind"

        # check full house
        elif 3 in rankctrval and 2 in rankctrval:
            return 6 #"full house"

        # check flush
        elif self.hasFlush():
            return 5 # "flush"
        
        # check straight
        elif self.hasStraight():
            return 4 # "straight"

        # check 3-kind
        elif 3 in rankctrval:
            return 3 # "3 of a kind"

        # check 2-pair
        elif len(rankctr.keys()) == 3 and 2 in rankctrval:
            return 2 # "2 pairs"

        # check 1-pair
        elif len(rankctr.keys()) == 4 and 2 in rankctrval:
            return 1 # "1 pair"
            
        else:
            return 0 # "high card"

    def whatStr(self):
        whatint = self.what()
        rstr = self.rankstring()
        return int(str(whatint) + rstr)
        

def WhatsMyHand(holeCards, table):
    allcards = Table(holeCards, table)
    maxhand = 0
    for comb in combinations(allcards.cards, 5):
        hand = Hand(comb)
        # print(hand.rankstring())
        maxhand = max(maxhand, hand.whatStr())
    return maxhand
    
def PokerShowdown(table, players):
    vals = [WhatsMyHand(p, table) for p in players]
    print(vals)
    maxval = max(vals)
    return [i for i, e in enumerate(vals) if e == maxval]


pairtest(PokerShowdown("KHKD5D5S4S", ["4DQH", "4CAH", "6H6C"]), [2])
