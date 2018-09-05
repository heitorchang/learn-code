data = data.concat([
//////////////////////////////////////////////////////////////////////
//
// COMBINATORICS
//
//////////////////////////////////////////////////////////////////////

  
  { // begin new topic
    topic: 'Combinatorics',
    title: 'Permutations, generating',
    reference: 'Python Fluente, 480',
    description: `permutations(iter, n=len(iter)) produces permutations of the items in iter of length n.`,
    code: `
import itertools
list(itertools.permutations('abc', 2))
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
    `
  },

  { // begin new topic
    topic: 'Combinatorics',
    title: 'Combinations, generating',
    reference: 'Python Fluente, 480',
    description: `itertools.combinations(iter, n) produces subsequences of length n. combinations_with_replacements allows elements to be repeated as many times as possible.`,
    code: `
import itertools
list(itertools.combinations('cba',2))
# [('c', 'b'), ('c', 'a'), ('b', 'a')]

[''.join(c) for c in itertools.combinations_with_replacement('cba', 3)]
# ['ccc', 'ccb', 'cca', 'cbb', 'cba', 'caa', 'bbb', 'bba', 'baa', 'aaa']
    `
  },


  { // begin new topic
    topic: 'Combinatorics',
    title: 'Permutations, number of',
    reference: 'Discrete Math, 408',
    description: `The number of r-permutations (permutations with r elements) of a set with n elements is: n! / (n - r)!. For example, to choose 3 winners out of 100, we have 100 people for first place, 99 for second, and 98 for third = 100 * 99 * 98. (100 - 3)! = 97!, which are the values cancelled outfrom 100!`,
    code: `
# r-permutations out of a list of n elements
n! / (n - r)!
    `
  },

  { // begin new topic
    topic: 'Combinatorics',
    title: 'Combinations, number of',
    reference: 'Discrete Math, 410',
    description: `The number of r-combinations (combinations with r elements) of a set with n elements is: n! / (r! * (n - r)!)`,
    code: `
# r-combinations out of a list of n elements
n! / (r! * (n - r)!)    
    `
  },

  {
    topic: 'Combinatorics',
    title: 'Product (Cartesian) combines elements of multiple lists',
    reference: 'Python Fluente, 478',
    description: `itertools.product(it1, it2, ... itn, repeat=1) produces tuples of n elements, where n are the number of given iterables. repeat indicates how many times the given iterables are repeated.`,
    code: `
import itertools

[''.join(p) for p in itertools.product("AB", "CD", "EF")]
# ['ACE', 'ACF', 'ADE', 'ADF', 'BCE', 'BCF', 'BDE', 'BDF']

[''.join(p) for p in itertools.product("AB", repeat=3)]
# ['AAA', 'AAB', 'ABA', 'ABB', 'BAA', 'BAB', 'BBA', 'BBB']
    `
  },

  { // begin new topic
    topic: 'Combinatorics',
    title: 'Permutations, iterative method',
    reference: '',
    description: `An iterative method to produce permutations of length n from a sequence a. The idea is to branch out at each step with all possible single items left from the remaining items, accumulating to each result.`,
    code: `
def permutation_branch(pair):
    """Given (base, rest), take each item in rest and append to base)"""
    out = []
    base, rest = pair
    for i, n in enumerate(rest):
        out.append((base + [n], rest[:i] + rest[i+1:]))
    return out

def my_permutations(a, n):
    a = list(a)
    out = [([], a)]
    
    for i in range(n):
        step = []
        for pair in out:
            step.extend(permutation_branch(pair))
        out = step
    return [p for (p, rest) in out]
    `
  },

  { // begin new topic
    topic: 'Combinatorics',
    title: 'Combinations with bit strings',
    reference: '',
    description: `A combination can be thought of a mapping between a bit string and the indices of the whole collection. If an index is 1 (True), the element is in the combination; 0 (False) means it is not. We iterate through bit strings with n ones (making it have n elements).`,
    code: `
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
    
    `
  },


]);
