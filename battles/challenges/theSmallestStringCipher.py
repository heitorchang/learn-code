def greaterThanSlow(a, b):
    """Return -1 if a < b, 1 if a > b, 0 if equal"""
    if a == b:
        return 0
        
    lena = len(a)
    lenb = len(b)

    for i in range(min(lena, lenb)):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1
    else:
        if lena < lenb:
            return -1
        return 1

def greaterThan(a, b):
    if a[-1] == b[-1]:
        return 0
    if a[-1] < b[-1]:
        return -1
    return 1
    

class Node:
    def __init__(self, resta, restb, accum):
        self.resta = resta
        self.restb = restb
        self.accum = accum

    def cmp(self, other):
        return greaterThan(self.accum, other.accum)

        
def theSmallestStringCipher(a, b):
    return step(Node(a, b, ""))

    
def step(node):
    if node.resta == "" and node.restb == "":
        return node.accum
        
    if node.resta == "":
        return node.accum + node.restb
        
    elif node.restb == "":
        return node.accum + node.resta
        
    else:
        left = Node(node.resta[1:], node.restb, node.accum + node.resta[0])
        right = Node(node.resta, node.restb[1:], node.accum + node.restb[0])

        if left.cmp(right) == -1:
            return step(left)
        elif left.cmp(right) == 1:
            return step(right)
        else:
            return min(step(left), step(right))
        
    

def failTheSmallestStringCipher(a, b):
    # does not pass
    ans = ""
    while len(a) > 0 or len(b) > 0:
        if len(a) == 0:
            ans += b
            b = ""
            continue
        elif len(b) == 0:
            ans += a
            a = ""
            continue

        if a[0] == b[0]:
            rtbnd = 1
            while True:
                if a[rtbnd] == b[rtbnd]:
                    rtbnd += 1
                else:
                    break
            if a[rtbnd] < b[rtbnd]:
                ans += a[:rtbnd]
                a = a[rtbnd:]
            else:
                ans += b[:rtbnd]
                b = b[rtbnd:]
        elif a[0] < b[0]:
            ans += a[0]
            a = a[1:]
        else:
            ans += b[0]
            b = b[1:]
    return ans

"""
test(greaterThan("aa", "aa"), False,
     greaterThan("aa", "aaa"), False,
     greaterThan("aaa", "aa"), True,
     greaterThan("aab", "aac"), False,

     )
"""

    
test(theSmallestStringCipher("b", "baa"), "baab",
     theSmallestStringCipher("gdmz", "hello"), "gdhellmoz",
     theSmallestStringCipher("aca", "acz"), "aacacz",
     )
