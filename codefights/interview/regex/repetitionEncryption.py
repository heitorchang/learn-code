def repetitionEncryption(letter):
    # patterns "not notice"
    # and "day days" are matching, but shouldn't
    # this pattern solves it
    # pattern = r'[^a-z]*([a-z]+)[^a-z]+\1[^a-z]'

    pattern = r'[^a-z]*([a-z]+)[^a-z]+\1\b'
    # pattern = r'\W*(\w+)\W*'
    regex = re.compile(pattern, re.IGNORECASE)
    print(re.findall(regex, letter))
    return len(re.findall(regex, letter))

def test():
    # testeql(repetitionEncryption("Hi, hi Jane! I'm so. So glad to to finally be able to write - WRITE!! - to you!"), 4)
    # testeql(repetitionEncryption("Do not notify me about this in the future"), 0)
    testeql(repetitionEncryption("Everything is fine, fine perfectly here. Here I have fun (fun all the day!) days. Although I miss you, so please please, Jane, write, write me whenever you can! Can you do that? That is the only (!!ONLY!!) thing I ask from you, you sunshine."), 9)  # day/days
    testeql(repetitionEncryption("let's s?,play%3with,1symbols88,/symbols"), 2)
