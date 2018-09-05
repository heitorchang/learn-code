# head-to-head fight vs. Negi_babu

def cyclicString(s1):

    for answer in range(1, len(s1)):
        correct = True
        for position in range(len(s1)):
            if s1[position] != s1[position - answer]:
                correct = False
                break
        if correct:
            pr('correct')
            return answer
    return len(s1)
    # not sure


def traverse(m, v, visited):
    options = m[v]
    hasChoice = -1
    for i in range(len(options)):
        if options[i] and i not in visited:
            hasChoice = i
            break
    if hasChoice == -1:
        return len(visited)
    else:
        return traverse(m, hasChoice, visited + [v])        

def dfsComponentSize(matrix, vertex):
    return traverse(matrix, vertex, [vertex])
# doesn't appear to handle a case like this correctly
#  (0)
#   |
#  (1) - (2)
#   |
#  (3)
    
# result 400 (7:21) : 200 (2:45) [pwnt]
# fight over after I submitted
# correct answer for Round 3

# 800 XP, 400 coins
    
def test():
    testeql(cyclicString("cabca"), 3)
    testeql(cyclicString("aba"), 2)
