description = """
You're the CEO of a small toy company, so small that the company only has 2 employees and 2 types of work:

manufacturing the toys (task number 1)
painting the toys (task number 2)
You're given a 2 × 2 matrix skills, such that skills[i][j] shows the skill level of (i + 1)th employee in (j + 1)th task. So skills[0][0] is the skill level of the first employee in the first task, skills[1][0] is the skill level of the second employee in the first task, etc. Assume that output quality equals skill.

Your goal is to assign exactly one task to each employee in such a way that the quality of the result is maximized. It's guaranteed that the answer is unique.
"""

def easyAssignmentProblem(skills):
    """Idea: simulate assignment of first worker to first task, and second worker to second task. If the combined skill this assignment is higher than the alternative, [1, 2] is the best answer.

    The problem states that the answer is unique.
    """
    
    if skills[0][0] + skills[1][1] > skills[0][1] + skills[1][0]:
        return [1, 2]
    return [2, 1]


def test():
    testeql(easyAssignmentProblem([[1,3], 
                                   [2,3]]), [2,1])
    testeql(easyAssignmentProblem([[3,1], 
                                   [2,1]]), [1,2])
