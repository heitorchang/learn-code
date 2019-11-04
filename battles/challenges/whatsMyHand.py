# something is not passing, if I add length.table != 10 returning full house, still missing one test

from operator import attrgetter
from collections import Counter
from itertools import combinations


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
                return True

            # check wraparound
            if (sortedranks == [12, 0, 1, 2, 3] or
                sortedranks == [11, 12, 0, 1, 2] or
                sortedranks == [10, 11, 12, 0, 1]):
                return True
        
        return False

    def hasRoyalStraight(self):
        return self.hasStraight() and self.cards[-1].rank == 12
        
        
    def countRanks(self):
        ctr = Counter([c.rank for c in self.cards])
        return ctr
        
        
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
        elif len(rankctr.keys()) == 3 and 2 in rankctrval and 1 in rankctrval:
            return 2 # "2 pairs"

        # check 1-pair
        elif len(rankctr.keys()) == 4 and 2 in rankctrval:
            return 1 # "1 pair"
            
        else:
            return 0 # "high card"


def WhatsMyHand(holeCards, table):
    allcards = Table(holeCards, table)
    maxhand = 0
    for comb in combinations(allcards.cards, 5):
        hand = Hand(comb)
        maxhand = max(maxhand, hand.what())
    if maxhand == 0:
        return "high card"
    elif maxhand == 1:
        return "1 pair"
    elif maxhand == 2:
        return "2 pairs"
    elif maxhand == 3:
        return "3 of a kind"
    elif maxhand == 4:
        return "straight"
    elif maxhand == 5:
        return "flush"
    elif maxhand == 6:
        return "full house"
    elif maxhand == 7:
        return "4 of a kind"
    elif maxhand == 8:
        return "straight flush"
    else:
        return "royal flush"
    
    
            
def testCardRank(twochar):
    c = Card(twochar)
    return c.rank

def testCardSuit(twochar):
    c = Card(twochar)
    return c.suit
        


pairtest(WhatsMyHand("5H5D", "JDTHTC4S3D"), "2 pairs",
         WhatsMyHand("3S4S", "THJHQHKHAS"), "straight")
