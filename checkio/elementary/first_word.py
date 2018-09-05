import re

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    pat = re.compile(r"[\w']+")
    return pat.search(text).group(0)

def test():
    testeql(first_word("Hello world"), "Hello")
    testeql(first_word("... andy's ..."), "andy's")
