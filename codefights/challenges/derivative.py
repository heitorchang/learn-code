def parseMonomial(m):
    # return [coef, power of x]
    # coeff == 1
    if m.find("*") == -1:
        if m.find('x') == -1:
            # constant
            return [int(m), 0]
        else:
            if m == 'x':
                return [1, 1]
            elif m == '-x':
                return [-1, 1]
            elif m.find('^') != -1:
                x_parts = m.split('^')
                if x_parts[0] == "-x":
                    return [-1, int(x_parts[1])]
                else:
                    return [1, int(x_parts[1])]        
            elif m.find('x') != -1:
                return [int(m[:-1]), 1]
    # split by "*"
    coef_xs = m.split("*")
    coef = coef_xs[0]
    xs = coef_xs[1]

    # x by itself
    if xs.find('^') == -1:
        # power is 1
        return [int(coef), 1]

    # find power
    x_pow = xs.split('^')
    if x_pow[0] == "-x":
        return [-1, int(x_pow[1])]
    else:
        return [int(coef), int(x_pow[1])]

def derivative(p, x):
    # format: monomial [ +/- other monomial ]*
    monomials = []
    tokens = p.split()

    # parse first monomial
    monomials.append(parseMonomial(tokens[0]))

    for i in range(1, len(tokens), 2):
        sign = 1 if tokens[i] == "+" else -1
        m = parseMonomial(tokens[i+1])
        monomials.append([m[0] * sign, m[1]])

    degree = max([pw[1] for pw in monomials])

    poly = [0 for _ in range(degree+1)]

    for m in monomials:
        poly[m[1]] += m[0]

    deriv = [0 for _ in range(degree)]
    for p in range(1, len(poly)):
        deriv[p-1] = p * poly[p]

    result = 0
    for p in range(len(deriv)):
        result += x ** p * deriv[p]

    return result

def test():
    testeql(parseMonomial("15"), [15, 0])
    testeql(parseMonomial("30*x"), [30, 1])
    testeql(parseMonomial("23*x^8"), [23, 8])

    testeql(parseMonomial("1"), [1, 0])
    testeql(parseMonomial("x"), [1, 1])
    testeql(parseMonomial("-1"), [-1, 0])
    testeql(parseMonomial("-x"), [-1, 1])
    testeql(parseMonomial("-x^3"), [-1, 3])
    
    # testeql(derivative("3*x^2 - x^4 + 8", -2), 20)
    # testeql(derivative("-3*x^2 + x^3 - 1000", -1), 9)
    testeql(derivative("23*x^8 + 53*x - -97*x^5 - -44*x^2 + 36*x - 85*x^3 - -23*x", -4), -2894816)
    testeql(derivative("2*x^2 - -x^12 - 15*x^3 + 172x", 0), 172)
