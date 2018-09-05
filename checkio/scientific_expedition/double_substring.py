def double_substring(line):
    """
    length of the longest substring that non-overlapping repeats more than once.
    """
    substrings = set()
    counts = {}
    
    # get all substrings
    len_line = len(line)
    for start in range(len_line):
        for end in range(start+1, len_line):
            substrings.add(line[start:end])

    for ss in substrings:
        count = line.count(ss)
        if count > 1:
            # ignore non-repeating substrings
            counts[ss] = count

    if counts:
        return len(max(counts, key=len))
    return 0
    

def test():
    assert double_substring('abababaab') == 3
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
