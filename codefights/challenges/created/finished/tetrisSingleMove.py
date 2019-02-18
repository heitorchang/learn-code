description = """

You're playing [Tetris](https://en.wikipedia.org/wiki/Tetris) on your GameBoy and the batteries are about to die. So you're going to make one final effort, then purposely end the game to record your high score.

Given the single piece you're going to place and the current state of the board, determine the maximal number of lines you can clear in this single move.

For this challenge, we assume you may not use tricks like temporarily "floating" the piece and performing a rotation to place it inside a gap. That is, assume after rotating a piece, it may only be placed straight downward.
"""

testCases = """

1.

livePiece =

["oooo"]

board =

[
"............",
"............",
"............",
"............",
"............",
"............",
"ooooo.oooooo",
"ooooo.oooooo",
"ooooo.oooooo",
"ooooo.oooooo",
"o.oooooo.ooo"]

ans = 4



2.

livePiece =

["oo", "oo"]

board =

[
"..................",
"..................",
"..................",
"..................",
"..................",
"..................",
"..................",
"ooooo..ooooooooooo",
"oooooooooooooooooo",
"oo.o.o.oooo.oooooo",
"ooooooo.oo...ooo.o",
"oooooooooo...o.ooo",
"oooooooooooooooooo"]

ans = 1


3.

livePiece =

["oo.", ".oo"]

board =

["..............",
"..............",
"..............",
"..............",
"..............",
"oo.oo.ooo.oo.o",
"oooo.o.oo..o.o",
"oo.ooo.oo.o.oo"]

ans = 0


4

livePiece =

["o..",
 "ooo"]

board =

[
".................",
".................",
".................",
".................",
".................",
".................",
".................",
"oo..ooooooooooooo",
"oo.oooooooooooooo",
"oo.oooooooooooooo",
"oo.oooooooooooooo",
"oo.oooooooooooooo",
"ooooo.ooo.o.o.ooo"]

ans = 3


5.

livePiece =

[".o.", "ooo"]

board =

["...................",
"...................",
"...................",
"...................",
"...................",
"oo.oooooooooooooooo",
"oo..ooooooooooooooo",
"oo.oooooooooooooooo",
"ooooooooooooooooooo"]

ans = 1

6.

livePiece =

["o.", "oo", "o."]

board =

["................",
"................",
"................",
"................",
"oo...ooooooooooo",
"ooo.oooooooooooo",
"oooooooooooooo.o",
"oooooooooooooo.o"]

ans = 2

7.

livePiece =

[
".o",
"oo",
"o."]

board = [
"................",
"................",
"................",
"................",
"................",
"ooo..ooooooooooo",
"ooo.oooooooooooo",
"ooooooooooooo.oo",
"..ooo.ooo.o.o.oo",
"ooooooo.oooooooo"]

ans = 2
