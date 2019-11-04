def countLineColorings(points, colors):
    total = colors
    c = colors
    for i in range(points-1):
        total *= c - 1
    return total

def dfsCheckTree(matrix):

    visited = []
    componentSize = [0]
    cyclesFound = [False]

    def dfs(currentVertex, parentVertex):
        visited[currentVertex] = True
        componentSize[0] += 1
        for nextVertex in range(len(matrix)):
            if (matrix[currentVertex][nextVertex]
              and nextVertex != parentVertex):
                if not visited[nextVertex]:
                    dfs(nextVertex, currentVertex)
                else:
                    cyclesFound[0] = True

    for i in range(len(matrix)):
        visited.append(False)

    dfs(0, 1)  # fix this line

    if componentSize[0] == len(matrix) - 1 and not cyclesFound[0]:
        return True

    return False

piano_dp_desc = """
While walking in the forest one day, you and your friends come across an abandoned wooden house. Upon entering the house, you notice an old piano standing near the window, and a ghostly hand playing on it! When you came closer, you realize it's playing the music written in a book laid out in front of it. Not one to believe in ghosts, once you get home you decide to try and make a robotic version of the ghostly piano-playing hand.

The first step is to write a program for it. Here's your idea: your robotic hand will have fingers fingers, and your piano will have keys keys. The hand will receive a melody to play as a 2-dimensional array, where melody[i] is the set of keys that should be pressed at the ith second. The hand will play the melody by placing its fingers over piano keys and pressing them according to the melody. Each finger can be placed over no more than one key at a time, and can keep pressing the same key over several seconds.

There are two types of moves your hand can make:

A vertical move where it switches the states of some fingers, i.e. a finger which was pressing a key may be lifted up (still staying above the same key), while a finger which was above another key may press it. Such a move doesn't require any energy.
A horizontal move where it changes the subset of keys under the fingers. Any such move requires one unit of energy.
You may choose the initial state and position of each finger at no cost. After each second (i.e. between two consecutive pieces of melody) you can make any of the above-described moves (or both of them, or none).

As you want this hand to play music for as long as possible without charging it, the amount of energy spent on playing should be kept to a minimum.

Your goal is to find the minimal number of units of energy the hand requires to play the given melody.

Example

For fingers = 5, keys = 7 and
melody = [[2, 3], [3, 6], [2, 6], [1, 2], [2, 3], [1, 2, 4], [1, 2, 3, 5, 7]],
the output should be
pianoMelody(fingers, keys, melody) = 1.

First it's optimal to place the fingers above the keys 1, 2, 3, 4 and 6. This way you can play the first 6 parts of the melody using only vertical moves. After that you will need one horizontal and one vertical move to play the last part of the melody. The answer is 1 because the hand makes only one horizontal move.

Check out the image below for better understanding:



Input/Output

[time limit] 4000ms (py3)
[input] integer fingers

An integer, the number of fingers on the robotic hand.

Guaranteed constraints:
1 ≤ fingers ≤ 10.

[input] integer keys

An integer, the number of keys on the piano.

Guaranteed constraints:
1 ≤ keys ≤ 20.

[input] array.array.integer melody

Array of arrays of integers, the given melody, where melody[i] is the set of distinct keys that should be pressed at the same time.

Guaranteed constraints:
1 ≤ melody.length ≤ 20,
1 ≤ melody[i].length ≤ min(fingers, keys),
1 ≤ melody[i][j] ≤ keys.

[output] integer

The minimal number of units of energy the robotic hand should spend to play the given melody.
"""

def pianoMelody(fingers, keys, melody):
    def update(mel, check, diff):
        for m in mel:
            if not check[m]:
                check[m] = True
                diff += 1
        return diff

    dp = [float('inf') for l in range(len(melody))]
    dp[0] = 0
    for i in range(1, len(melody)):
        check = [False for l1 in range(keys + 1)]
        diff = update(melody[i], check, 0)
        for j in range(i, 0, -1):
            if diff <= fingers:
                dp[i] = ...  # fill in this
                diff = update(melody[j - 1], check, diff)
            else:
                break
        if diff <= fingers:
            dp[i] = 0
    return dp[len(melody) - 1]


def test():
    testeql(countLineColorings(2,3), 6)
    testeql(dfsCheckTree([[False,True,True], 
 [True,False,False], 
 [True,False,False]]), True)
