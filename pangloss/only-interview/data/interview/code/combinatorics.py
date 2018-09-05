from itertools import permutations, combinations

def permutation_branch(pair):
    """Given (base, rest), take each item in rest and append to base)"""
    out = []
    base, rest = pair
    for i, n in enumerate(rest):
        out.append((base + [n], rest[:i] + rest[i+1:]))
    return out

def my_permutations(a, n):
    """Obtain a list of permutations of items in a, each with n items

    Idea: branch out with all possible single items, and remember
    which other ones are left. Build each branch with the remaining items.
    """

    a = list(a)
    out = [([], a)]
    
    for i in range(n):
        step = []
        for pair in out:
            step.extend(permutation_branch(pair))
        out = step

    return [p for (p, rest) in out]


# Combinations

def push_rightmost_bit(bs):
    """Find next bit string with the same number of ones"""
    rightmost_10 = bs.rfind("10")
    if rightmost_10 == -1:
        return False  # cannot push any more
    # count number of ones to the right of 10
    ones_to_move = bs[rightmost_10 + 1:].count("1")
    zeros_left = len(bs) - rightmost_10 - ones_to_move - 2
    return bs[:rightmost_10] + "01" + ("1" * ones_to_move) + ("0" * zeros_left)

def bitstring_combination(a, bs):
    return [elem for (i, elem) in enumerate(a) if bs[i] == "1"]

def my_combinations(a, n):
    a = list(a)
    len_a = len(a)
    bs = ('1' * n) + ('0' * (len_a - n))
    out = []
    while bs:
        out.append(bitstring_combination(a, bs))
        bs = push_rightmost_bit(bs)
    return out


# Tests

def test():
    testeql(permutation_branch(([], ['a','b','c'])), [(['a'], ['b', 'c']), (['b'], ['a', 'c']), (['c'], ['a', 'b'])])
    testeql([''.join(w) for w in my_permutations('abc', 3)], ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    testeql([''.join(w) for w in my_permutations('abc', 2)], ['ab', 'ac', 'ba', 'bc', 'ca', 'cb'])

    testeql(push_rightmost_bit("11010"), "11001")
    testeql(push_rightmost_bit("1001010"), "1001001")
    testeql(push_rightmost_bit("1001001"), "1000110")
    testeql(push_rightmost_bit("1000110"), "1000101")

    testeql(bitstring_combination("abc", "010"), ['b'])

    testeql(my_permutations('abcde', 3), [list(p) for p in permutations('abcde', 3)])
    testeql(my_combinations('abcde', 3), [list(c) for c in combinations('abcde', 3)])
