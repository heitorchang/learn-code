def count_words(text, words):
    total = 0
    text = text.lower()
    for word in words:
        if text.find(word) > -1:
            total += 1
    return total

def test():
    #These "asserts" using only for self-checking and not necessary for auto-testing
    testeql(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}), 3)
    testeql(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}), 2)
    testeql(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}), 1)
