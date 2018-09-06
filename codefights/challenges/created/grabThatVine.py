description = """
Help *Quicksand Larry* escape from furious natives through the jungle by grabbing on to vines and swinging above and past deadly quicksand pits!

After Larry had "acquired" the sacred, golden *Mozca Macaque Head* from a secret cave, the natives began their chase after *his* head for taking their relic.

Larry is desperately running in a straight line towards his airplane, where his pilot awaits and will immediately take off upon reaching it.

Between the cave entrance and the airplane are multiple quicksand pits, and long, precarious vines swing above them.

### The Game

Larry's path to safety is represented as `100` squares, starting from 0 at the left end, which is just outside the cave, to `99` at the right end, where the airplane waits for him. As soon as Larry reaches square `99`, he flies away and is safe from the natives.

Each quicksand pit takes up `3` squares and Larry will not dare step on them. A vine swings back and forth above `5` squares: a solid square on each end of the pit and the `3` pit squares.

The vines move predictably and each one of them has a fixed rate of movement (these rates are independent of each other). For each vine, the time (in seconds) it takes for it to move from one end to the other will be given.

Larry moves at a rate of one square per second, and if he reaches a vine's end at the exact second it arrives, he immediately jumps up (losing momentum) to grab on to it. The vine will then swing to the other end at its given speed. Otherwise, he must wait until the vine is reachable.

Upon reaching the other end of the pit, Larry jumps off and acrobatically slashes the vine with his machete, thus slowing down the natives. He immediately resumes running toward the airplane. 

Though more theoretically-minded treasure hunters may wish to optimize wait times and ideal points of vine contact to see the absolute fastest time they can reach the airplane, Larry has a simple rule: **run, don't think!** 

Besides, mathematics wasn't really his strong suit--he thought a GCD was a Giant Corn Dog!


"""
