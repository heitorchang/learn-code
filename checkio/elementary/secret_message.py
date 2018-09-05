import re

def find_message(text):
    """Find a secret message"""
    p = re.compile(r'[^A-Z]')
    return p.sub('', text)

def test():
    testeql(find_message("How are you? Eh, ok. Low or Lower? Ohhh."), "HELLO")
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
