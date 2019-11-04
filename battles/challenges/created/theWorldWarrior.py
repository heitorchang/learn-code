class Fighter:
    def __init__(self, name, playerNum):
        self.name = name
        self.playerNum = playerNum
        

class Game:
    # moves
    #      8
    #    7   9
    #  4   5   6
    #    1   3
    #      2
    
    def __init__(self):
        self.fieldSize = 20
        self.fieldHeight = 3
        self.field = [[0] * fieldSize for _ in range(fieldHeight)]
        self.ryu = Fighter("Ryu", 1)
        self.ken = Fighter("Ken", 2)

        
    def initField(self):
        self.field = [[0] * fieldSize for _ in range(fieldHeight)]


    def showField(self):
        print()
        for row in self.field:
            print(row)
        

    def place(self, player, row, col):
        self.field[row][col] = player.playerNum
        
        
    def fight(self):
        self.initField()
        
        self.place(self.ryu, 2, 6)
        self.place(self.ken, 2, 13)

        self.showField()


def theWorldWarrior(key1, key2):
    g = Game()
    g.fight()
    
test(
    theWorldWarrior("", ""), None,

    )
