def differentiate(coeffs):
    """Differentiate 2x^3 - 4x^2 + 10 (given as [2, -4, 0, 10]).
    The result is 6x^2 - 8x. [6, -8, 0]
    """
    len_terms = len(coeffs)
    result = []
    for i, coeff in enumerate(coeffs[:-1]):
        power = len_terms - i - 1
        result.append(power * coeff)
    return result

def test():
    testeql(differentiate([2, -4, 0, 10]), [6, -8, 0])
    testeql(differentiate([4, 0, 0, -5, -3]), [16, 0, 0, -5])
