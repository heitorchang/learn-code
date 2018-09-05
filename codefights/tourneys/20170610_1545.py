def iterate(s, digitCt, curDigit, result):
    if s == "":
        return result
    if s[0] == curDigit:
        return iterate(s[1:], digitCt + 1, curDigit, result)
    else:
        return iterate(s[1:], 1, s[0], result + str(digitCt) + curDigit)


def lookAndSaySequenceNextElement(element):
    return iterate(element[1:], 1, element[0], "")
    # does not pass



def test():
    testeql(lookAndSaySequenceNextElement("1211"), "111221")
