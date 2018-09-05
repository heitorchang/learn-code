import re

plan = """
choosing 2 out of any is easy
work in a triangle shape

  1,2,3,4
> 12, 13, 14
>>  23, 24
>>>   34

3 out of 4?

begin with 12, 13, 14, 23, 24, 34
take "remaining elems" only with indices greater than all base elements
123, 124
134
234
"""

def first_step_take_remaining(lst):
    """
    [1,2,3,4]
    12[34] 13[4] 14
    23[4] 24
    34
    """
    result = []
    for row in range(len(lst)-1):
        for elem in range(row+1, len(lst)):
            result.append(([lst[row], lst[elem]], lst[elem+1:]))
    return result

def extend_combination(bases_and_remaining):
    base_len = len(bases_and_remaining[0])  # assume input is well-formed
    target_len = base_len + 1
    valid_bases = filter(lambda tup: len(tup[0]) + len(tup[1]) >= target_len, bases_and_remaining)
    result = []

    return list(valid_bases)

# Insight from reading intro to "Generating subsets" in Skiena:
# There are 2^n subsets (combinations)
#
# we can model a choice as a bit string where 1 = have and 0 = do not have
# Geee-nious

def my_bit_combinations(lst):
    def subset(bit_str):
        if len(lst) != len(bit_str):
            raise ValueError("inconsistent input")
        zipped = zip(lst, list(bit_str))
        return [pair[0] for pair in filter(lambda tup: tup[1] == '1', zipped)]
    result = []
    n = len(lst)
    limit = 2 ** n
    for i in range(limit):
        result.append(subset(format(i, "0" + str(n) + "b")))

    return result

def partial_bit_strings(items, n_subset):
    """
    3, 1: 100, 010, 001
    3, 2: 110, 101, 011
    3, 3: 111

    110000
    101000
    100100
    100010
    100001
    011000
    010100
    010010

    111000
    110100
    110010
    110001
    101100
    101010

    1110
    1101
    1011
    0111

    0111
    1011
    1101

    00011
    00110
    01100
    11000
    00101
    01010
    10100
    01001
    10010
    10001

    1000001 z=7, sep=6
    """
    pass
    
def bit_wave(zeros):
    zeros_arr = ["0" for i in range(zeros)]
    wave = []
    for i in range(zeros):
        zeros_copy = zeros_arr[:]
        zeros_copy[i] = "1"
        wave.append("".join(zeros_copy))
    return wave

def bit_subsets(it, n):
    """
    111000
    110100
    110010
    110001
    101100
    101010
    101001
    100110
    """
    # n == 2
    items = it-1
    for i in range(items):
        waves = bit_wave(items-i)
        for wave in waves:
            print('0'*i + '1' + wave)

def wave_of_wave(it, n):
    """
    1000
    0100
    0010
    0001

    11000
    10100
    10010
    10001
    01100
    01010
    01001
    00110
    00101
    00011

    111000
    10
    """
    
    if n == 1:
        return bit_wave(it)
    else:
        return 0


def attach(levels):
    if levels == 0:
        return ""
    return "A" + attach(levels-1)

def next_bit_str(s):
    """Given a bit string, find the next (increasing) bit string, or return notice if the limit has been reached
    reversed from typical integers (push 1's to the right):
    110 -> 101
    011 -> None  (cannot push further)
    1010 -> 0110
    
    1001 -> 0101
    0101 -> 0011 -> END
    
    01101 -> 10011
    011101 -> 110101
    
    1100 -> 1010 -> 0110 -> 1001 -> 0101 -> 0011 -> end
    01101 -> 10011
    01110 -> 11001
    100110 -> 010110
    011001 -> 100101
    0011010 -> 1000110
    """
    lst = list(s)
    # print(lst)

    end_pattern = re.compile(r'^0*1+$')
    if end_pattern.match(s):
        return "END"
    first_one = lst.index('1')
    if lst[first_one+1] == '0':
        lst[first_one], lst[first_one+1] = lst[first_one+1], lst[first_one]  # swap 1 and 0 (equivalent to pushing the 1 to the right)
    else:
        end_of_first_ones = first_one + lst[first_one:].index('0') - 1
        # push leftmost ones to the left and push end_of_first_ones to the right
        # print(end_of_first_ones)
        number_of_ones_to_push_left = end_of_first_ones - first_one
        for i in range(number_of_ones_to_push_left):
            lst[i] = '1'
        for i in range(number_of_ones_to_push_left, end_of_first_ones):
            lst[i] = '0'
        lst[end_of_first_ones] = '0'
        lst[end_of_first_ones+1] = '1'

    return "".join(lst)

def bit_strs(items, n):
    bit_str = '1' * n + '0' * (items - n)
    while bit_str != "END":
        print(bit_str)
        bit_str = next_bit_str(bit_str)
