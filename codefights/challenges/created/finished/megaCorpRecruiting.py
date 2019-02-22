draft = """

You're the head of recruiting at MegaCorp and the CTO just announced `12` new developer job openings to be filled urgently! She noted that some roles are more desirable than others.

You scramble to get *your* job done, and heard really good things about [this cutting-edge technical interviewing platform](https://codesignal.com/). Why not give it a try?

After doing a bit of research, you find out that potential candidates are given a score between `600` and `850` after completing the coding test. In addition, the site offers a wide range of optional *Challenges* that anyone can try and solve, and a *Forum* open to any sort of discussion.

Clearly, one's coding ability should be the most important factor in hiring. You will accept candidates with a **score of `800` or more** points. 

In case candidates are tied in their test scores, the tiebreaker will be the total number of challenges each candidate solved. If these two values are tied again, the final criteria will be the number of forum posts each candidate wrote (after all, good communication skills are highly valued in software engineering).

You might find that more than `12` candidates are qualified. In this case, prioritize the candidates with lower ID numbers (those who interviewed better got the chance to take the test first and were assigned lower ID numbers).

Given a matrix of candidates who completed the coding test, output a list of integers of the candidates' IDs you will hire in the order of their aptitude (higher test scores first, then more challenges solved, more forum posts, and finally, those who interviewed better and thus have smaller ID numbers). The better candidates will have the more desirable roles.

Each row of this matrix is an array of integers representing a candidate, in this order:

```
[candidateID, testScore, challengesSolved, forumPostsWritten]
```

__Examples__

"""


description = """

You're the head of recruiting at MegaCorp and the CTO just announced `20` new developer job openings to be filled urgently! She noted that some roles are more desirable than others.

You scramble to get *your* job done, and heard really good things about [this cutting-edge technical interviewing platform](https://codesignal.com/). Why not give it a try?

After doing a bit of research, you find out that potential candidates are given a score between `600` and `850` after completing the coding test. In addition, the site offers a wide range of optional *Challenges* that anyone can try and solve, and a *Forum* open to any sort of discussion.

Clearly, one's coding ability should be the most important factor in hiring. You will accept candidates with a **score of `800` or more** points. 

In case candidates are tied in their test scores, the tiebreaker will be the total number of challenges each candidate solved. If these two values are tied again, the final criteria will be the number of forum posts each candidate wrote (after all, good communication skills are valued in any profession).

You might find that more than `20` candidates are qualified. In these scenarios, prioritize the candidates with lower ID numbers (those who completed the test first have lower ID numbers).

Given a matrix of candidates who completed the coding test, output a list of integers of the candidates' IDs in the order of their aptitude (higher test score, more challenges solved, more forum posts, and finally, those who arrived first). The better candidates will have the more desirable roles.

Each row of this matrix is an array of integers representing a candidate, in this order:

```
[candidateID, testScore, challengesSolved, forumPostsWritten]
```

"""


from collections import namedtuple
from operator import attrgetter

def megaSoftCorpHiring(candidates):
    Candidate = namedtuple("Candidate", "id score challenges forum")

    cs = [Candidate(*c) for c in candidates if c[1] >= 800]

    cs.sort(key=attrgetter("id"))
    cs.sort(key=attrgetter("score", "challenges", "forum"), reverse=True)
    return [c.id for c in cs][:7]


test(megaSoftCorpHiring(
[[3, 729, 39, 3],
 [4, 832, 112, 93],
 [2, 690, 22, 0],
 [1, 798, 5, 0]]

), [4],

     megaSoftCorpHiring(
[[3, 620, 0, 0],
 [1, 721, 3, 0],
 [2, 752, 92, 221]]

     ), [],

     megaSoftCorpHiring(
[[4, 800, 0, 0], 
 [2, 800, 0, 0], 
 [5, 840, 1, 1], 
 [1, 800, 0, 0], 
 [3, 720, 1, 1], 
 [6, 803, 1, 1], 
 [8, 838, 1, 1], 
 [10, 832, 1, 1], 
 [9, 763, 1, 1], 
 [7, 800, 0, 0]]

     ),  [5, 8, 10, 6, 1, 2, 4],

     )

import random

def generateCand(lSc, uSc, chall, forum):
    return [random.randint(lSc, uSc), random.randint(0, chall), random.randint(0, forum)]

def generateExact(sc, c, f):
    return [sc, c, f]
    
def generateRandomTestCase(lim):
    ids = list(range(1, lim+1))
    random.shuffle(ids)

    test = []
    for i in range(lim):
        test.append(generateCand(650, 839, 20, 6))

    random.shuffle(test)

    for i in range(lim):
        test[i] = [ids[i]] + test[i]
        
    return test


def generateEdgeCase(lim):
    pass
