def toggle_bit(n, idx):
    """Toggle bit at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    toggle_mask = 1 << idx
    return n ^ toggle_mask  # use XOR

def test():
    testeql(toggle_bit(0b10011, 1), 0b10001)
    testeql(toggle_bit(0b10001, 4), 1)
    testeql(toggle_bit(0b1, 3), 0b1001)
