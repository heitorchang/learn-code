import re

def swap(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    
def push_bit(s):
    """Given a string like '0110100', push bits towards the right.
    Returns 'END' if nothing can be pushed
    """
    end_pattern = re.compile(r'^0*1+$')
    if end_pattern.match(s):
        return "END"

    else:
        bit_lst = list(s)
        
        first_one = bit_lst.index('1')
        # print("first_one", first_one)

        # if a pattern 10 is found, counting from the left, swap them
        if bit_lst[first_one+1] == '0':
            swap(bit_lst, first_one, first_one+1)

        else:
            # look for index of the right side of string of ones
            end_of_ones = first_one + bit_lst[first_one:].index('0') - 1
            swap(bit_lst, end_of_ones, end_of_ones+1)

            num_ones = end_of_ones - first_one + 1

            # print("{} {}".format(first_one, end_of_ones))
            # push left remaining ones

            # fill with zeros
            bit_lst[0:end_of_ones] = '0' * end_of_ones

            # fill with ones
            bit_lst[0:num_ones-1] = '1' * (num_ones-1)
            
            # print("end_of_ones", end_of_ones)
        return "".join(bit_lst)

def generate_bit_lst(items, n):
    result = set()
    bit_str = '1' * n + '0' * (items-n)
    while bit_str != "END":
        result.add(bit_str)
        print(bit_str)
        bit_str = push_bit(bit_str)

    return result

# OBSERVATION: generate_bit_lst is the set of permutations of '11100'
# Computing permutations is expensive, though
