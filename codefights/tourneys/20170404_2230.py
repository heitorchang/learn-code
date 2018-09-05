def alphaOnly(word):
    result = ""
    for c in list(word):
        if ord(c) >= 97 and ord(c) <= 122:
            result += c
    return result

def clean(word):
    result = ""
    for c in list(word):
        if ord(c) >= 97 and ord(c) <= 122:
            result += c
        else:
            result += " "
    return result

def repetitionEncryption(letter):
    s = clean(letter.lower())
    s.replace("-", " ")
    wordsOnly = []
    for w in s.split():
        if ord(w[0]) <= 122 and ord(w[0]) >= 97:
            wordsOnly.append(w.strip())
    total = 0
    for i in range(1, len(wordsOnly)):
        if wordsOnly[i-1] == wordsOnly[i]:
            total += 1
    return total

def test():
    testequal(repetitionEncryption("Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!"), 4)
    testequal(repetitionEncryption("Yo-yo, how's s it going going for ya? Ya is okay, okay'nt ya?"), 5)
