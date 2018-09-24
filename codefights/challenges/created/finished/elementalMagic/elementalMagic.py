description = """

How quickly can you defeat a group monsters with your magic? You have three spells and special glasses to see their strengths and weaknesses. They may be weak to some spells and absorb others.

The battle is turn-based and you always move first. For each battle, you will start with a variable amount of HP (hit points; if they drop to zero or less, you lose).

Your three spells are **Bolt**, **Fire**, and **Wind**. We will refer to them by their first letters, **B**, **F**, and **W**. During your turn, casting a spell will hit all monsters.

To represent the monsters, an array of comma-separated strings is given. Each monster follows this format:

`"Weaknesses,Absorbs,HP"`

`Weaknesses` and `Absorbs` are concatenations of **B**, **F**, and **W**, or the empty string for none. A spell will not be in both places at once.

A spell deals a fixed amount of damage to a monster (or healing, if it absorbs that element) shown below:

|Vulnerability to element|HP change|
|--|--|
|Weak to element| -5 |
|Neutral | -2 |
|Absorbs element| +1 |

During the monsters' turn, each remaining, living monster will inflict **1 HP of damage** to you.

##### Your task

Find the shortest sequence of spells to cast that defeats all monsters.

If you determine that the battle is unwinnable, output `R` (Run).

When there is more than one sequence of spells with the shortest length, output the lexicographically smallest one.

__Example__

* For
```
yourHP: 10
monsters: ["F,BW,20"]
```

The output should be `"FFFF"`. The monster is weak to **Fire**, and in the 4th turn you will defeat it.

* For 
```
yourHP: 5
monsters: [",,4", ",,4", ",,4"]
```
You may cast any spell twice to defeat the three monsters (each spell deals 2 HP of damage because they are weak to nothing and absorb nothing). Also, a spell hits all monsters at once.

The expected output is `"BB"` (two **Bolts**) because it's the lexicographically smallest sequence of two spells. Because you move first, the enemies will be defeated before their second wave of attacks.

* For
```
yourHP: 7
monsters: ["W,F,11", "F,W,10"]
```
The first, 11-HP monster is weak to **Wind** and absorbs **Fire**, while the opposite holds for the second monster.

The expected spell sequence (output) is `"BWWFF"`. There are other possible winning sequences such as `"FFWWW"` but `"BWWFF"` is lexicographically smaller.

| Turn | Spell | Monster A | Monster B | Your HP |
|--|--|--|--|--|
| (start) | (none)          | 11 | 10 | 7 |
| 1       | Bolt          | 9  | 8  | 7 |
| 1'      | monsters attack | 9  | 8  | 5 |
| 2       | Wind          | 4  | 9  | 5 |
| 2'      | monsters attack | 4  | 9  | 3 |
| 3       | Wind          | -1 | 10 | 3 |
| 3'      | monster attack | X  | 10 | 2 |
| 4       | Fire          | X  | 5  | 2 |
| 4'      | monster attack | X  | 5  | 1 |
| 5       | Fire          | X  | 0  | 1 |
| (win)   | (victory)    | X  | X  | 1 |

(your HP is in the last column and you may have to resize this panel to see it)

* For
```
yourHP: 3
monsters: [",BFW,3"]
```
the expected output is `"R"` because this monster absorbs all spells (resulting in their HP increasing every turn). You will never be able to win this battle, so you must run away.

* For 

```
yourHP: 7
monsters: [",,10", ",,10"]
```
You need to cast spells for 5 rounds to defeat these monsters, but on the 4th round, they would have dealt 8 HP of damage to you. You cannot win and should output `"R"`, escaping defeat.

__Input / Output__
"""

from itertools import product
from copy import deepcopy


class Monster:
    
    def __init__(self, monsterStr):
        parts = monsterStr.split(',')
        
        self.name = "Unknown"
        self.weaknesses = set(parts[0])
        self.absorbs = set(parts[1])
        self.hp = int(parts[2])

        
    def __str__(self):
        return "{} ({} HP) weak to {}, absorbs {}".format(
            self.name,
            self.hp,
            ''.join(sorted(list(self.weaknesses))).upper(),
            ''.join(sorted(list(self.absorbs))).upper())


    def __repr__(self):
        return "{};{};{};{}".format(self.name, self.weaknesses, self.absorbs, self.hp)

        
class Nabila:
    
    def __init__(self, hp):
        self.hp = int(hp)

        
    def __str__(self):
        return "Nabila's HP: " + self.hp

        
def parseMonster(s):
    # instantiates given monster string as a Monster
    return Monster(s)

    
def attack(monster, spell):
    if spell in monster.weaknesses:
        monster.hp -= 5
    elif spell in monster.absorbs:
        monster.hp += 1
    else:
        monster.hp -= 2 


def summarizeMonsters(monsters):
    out = ""
    for m in monsters:
        out += str(m) + "\n"
    return out[:-1]
        
def simulatePrint(nabila, monsters, spellSeq):
    print("\nSimulating monster leader", monsters[0], "magic sequence", spellSeq)
    round = 1
    for i, s in enumerate(spellSeq):
        
        print("Round", round, "Spell:", spellSeq[i])
        
        # your move
        for m in monsters:
            attack(m, s)

        print(summarizeMonsters(monsters), "; Nabila's HP:", nabila.hp)
           
        # check if any was defeated
        for i in range(len(monsters)-1, -1, -1):
            if monsters[i].hp <= 0:
                del monsters[i]

        # check for victory
        if len(monsters) == 0:
            # print("Monsters perished")
            return spellSeq
            
        # enemies attack
        nabila.hp -= len(monsters)

        # check for defeat
        if nabila.hp <= 0:
            return "D"

        round += 1
    return "C"  # continue

def simulate(nabila, monsters, spellSeq):
    round = 1
    for i, s in enumerate(spellSeq):
        
        # your move
        for m in monsters:
            attack(m, s)

        # check if any was defeated
        for i in range(len(monsters)-1, -1, -1):
            if monsters[i].hp <= 0:
                del monsters[i]

        # check for victory
        if len(monsters) == 0:
            # print("Monsters perished")
            return spellSeq
            
        # enemies attack
        nabila.hp -= len(monsters)

        # check for defeat
        if nabila.hp <= 0:
            return "D"

        round += 1
    return "C"  # continue

    
def elementalMagic(yourHP, monsterList):
    nabila = Nabila(yourHP)
    spells = "BFW"
    monsters = []
    for monsterStr in monsterList:
        monsters.append(parseMonster(monsterStr))

    # battle can only last until you run out of HP
    # assume only one enemy is standing after your first move
    turnLimit = nabila.hp

    for rounds in range(1, turnLimit+1):
        combos = product(spells, repeat=rounds)
        spellSeqs = [''.join(c) for c in combos]
        for seq in spellSeqs:
            nCopy = deepcopy(nabila)
            mCopy = deepcopy(monsters)
            outcome = simulate(nCopy, mCopy, seq)
            if outcome == "D":
                # print("Nabila is defeated with", seq)
                pass
            elif outcome == "C":
                pass
            else:
                # print("monsters perished")
                return outcome
    return "R"  # could not reach a winning sequence


print(elementalMagic(10, ["F,BW,20"]))

print(elementalMagic(5, [",,4", ",,4", ",,4"]))

print(elementalMagic(7, ["W,F,11", "F,W,10"]))

print(elementalMagic(3, [',BFW,3']))

print(elementalMagic(7, [',,10', ',,10']))

print(simulatePrint(Nabila(7), [parseMonster(m) for m in ["W,F,11", "F,W,10"]], "FFWWW"))
