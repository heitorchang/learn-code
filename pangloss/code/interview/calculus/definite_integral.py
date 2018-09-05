def definite_integral(coeffs, a, b):
    """For the integral of a polynomial with given coefficients,
    where the rightmost element is a constant, second-to-last is x,
    third-to-last is x^2, etc.

    For definite_integral([1, 0, 1], 0, 2),
    the anti-derivative is (1/3)x^3 + x = [1/3, 0, 1]
    """
    anti_derivative = []  # ignore C, constant value
    len_coeffs = len(coeffs)
    for i, coeff in enumerate(coeffs):
        power = len_coeffs - i
        anti_derivative.append(1 / power * coeff)

    # compute anti_derivative with a and b
    len_anti_derivative = len(anti_derivative)
    result = 0
    for i, coeff in enumerate(anti_derivative):
        power = len_anti_derivative - i
        result += coeff * b ** power
        result -= coeff * a ** power
    return result

def test():
    testeql(definite_integral([1, 0, 1], 0, 2), 14/3)
    testeql(definite_integral([6, -5, 2], -3, 1), 84)
