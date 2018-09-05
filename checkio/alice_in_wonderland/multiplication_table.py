from operator import and_, or_, xor

def dec_to_bin_list(n):
    """Produce a list of bits from a decimal integer"""
    return list(map(int, bin(n)[2:]))

def robot_multiply(n, m, operation):
    """Given n x m, convert to a header row and initial column, and
    apply the operation"""
    
    left_col = dec_to_bin_list(n)
    header = dec_to_bin_list(m)
    total = 0
    
    for r in left_col:
        row = ""
        for c in header:
            row += str(operation(r, c))  # accumulate bits as a string
        total += int(row, 2)  # convert from bit string to decimal int
    return total

def checkio(first, second):
    grand_total = 0
    operations = [and_, or_, xor]
    for op in operations:
        grand_total += robot_multiply(first, second, op)
    return grand_total

def test():
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
