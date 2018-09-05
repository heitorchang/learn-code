def variableName(name):
    pat = re.compile('^[a-zA-Z_][a-zA-Z0-9_]*$')
    pr('pat.match(name)')
    return pat.match(name) is not None

def test():
    testeql(variableName("var_1_I"), True)
    testeql(variableName("q-q"), False)
