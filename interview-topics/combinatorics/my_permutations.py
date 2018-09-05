plan = """
input: [1,2,3], 3 (3-item long permutation
output: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]

input: [1,2,3], 1
output: [1], [2], [3]

input: [1,2,3], 2
output: [1,2], [1,3], [2,1], [2,3], [3,1], [3,2]

"""

def permute(lst, n):
    def add_choices(base, choices):
        result = []
        for i in range(len(choices)):
            choices_minus_current_choice = choices[:i] + choices[i+1:]
            result.append((base + [choices[i]], choices_minus_current_choice))
        return result
    
    if n == 0:
        return [([], lst)]  # a list of one tuple
    else:
        bases = permute(lst, n-1)
        result = []
        for base in bases:
            result.extend(add_choices(*base))
        return result
    
def first_try_permute(lst, n):
    if n == 0:
        return []

    if len(lst) >= n:
        if n == 1:
            return extend_with_choices(([], lst))

        if n > 1:
            bases = first_try_permute(lst, n-1)
            result = []
            for base in bases:
                result.extend(extend_with_choices(base))
            return result
        
        else:
            print("unexpected input")
        

def extend_with_choices(base_and_choices):
    base = base_and_choices[0]
    choices = base_and_choices[1]
    # return [([base + [choice],  for choice in choices]
    return [(base + [choices[i]], choices[:i] + choices[i+1:]) for i in range(len(choices))]

plan2 = """
[1,2,3] -> ([1], [2,3])
        -> ([2], [1,3])
        -> ([3], [1,2])

[1,2]
"""

def separate(lst):
    """ UNUSED """
    return [([lst[i]], lst[:i] + lst[i+1:]) for i in range(len(lst))]
