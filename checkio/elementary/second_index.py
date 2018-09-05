import re

def second_index(text: str, symbol: str):
    # edit by hanna hofman
    
    index = text.find(symbol, text.find(symbol)+1) 
    if index == -1:
        return None
    else:
        return index

def second_index_submitted(text: str, symbol: str):
    # Originally I used re.finditer but it will needlessly search
    # for all occurrences of symbol. While it looks cooler, the
    # simple approach below should be more efficient.
    
    first_index = text.find(symbol)
    index_in_remainder = text[first_index+1:].find(symbol)
    if index_in_remainder == -1:
        return None
    else:
        return first_index + index_in_remainder + len(symbol)

def second_index_re(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    symbol_pat = re.compile(symbol)
    indices = list(symbol_pat.finditer(text))
    if len(indices) > 1:
        return indices[1].start()
    else:
        return None

def test():
    testeql(second_index("sims", "s"), 3)
    testeql(second_index("find the river", "e"), 12)
    testeql(second_index("bc", "a"), None)
