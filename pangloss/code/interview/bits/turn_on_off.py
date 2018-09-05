"""Given an arbitrary bit sequence, turn a specific bit on or off"""

def turn_bit_on(n, idx):
    """Turn n's bit on (set to 1) at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    # idea:
    #    0b?????
    # OR 0b00100
    #    -------
    #        x   will always equal 1

    on_seq = 1 << idx
    return n | on_seq

def turn_bit_off(n, idx):
    """Turn n's bit off (set to 0) at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    # idea:
    #     0b?????
    # AND 0b11011
    #     -------
    #         x   will always equal 0

    bit_len = n.bit_length()
    off_seq = ~(1 << idx)  # NOT operator, switches on/off

    print(bin(off_seq))
    return n & off_seq

def test():
    testeql(turn_bit_on(0b1000, 2), 0b1100)
    testeql(turn_bit_on(0b1000, 0), 0b1001)
    testeql(turn_bit_off(0b10101, 2), 0b10001)
    testeql(turn_bit_off(0b111, 0), 0b110)
    testeql(turn_bit_off(0b10010111, 4), 0b10000111)
