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
