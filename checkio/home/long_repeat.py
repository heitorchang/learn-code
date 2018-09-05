def long_repeat(line):
    max_len = 0
    current_len = 0  # length of current run of characters
    current_char = None
    
    for c in line:
        if c != current_char:
            # found a different character
            max_len = max(max_len, current_len)
            current_len = 1
        else:
            # same character, add to length
            current_len += 1
        current_char = c
    max_len = max(max_len, current_len)  # consider single character run
    return max_len


def test():
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, 'aa'
    print('"Run" is good. How is "Check"?')
