def specialPolynomial(x, n):
    total = 0
    for power in range(n):
        total += x ** power
        pr('power total')
        if total > n:
            return power - 1
        power += 1

def specialPolynomialWhile(x, n):
    power = 0
    total = 0
    while total <= n:
        total += x ** power
        pr('total power')
        power += 1
    pr('power')
    return power - 2

def htmlTable(table, row, column):
    i = 0
    row += 1
    column += 1
    while i < len(table):
        if table[i:i + 4] == '<tr>':
            row -= 1
            i += 5
        elif row == 0 and table[i:i + 4] == '<td>':
            column -= 1
            i += 4
            if column == 0:
                result = ''
                while table[i] != '<':
                    result += table[i]
                    i += 1
                return result
        else:
            i += 1
    return 'No such cell'

def test():
    testeql(specialPolynomial(3, 140), 4)
