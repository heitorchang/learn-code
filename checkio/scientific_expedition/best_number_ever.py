def checkio():
    """In our world watched by Big Brother, we must identify every member of the world. Including oneself."""
    return id(checkio)

def test():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    testeql(checkio(), 0)
    assert isinstance(checkio(), (int, float, complex))
