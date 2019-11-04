def telephoneGame(messages):
    answer = -1
    for i in range(len(messages)):
        if messages[i] != messages[0]:
            answer = i
            break
    return answer

def test():
    testeql(
