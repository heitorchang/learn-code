# math.isclose, available in 3.5

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def areclose(lst_a, lst_b, rel_tol=1e-09, abs_tol=0.0):
    return all([isclose(a, b, rel_tol, abs_tol) for (a, b) in zip(lst_a, lst_b)])
