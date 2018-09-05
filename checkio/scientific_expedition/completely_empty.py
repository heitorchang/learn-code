def completely_empty_visit(val, visited):
    # look for infinite loop : c = []; c.append(c)
    id_val = id(val)
    if id_val in visited:
        return False
    try:
        val = list(val)
        if isinstance(val, dict) and len(val) == 1:
            if list(val.keys())[0] != '':
                return False
        elif len(val) != 0:
            return all(completely_empty_visit(v, visited+[id_val]) for v in val)
    except TypeError:
        return False
    return True

def completely_empty(val):
    return completely_empty_visit(val, [])

    

def completely_empty_top(val):
    try:
        return all(map(completely_empty, val))
    except:
        return False


def test():
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    assert completely_empty([iter(())]) == True
    c = []
    c.append(c)
    assert completely_empty_top(c) == False
    print('Done')
