# A Fire Emblem parody

zero_comments = """
I think this is a really good problem btw

it's very challenging, but incorporates lots of important concepts

basically the way my solution works is that it finds all friendly units, finds all the positions where they could attack an enemy, then tries to assign those spots in such a way that no two units occupy the same spot or attack the same enemy

1. discover positions of all friendly units
zero_cool, 7 hours ago
2. bfs from each unit's position to find all possible attack points
zero_cool, 7 hours ago
3. dp / memo recursion over all attack points to find an arrangement that maxes attacks on enemies
zero_cool, 7 hours ago
step 3 may involve backtracking more than anything else

"""

zero_final_version = """
You are Nargit, the bold General of the Signalian Army in the turn-based, grid-based medieval strategy game *Flame Crest*.

It is your turn and you plan to strike as many enemy soldiers as possible with your Knights and Archers. A single blow to a lightly armored enemy soldier will render them incapable of counterattacking, and because you are a noble and merciful warrior, you will spare their lives.

At your disposal are **Knights** (mounted on horses and armed with swords) and **Archers** (on foot and armed with bows and arrows). Their stats are as follows:

| Type   | Movement | Attack range |
|--|--|--|
| Knight | 7 | 1 |
| Archer | 4 | 3 |

In the grid-based world of *Flame Crest*, movement and attack ranges are measured only vertically and horizontally, never diagonally. 

During your turn, you may move all your units simultaneously (vertically and horizontally, but not diagonally). Your units may freely pass through other friendly units, but only one unit may stop at a square (units cannot overlap). As a consequence, as long as two units move within their ranges, they may swap places.

Enemy units will block your way. The enemy cannot move any unit during your turn.

After moving any number of squares up to its limit, a unit may then attack an enemy located at the exact number of squares away from the attacker defined by their **attack range**. After attacking, the unit will remain in place for the rest of the turn. 

Attacking an enemy more than once is fruitless (and against the strategy described above). An enemy's square is never cleared during your turn.

A **Knight** may move from `0` to `7` squares, and can then attack an enemy directly above, below, to the left or to the right of their new position. (An immediate diagonal square counts as a distance of `2`, such as up and to the right, and is out of range).

An **Archer** may move from `0` to `4` squares, but their attack is ineffective at close range. After moving, they may fire at an enemy exactly three squares away (see diagram below). Archers may fire over other units (the arrow flies above all obstacles on a third dimension above the battlefield).

Below, the light blue squares indicate where an **Archer** may go. Supposing the unit has a clear path to `(5, 9)`, they can then attack an enemy in any red square.

![Archer movement and attack](https://i.imgur.com/3k6ncaU.png)

The battlefield grid is defined as an array of strings `grid`, where `E` is an **enemy**, `K` is one of your **Knights**, `A` an **Archer**, and `-` (dash) is an empty square. Each string represents a row of the battlefield.

Given the battlefield grid, determine the maximum number of unique enemies you can attack during your turn. 

__Example__
* For 
  ```
  grid: ["------------",
         "----E-------",
         "-----------E",
         "-E----------",
         "------------",
         "------------",
         "------------",
         "---E-----A--",
         "------------",
         "------------",
         "------------",
         "-K----------",
         "------K-----",
         "----------E-",
         "---------EAE"]
  ```
  the output should be `swordsAndArrows(grid) = 3`.

  You can wound a maximum of `3` enemies if your units move up. The topmost enemy is out of range. Though you may gang up on the middle enemy, it is not following the optimal strategy of disabling the largest number of enemy soldiers.

  Note that the Archer on `(10, 0)` is stuck and cannot attack at close range. The Knight may alternatively help the trapped Archer, but we are only interested in the maximum *number of attacked enemies*, independent of their locations.

  ![Chaotic battlefield](https://i.imgur.com/mn0Wly3.png)


* For 
  ```
  grid: ["------",
         "-E----",
         "------",
         "EEEEE-",
         "--K---",
         "------",
         "KKKKK-"]
  ```
  the output should be `swordsAndArrows(grid) = 5`.

  You may strike at most `5` enemies because the lone enemy is out of range. Each Knight should simply attack the enemy directly in front of them, and one Knight will not have to attack.

  ![Rows of soldiers](https://i.imgur.com/7ty9f3r.png)

* For `grid: ["EEKA"]`, the output should be `swordsAndArrows(grid) = 2`.

  We see how the **Archer** on `(3, 0)` may attack the enemy on `(0, 0)` because their arrows fly over any unit (on a third dimension above the battlefield). The archer's range is exactly `3`, so they cannot attack the enemy at `(1, 0)`, but the **Knight** can. The maximum number of enemies you can attack is `2`.

  ![Archer attacks fly over any unit](https://i.imgur.com/SQVzaLt.png)

* For `grid: ["EEKKA"]`, the output should be `swordsAndArrows(grid) = 2`.

  If nobody moves, the second `E` will get hit twice. So we have the second `K` swap places with `A` so that both enemies can be attacked.

  ![Swap places](https://i.imgur.com/aJUPnrS.png)


__Input / Output__
"""

inputs = """
The battlefield grid, where `"E"` is an enemy, `"K"` is one of your knights, `"A"` is one of your archers, and `"-"` (dash) is an empty square. Each string in the grid array represents a row. It's guaranteed that there's at least one enemy and one friendly unit on the grid.

*Guaranteed constraints*:
<code>1 &le; grid.length &le; 80</code>
<code>1 &le; grid[i].length &le; 180</code>
<code>grid[i][j] &isin; {"E", "K", "A", "-"}</code>
"""
