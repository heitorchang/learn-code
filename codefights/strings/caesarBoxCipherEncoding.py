from itertools import chain

def caesarBoxCipherEncoding(inputString):
    side = int(math.sqrt(len(inputString)))
    s = inputString
    rows = [s[side*i:side*i+side] for i in range(side)]
    return ''.join(chain(*zip(*[list(j) for j in rows])))
    
test(caesarBoxCipherEncoding("a message"), "aea sgmse")
