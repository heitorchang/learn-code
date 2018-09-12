description = """

You are *Nabila*, a brave aspiring sorceress in the land of *Qod Segnall*. Between you and the fabled *Qantum Staff* are groups of bloodthirsty monsters you must defeat with your magic.

So far you have learned three elemental spells:

| Name | Element |
|--|--|
|*Blowah*|Wind|
|*Coldah*|Ice|
|*Hottah*|Fire|

Your eagerness and high intelligence come at a cost: you have yet to master the skill to focus your energy on a specific target. All spells you cast will hit everything in front of you. Casting spells use up your willpower, which you may recover after a battle is over (in other words, you can endlessly cast spells). However, you want to save your energy for the grueling road in front of you.

You start each battle with **a variable amount of HP** (hit points) and are equipped with the magical **Jaevskrit  Armor**, which reduces all damage by a single monster to just **1 HP per attack**. If your HP drops to zero or below, you will lose the battle and your quest will end.

Monsters are attuned to certain elements, and may have a weakness to none or multiple elements. They may also absorb some elements, which increases their HP. 

With your Spectral Specs you can always tell how much HP monsters have and what their elemental affinities are. They have no upper limit to their HP. 

Every spell deals a fixed amount of damage (or healing, if the monster absorbs that element) shown below:

|Vulnerability to element|HP change|
|--|--|
|Weak to element| -5 |
|Neutral | -2 |
|Absorbs element| +1 |

A monster is defeated if its HP drops to zero or below. A defeated monster cannot revive.

In your studies, you have classified basic monster types by the following characteristics. The abbreviations refer the initial letter of your spells, (B)lowah, (C)oldah and (H)ottah.

| Type | Weak to | Absorbs |
|--|--|--|--|
| blazing | C | H |
| frigid | H | C |
| lizard | C | (none) |
| flying | B | (none) |
| spirit | (none) | B |
| vortex | (none) | BCH |
| humanoid | (none) | (none) |

For convenience, these types are available in the following JSON with `[weak to, absorbs]` format:

```
{"blazing": ["C", "H"],
"frigid": ["H", "C"],
"lizard": ["C", ""],
"flying": ["B", ""],
"spirit": ["", "B"],
"vortex": ["", "BCH"],
"humanoid": ["", ""]}
```

If a monster with multiple types has conflicting elemental attributes, its **Absorbs** characteristic overrides its weakness. For example, **Ghost** is a flying spirit. While flying enemies are normally weak to *Blowah*, spirits absorb *Blowah*, therefore, a **Ghost** will absorb *Blowah*.

As another example, dragons, being `flying lizard`s, are supposed to be weak to *Coldah* and *Blowah*.

But an **Ice dragon**, being *frigid*, will absorb *Coldah*, nullifying the *lizard*'s weakness to this spell. So the **Ice dragon** will be weak to *Blowah* and *Hottah* (because it's *frigid*), and will absorb *Coldah*.

Each *Test Case* will represent a battle you must win or run away from. Winning battles give you experience, so you will only run if the battle is unwinnable (that is, there are no possible winning sequences)

Battles are turn-based and you will always move first, starting with `nabilaHP` Hit Points. You win when all monsters' HP drop to zero or below. After your move, all living monsters will attack you (dealing 1 HP of damage per living monster), and afterward, a new round begins. There is no way to heal yourself during a battle.

Your task is to find the shortest sequence of spells to dispatch the monsters. If there is more than one optimal sequence, output the lexicographically smallest one. You must try and win, but for hopeless battles, output `"R"` (Run). 

A valid sequence of spells will be a string of characters made up of any number of `"B", "C"`, and `"H"`, (the first letter of each spell: (B)lowah, (C)oldah and  (H)ottah). Spells should simply be concatenated together without separators.

Monsters are given as an array of strings in the following semicolon-separated format:

`"Monster Name;Types (comma-separated);initial HP"`

For example:

`"Ice dragon;lizard,flying,frigid;35"`

__Example__

* For
```
monsters: ["Ice dragon;lizard,flying,frigid;35"]
nabilaHP: 15
```

The output should be `"BBBBBBB"`. Being a *flying* monster with no additional characteristic to absorb *Blowah*, it will be weak to this spell and receive `5` points of damage every turn. Because you attack first, on the 7th round the dragon will be defeated. You will have received `6` points of damage to you, winning with only `1` HP left. You will begin other battles with an unrelated amount of HP.

* For 
```
monsters: ["Goblin;humanoid;4",
"Goblin;humanoid;4",
"Goblin;humanoid;4"]
nabilaHP: 5
```
You may cast any spell twice to defeat the three goblins (each spell deals 2 HP of damage because they are weak to nothing and absorb nothing). Remember that any spell hits all monsters at once.

The expected output is `"BB"` (two Blowahs) because it's the shortest and lexicographically smallest sequence of spells. Because you move first, the enemies will be defeated before their second wave of attacks.

* For
```
monsters: ["Flame wolf;blazing;11",
"Ice leopard;frigid;10"]
nabilaHP: 7
```
The wolf is weak to *Coldah* and absorbs *Hottah*, while the opposite holds for the leopard.

The expected spell sequence (output) is `"BCCHH"`. There are other possible winning sequences such as `"HHCCC"` but `"BCCHH"` is lexicographically smaller.

| Turn | Spell | Flame W. | Ice L. | Your HP |
|--|--|--|--|--|
| (start) | (none)          | 11 | 10 | 7 |
| 1       | Blowah          | 9  | 8  | 7 |
| 1'      | monsters attack | 9  | 8  | 5 |
| 2       | Coldah          | 4  | 9  | 5 |
| 2'      | monsters attack | 4  | 9  | 3 |
| 3       | Coldah          | -1 | 10 | 3 |
| 3'      | monster attack | X  | 10 | 2 |
| 4       | Hottah          | X  | 5  | 2 |
| 4'      | monster attack | X  | 5  | 1 |
| 5       | Hottah          | X  | 0  | 1 |
| (win)   | Victory pose    | X  | X  | 1 |

(your HP is the last column and you may have to resize this panel to see it)

* For
```
monsters: ["Magic haze;vortex;3",
"Iguana;lizard;12"]
nabilaHP: 4
```
the expected output is `"R"` because vortices absorb all spells (resulting in their HP increasing every turn). You will never be able to win this battle, so you must run away.

* For 

```
monsters: ["Iron golem;humanoid;10",
"Iron golem;humanoid;10"]
nabilaHP: 7
```
You need to cast spells for 5 rounds to defeat these monsters, but on the 4th round, they would have dealt 8 HP of damage to you. You cannot win and should output `"R"`, escaping defeat.

__Input / Output__

"""


inputoutput = """
The list of monsters in this particular battle. Each string represents a monster in the format `"NAME;TYPES (comma-separated);HP"`

*Guaranteed constraints*:
<code>1 &le; monsterList.length &le; 10</code>


Nabila's HP at the start of the battle

*Guaranteed constraints*:
<code>1 &le; nabilaHP &le; 100</code>


The shortest sequence of spells you will cast that leads to victory, or `"R"` if you must run away. If multiple winning sequences of the shortest length exist, output the lexicographically smallest one.

"""

from itertools import product
from copy import deepcopy

type_defs = {
    "blazing": ["C", "H"],
    "frigid": ["H", "C"],
    "lizard": ["C", ""],
    "flying": ["B", ""],
    "spirit": ["", "B"],
    "vortex": ["", "BCH"],
    "humanoid": ["", ""],
}

class Monster:
    
    def __init__(self, name, types, hp):
        self.name = name
        self.weaknesses = set()
        self.absorbs = set()
        self.hp = int(hp)

        # build all absorbs
        for type_name in types:
            type = type_defs[type_name]
            type_absorbs = type[1]
            for a in type_absorbs:
                self.absorbs.add(a)

        # build weaknesses
        for type_name in types:
            type = type_defs[type_name]
            type_weaknesses = type[0]
                
            for w in set(type_weaknesses):
                if w not in self.absorbs:
                    self.weaknesses.add(w)

                    
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
    name, types_csv, hp = s.split(';')
    types = types_csv.split(',')
    return Monster(name, types, hp)

    
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
        
def simulate(nabila, monsters, spellSeq):
    # print("\nSimulating monster leader", monsters[0], "magic sequence", spellSeq)
    round = 1
    for s in spellSeq:
        
        # print("Round", round, "Spell:", spellSeq)
        
        # your move
        for m in monsters:
            attack(m, s)

        # print(summarizeMonsters(monsters), "; Nabila's HP:", nabila.hp)
              
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
        
def mightyMagic(monsterList, nabilaHP):
    nabila = Nabila(nabilaHP)
    spells = "BCH"
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

# print(mightyMagic(["Ice dragon;lizard,flying,frigid;25"]))

"""
print(mightyMagic([
"Goblin;humanoid;4",
"Goblin;humanoid;4",
"Goblin;humanoid;4"
]))
"""

print(mightyMagic(["Ice dragon;lizard,flying,frigid;35"], 15))

print(mightyMagic(["Goblin;humanoid;4",
                   "Goblin;humanoid;4",
                   "Goblin;humanoid;4"], 5))

print(mightyMagic(["Flame wolf;blazing;11","Ice leopard;frigid;10"], 7))

print(mightyMagic(["Magic haze;vortex;3",
                   "Iguana;lizard;12"], 4))

print(mightyMagic(["Iron golem;humanoid;10",
                   "Iron golem;humanoid;10"], 7))

print(mightyMagic(["Frost Gecko;frigid,lizard;10"], 9))  # HH
