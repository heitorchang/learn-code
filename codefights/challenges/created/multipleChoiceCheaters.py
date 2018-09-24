description = """
You have given a multiple-choice oral exam and received a tip that two of your students cheated.

You find it difficult to keep an eye on them at all times, so you estimate that a student can write on their paper unobserved for about seven questions at a time.
 
Therefore, when you inspect the two suspects' exam sheets, you will concentrate on continuous sequences of seven answers each.

A question may be answered as a choice between `A`, `B`, `C` and `D`. Because there is no penalty for guessing, students never leave anything blank.

You will consider a seven-answer sequence *suspicious* if there are four or more **wrong** answers that are the same for both students. If they both wrote down the correct answer, it could be that they really knew it, and you cannot count it against them.

*Normal* answer sequences are those outside of *suspicious* sequences and may be of any size. In contrast, *Suspicious* sequences are always seven answers long and do not overlap. Whenever possible, you will produce as many *suspicious* sequences as you can.

If the total length of *suspicious* sequences exceeds the total length of *normal* sequences, you will consider their entire answer sheets *suspicious* and will grill them later to see if they confess to cheating. Otherwise, you will stay quiet.

Given the sequences `studentA`, `studentB` and `answerKey`, output whether the students' entire answer sheets are *suspicious* or not.

# To-do

consider tweaking seven-answer sequence length and number of wrong answers to be considered cheating
"""

from random import choice

def generateAnswerSheet(questions):
    CHOICES = "ABCD"
    return [choice(CHOICES) for _ in range(questions)]


def compareSequences(a, b):
    return [m == n for (m, n) in zip(a, b)]
