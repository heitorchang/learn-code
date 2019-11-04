def decipher(cipher):
    answer = ""
    while cipher:
        cur_letter = cipher[0]
        if cur_letter == "1":
            code = cipher[:3]
            answer += chr(int(code))
            cipher = cipher[3:]
        else:
            code = cipher[:2]
            answer += chr(int(code))
            cipher = cipher[2:]
    return answer

def test():
    testeql(decipher("10197115121"), "easy")
    
