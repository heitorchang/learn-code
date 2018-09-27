description = """
You have given a multiple-choice oral exam and received a tip that two of your students cheated.

You find it difficult to keep an eye on them at all times, so you estimate that a student can write on their paper unobserved for about seven questions at a time.
 
Therefore, when you inspect the two suspects' exam sheets, you will concentrate on continuous sequences of seven answers each.

A question may be answered as a choice between `A`, `B`, `C` and `D`. Because there is no penalty for guessing, students never leave anything blank.

You will consider a `7`-answer sequence *suspicious* if there are `4` or more **wrong** answers that are the same for both students. If they both wrote down the correct answer, it could be that they really knew it, and you cannot count it against them.

*Normal* answer sequences are those outside of *suspicious* sequences and may be of any size. In contrast, *Suspicious* sequences are always seven answers long and do not overlap. Whenever possible, you will produce as many *suspicious* sequences as you can.

If the total length of *suspicious* sequences exceeds the total length of *normal* sequences, you will consider their entire answer sheets *suspicious* and will grill them later to see if they confess to cheating. Otherwise, you will stay quiet.

Given the sequences `studentA`, `studentB` and `answerKey`, output whether the students' entire answer sheets are *suspicious* or not.

# To-do

consider tweaking seven-answer sequence length and number of wrong answers to be considered cheating
"""

from random import choice, randint
from itertools import combinations

SUSPICIOUS_BOUNDARY = 4

def generateSuspiciousTriple():
    CHOICES = "ABCD"
    pairs = list(combinations(CHOICES, 2))
    triples = list(combinations(CHOICES, 3))
    indices = range(7)
    a = ""
    b = ""
    c = ""

    combos = list(combinations(indices, SUSPICIOUS_BOUNDARY))
    cheatIndices = choice(combos)

    for i in range(7):
        if i in cheatIndices:
            pair = choice(pairs)
            r = randint(1, 2)
            if r == 1:
                a += pair[0]
                b += pair[0]
                c += pair[1]
            else:
                a += pair[1]
                b += pair[1]
                c += pair[0]
        else:
            r = randint(1, 2)
            if r == 0:
                ch = choice(CHOICES)
                a += ch
                b += ch
                c += ch
            else:
                triple = choice(triples)
                a += triple[0]
                b += triple[1]
                c += triple[2]
            
    return (a, b, c)
    
def generateAnswerSheet(questions):
    CHOICES = "ABCD"
    return [choice(CHOICES) for _ in range(questions)]


def generateRandomTriple():
    CHOICES = "ABCD"
    return (choice(CHOICES), choice(CHOICES), choice(CHOICES))
    
def generateTestCase(approxLen, cheatThreshold):
    # If a random integer from 1 to 100 is below cheatThreshold,
    # a suspiciousWindow is generated. Otherwise a single random answer
    # is generated

    # cheatThreshold = 11 seems to give a good mix of True and False
    # for approxLen = 3000
    
    i = 0
    a = ""
    b = ""
    c = ""
    while i < approxLen:
        r = randint(1, 100)
        # If 
        if r <= cheatThreshold:
            strs = generateSuspiciousTriple()
            i += 7
        else:
            strs = generateRandomTriple()
            i += 1
        a += strs[0]
        b += strs[1]
        c += strs[2]
    return (a, b, c)
        

def compareSequences(a, b):
    return [m == n for (m, n) in zip(a, b)]


def isWindowSuspicious(w):
    return w.count('y') >= SUSPICIOUS_BOUNDARY
    

def answersToCheatString(a, b, k):
    return ''.join(['y' if m == n and m != p else 'n' for (m, n, p) in zip(a, b, k)])

    
def multipleChoiceCheaters(a, b, k):
    if len(a) < 7:
        # a suspicious window is at least 7 answers wide
        return False
        
    # A suspicious answer is 'y', otherwise 'n'
    cheatString = answersToCheatString(a, b, k)

    # boundaries of window
    currentWindowLeft = 0
    currentWindowRight = 7

    suspiciousWindows = []
    
    
    while currentWindowRight <= len(a):
        window = cheatString[currentWindowLeft:currentWindowRight]
        if isWindowSuspicious(window):
            suspiciousWindows.append(window)
            currentWindowLeft += 7
            currentWindowRight += 7
        else:
            currentWindowLeft += 1
            currentWindowRight += 1

    suspiciousAnswersCount = len(suspiciousWindows) * 7
    nonSuspiciousAnswersCount = len(a) - suspiciousAnswersCount

    return suspiciousAnswersCount > nonSuspiciousAnswersCount
    

print(multipleChoiceCheaters("AAABBBBBBBAAA",
                             "AAABBBBBBBAAA",
                             "AAAAAAAAAAAAA"
))

                             
# t = generateTestCase(100, 11)
# multipleChoiceCheaters(*t)
# t[0]
# t[1]
# t[2]

