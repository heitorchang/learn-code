def longestWordPhail(text):
    # strip non alpha or space
    st = ""
    for c in text:
        if c.isalpha() or c == ' ':
            st += c
    lst = st.split()
    lsts = sorted(lst, key=lambda w: len(w), reverse=True)
    return lsts[0]

def longestWord(text):
    # franciraldo
    return sorted(re.findall('\w+', text), key=len)[-1]

def test():
    testeql(longestWord("Ready, steady, go!"), "steady")
