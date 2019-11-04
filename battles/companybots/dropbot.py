def incorrectPasscodeAttempts(passcode, attempts):
    numIncorrect = 0
    for c in attempts:
        if c != passcode:
            numIncorrect += 1
        else:
            numIncorrect = 0
        if numIncorrect == 10:
            return True
    return False

def losslessDataCompression(inputString, width):
    length = len(inputString)
    i = 0
    result = ""
    
    while i < length:
    # while i <= 8:
        window = inputString[max(0, i - width):i]
        # find match
        windowLen = len(window)
        foundMatch = False
        for matchLen in range(windowLen, 0, -1):
            for startIndex in range(windowLen - matchLen, -1, -1):
                pr('i matchLen startIndex')
                print(window[startIndex:startIndex+matchLen])
                inx = inputString[i:i+matchLen].find(inputString[startIndex:startIndex+matchLen])
                if inx >= 0:
                    foundMatch = True
                    print("found inx", startIndex, matchLen)
                    result += "(" + str(startIndex) + "," + str(matchLen) + ")"
                    break
            if foundMatch:
                break
        if foundMatch:
            i += matchLen
        else:
            result += inputString[i]
            i += 1
    return result
    # give up

def displayDiff(oldVersion, newVersion):
    result = ""
    o = 0
    n = 0

    maxlen = max(len(oldVersion), len(newVersion))
    
    while True:
        if o >= len(oldVersion) and n >= len(newVersion):
            return result

        if o >= len(oldVersion):
            return result + "[" + newVersion[n:] + "]"

        if n >= len(newVersion):
            return result + "(" + oldVersion[o:] + ")"

        if oldVersion[o] == newVersion[n]:
            result += oldVersion[o]        
            o += 1
            n += 1
            
        else:
            # see which version has longer difference
            fo = newVersion[n:].find(oldVersion[o])
            fn = oldVersion[o:].find(newVersion[n])
            if fo == -1: fo = maxlen
            if fn == -1: fn = maxlen

            pr('o n oldVersion[o] newVersion[n] fo fn')
            if fn < fo:
                print("branch a")
                result += "(" + oldVersion[o:o+fn] + ")"
                o += fn
            elif fo < fn:
                print("branch b")
                result += "[" + newVersion[n:n+fo] + "]"
                n += fo
            else:
                print('branch c')
                result += "(" + oldVersion[o:o+fn] + ")" + "[" + newVersion[n:n+fo] + "]"
                o += fn
                n += fo
        pr('result o n')

def test():
    # testeql(losslessDataCompression("abacabadabacaba", 7), "ab(0,1)c(0,3)d(4,3)c(8,3)")
    # testeql(displayDiff("same_prefix_1233_same_suffix",
    #                     "same_prefix23123_same_suffix"),
    #         "same_prefix(_1)23[12]3_same_suffix")
    # testeql(displayDiff("a", "b"), "(a)[b]")
    # testeql(displayDiff("ab", "bb"), "(a)b[b]")
    testeql(displayDiff("a2_3b42c_78d",
                        "a_34c27_8ed"), "a(2)_3(b)4(2)c(_)[2]7[_]8[e]d")

    testeql(displayDiff("3b42c_", "34c27_"), "3(b)4(2)c(_)[2]7[_]")
