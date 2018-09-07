final_draft = """
Help *Quicksand Larry* escape from furious natives through the jungle by grabbing on to vines and swinging above and past multiple deadly quicksand pits!

After Larry "acquired" the sacred, golden *Mozca Macaque Head* from a secret cave, countless natives now want *his* head for taking their relic.

Larry is desperately running in a straight line towards his airplane, where his pilot awaits and will immediately take off upon reaching it.

### The Game

Larry's path to safety is represented as `100` squares, starting from 0 at the left end, which is just outside the cave, to `99` at the right end, where the airplane is waiting.

Each quicksand pit takes up `3` squares and Larry will not dare step on them. A vine swings back and forth above `5` squares: a solid square on each end of the pit and the `3` pit squares.

Larry moves on solid ground at a rate of one square per second.

### Vines

The vines move predictably and each one of them has a fixed rate of movement (but each vine has its own rate).

* At the beginning of the game, all vines are on the leftmost position.

* If Larry reaches a vine's end at the exact second it arrives, he immediately jumps up (losing momentum) to grab on to it.

* The vine must have completely reached the left end for Larry to grab on to it.

* The vine will then swing to the other end at its given speed.

* Otherwise, he must wait until the vine is reachable.

Upon reaching the other end of the pit, Larry jumps off and acrobatically slashes the vine with his machete, thus slowing down the natives. He immediately resumes running toward the airplane. 

An array of arrays of `vines` will be given, where each vine is a two-element array `[leftEndpoint, swingTime]`. The first value is the leftmost square (where Larry may grab on to it) and the second value, the time (in seconds) it takes for the vine to move from one end to the other.

### Notes

Though more theoretically-minded treasure hunters may wish to optimize wait times and ideal points in time of vine contact to find the absolute fastest time they can reach the airplane, Larry has a simple rule: **Run, don't Think!**

The companion game **Jungle Julie** (coming soon) will have Julie run the same courses without angry, spear-wielding natives chasing after her, so make sure to check it out and see how much faster she can reach the airplane! 

### Your task

Determine how many seconds it will take for Larry to reach the airplane by following his strategy of Run, Jump, Slash, Repeat.

__Example__

For

```
vines: [[1, 2], [7, 3]]
```

![Quicksand example](https://i.imgur.com/Y1ImCZ2.png)

In the diagram above, the white squares are solid ground, brown squares are impassable quicksand, and the thick green lines the vines, centered above the quicksand. Larry starts at square `0`. The vine locations all the way to the left are their initial positions.

Larry will get to square `1` on the first second, and the first vine will have just moved away. He has to wait until the fourth second to grab it. On the sixth second, he reaches the end of the first pit and slashes that vine. He must then advance two squares and wait again. After clearing the second pit, he dashes toward the airplane. He needs to run `88` squares to get to the airplane on `99`, so you will return `103`.

| Time | Larry | Vine 1 | Vine 2 |
|--|--|--|--|
| 0 | 0   | 1        | 7 |
| 1 | 1   | pit      | pit |
| 2 | 1   | 5        | pit |
| 3 | 1   | pit      | 11  |
| 4 | 1   | 1 (grab) | pit |
| 5 | pit | pit      | pit |
| 6 | 5   | 5        | 7   |
| 7 | 6   | pit      | pit |
| 8 | 7   | 1        | pit |
| 9 | 7   | pit      | 11  |
|10 | 7   | 5        | pit |
|11 | 7   | pit      | pit |
|12 | 7   | 1        | 7 (grab) |
|13 | pit | pit      | pit |
|14 | pit | 5        | pit |
|15 | 11  | pit      | 11  |
|16 | 12  | 1        | pit |
|...|...|...|...|
|103| 99 (escape) | ... | ... |

__Input / Output__

"""

description = """
Help *Quicksand Larry* escape from furious natives through the jungle by grabbing on to vines and swinging above and past deadly quicksand pits!

After Larry had "acquired" the sacred, golden *Mozca Macaque Head* from a secret cave, the natives began their chase after *his* head for taking their relic.

Larry is desperately running in a straight line towards his airplane, where his pilot awaits and will immediately take off upon reaching it.

Between the cave entrance and the airplane are multiple quicksand pits, and long, precarious vines swing above them.

### The Game

Larry's path to safety is represented as `100` squares, starting from 0 at the left end, which is just outside the cave, to `99` at the right end, where the airplane waits for him. As soon as Larry reaches square `99`, he flies away and is safe from the natives.

Each quicksand pit takes up `3` squares and Larry will not dare step on them. A vine swings back and forth above `5` squares: a solid square on each end of the pit and the `3` pit squares.

Larry moves on solid ground at a rate of one square per second.

### Vines

The vines move predictably and each one of them has a fixed rate of movement (but each vine has its own rate).

* At the beginning of the game, all vines are on the leftmost position.

* If Larry reaches a vine's end at the exact second it arrives, he immediately jumps up (losing momentum) to grab on to it.

* The vine must have completely reached the left end for Larry to grab on to it.

* The vine will then swing to the other end at its given speed.

* Otherwise, he must wait until the vine is reachable.

Upon reaching the other end of the pit, Larry jumps off and acrobatically slashes the vine with his machete, thus slowing down the natives. He immediately resumes running toward the airplane. 

An array of arrays of `vines` will be given, where each vine is a two-element array `[leftEndpoint, swingTime]`. The first value is the leftmost square (where Larry may grab on to it) and the second value, the time (in seconds) it takes for the vine to move from one end to the other.

### Notes

Though more theoretically-minded treasure hunters may wish to optimize wait times and ideal points in time of vine contact to see the absolute fastest time they can reach the airplane, Larry has a simple rule: **Run, don't Think!**

The companion game **Jungle Julie** (coming soon) will have Julie run the same courses without angry, spear-wielding natives chasing after her, so make sure to check it out and see how much faster she can reach the airplane! 

### Your task

Determine how many seconds it will take for Larry to reach the airplane by following his strategy of Run, Jump, Slash, Repeat.

__Example__

For

```
vines: [[1, 2], [7, 3]]
```

Larry will get to square `1` on the first second, and the first vine will have just moved away. He has to wait until the fourth second to grab it. On the sixth second, he reaches the end of the first pit and slashes that vine. He must then advance two squares and wait again. After clearing the second pit, he dashes toward the airplane.

| Time | Larry | Vine 1 | Vine 2 |
|--|--|--|--|
| 0 | 0   | 1        | 7 |
| 1 | 1   | pit      | pit |
| 2 | 1   | 5        | pit |
| 3 | 1   | pit      | 11  |
| 4 | 1   | 1 (grab) | pit |
| 5 | pit | pit      | pit |
| 6 | 5   | 5        | 7   |
| 7 | 6   | pit      | pit |
| 8 | 7   | 1        | pit |
| 9 | 7   | pit      | 11  |
|10 | 7   | 5        | pit |
|11 | 7   | pit      | pit |
|12 | 7   | 1        | 7 (grab) |
|13 | pit | pit      | pit |
|14 | pit | 5        | pit |
|15 | 11  | pit      | 11  |
|16 | 12  | 1        | pit |
|...|...|...|...|
|103| 99 (escape) | ... | ... |

![Quicksand example](https://i.imgur.com/Y1ImCZ2.png)

In the diagram above, the white squares are solid ground, brown squares are impassable quicksand, and the thick green lines the vines, centered above the quicksand. Larry starts at square `0`. The vine locations all the way to the left are their initial positions.

__Input / Output__

"""
