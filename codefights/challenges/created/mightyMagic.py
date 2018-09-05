description = """
You are *Nabila*, a brave, aspiring sorceress in the land of *Qod Segnall*. Between you and the fabled *Qantum Staff* are hordes of bloodthirsty monsters.

So far you have learned three elemental spells:

| Enchantment | Element |
|--|--|
|*Blowah*|Wind|
|*Coldah*|Ice|
|*Hottah*|Fire|

Your eagerness and high intelligence come at a cost: you have yet to master the skill to focus your energy on a specific target. All spells you cast will hit everything in front of you. Casting spells use up your willpower, which you may recover after a battle is over (in other words, you can endlessly cast spells). However, you want to save your energy for the grueling road in front of you.

**You have 15 HP** (hit points) and are equipped with the magical **Jaavskrit  Armor**, which reduces all monster damage to just **1 HP per attack**. By standing still for just a minute after completing a battle, the armor will restore you to full health. If your HP drops to zero or below, you will faint and lose the battle.

Monsters are attuned to certain elements, and may have a weakness to none or multiple elements. They may also absorb some elements, which recovers their HP. 

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

If a monster with multiple types has conflicting elemental attributes, its **Absorbs** characteristic overrides its weakness. For example, **Ghost** is a flying spirit. While flying enemies are normally weak to *Blowah*, spirits absorb *Blowah*, therefore, a **Ghost** will absorb *Blowah*.

As another example, dragons, being flying lizards, are supposed to be weak to *Coldah* and *Blowah*.

But an **Ice Dragon**, being *frigid*, will absorb *Coldah*, nullifying the normal weakness to this spell. So the **Ice Dragon** will only be weak to *Blowah* and will absorb *Coldah*.

Each *Test Case* will represent a battle you must win or run away from. Winning battles give you experience, so you will only run if the battle is unwinnable (that is, the enemies are unbeatable, or they will render you unconscious before you can defeat them).

Battles are turn-based and you will always move first, starting with **15 HP**. You must cast a spell, and may not pass your turn. You win when all monsters' HP drop to zero or below. After your turn, all living monsters will attack you (dealing 1 HP of damage per living monster), and afterward, a new round begins. There is no way to heal yourself during a battle.

Your task is to find the shortest sequence of spells to dispatch the monsters. If there is more than one optimal sequence, output the lexicographically smallest one. You must try and win, but for hopeless battles, output `"R"` (Run). 

A valid sequence of spells will be a string of characters made up of any number of `"B", "C"`, and `"H"`, which stand for the first letter of each spell: (B)lowah, (C)oldah and  (H)ottah. Spells should simply be concatenated together without separators.

Monsters are given as an array of strings in the following semicolon-separated format:

`"Monster Name;Types (comma-separated);initial HP"`

For example:

`"Ice Dragon;dragon,frigid;35"`

__Example__

* For 
```
monsters: ["Goblin;humanoid;4",
"Goblin;humanoid;4",
"Goblin;humanoid;4"]
```
You may cast any spell twice to defeat the three goblins (each spell deals 2 HP of damage because they are weak to nothing and absorb nothing). Remember that any spell hits all monsters at once.

The expected output is `"BB"` (two Blowahs) because it's the shortest and lexicographically smallest sequence of spells.

* For
```
monsters: ["Flame wolf;blazing;12",
"Ice leopard;frigid;13"]
```
The wolf is weak to *Coldah* and absorbs *Hottah*, while the opposite holds for the leopard.

The optimal spell sequence is `""`

| Turn | Spell | Flame W. | Ice L. | Your HP |
|--|--|--|--|--|
| (start) | (none) | 0 | 0 | 15 |
| 1 | Coldah | 0 | 0 | 15 |
| 1 | monsters attack | 0 | 0 | 13 |
| 2 | Hottah | 0 | 0 | 13 |
| 2 | monsters attack | 0 | 0 | 11 |

(your HP is the last column and you may have to resize this panel to see it)

* For
```
monsters: ["Magic haze;vortex;3",
"Iguana;lizard;12"]
```
the expected output is `"R"` because vortices absorb all spells (resulting in their HP increasing every turn). You will never be able to win this battle, so you must run away.

* For 

```
monsters: ["Iron golem;humanoid;20",
"Iron golem;humanoid;20"]
```
You need to cast any spell 10 times to defeat these monsters, but on the 8th round, they would have dealt 16 HP of damage to you. You cannot win and should output `"R"`, saving yourself from defeat.

__Input / Output__
"""

inputoutput = """
The list of monsters in this particular battle. Each string represents a monster in the format

`"NAME;TYPES (comma-separated);HP"`

The shortest sequence of spells you will cast that leads to victory, or `"R"` if you must run away. If more than one optimal sequence exists, output the lexicographically smallest one.

"""

