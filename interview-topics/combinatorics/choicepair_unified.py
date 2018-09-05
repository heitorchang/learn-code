from collections import namedtuple

ChoicePair = namedtuple("CP", "selected, remaining")

def exclude_index(lst, index):
    """(For permutations) Return the lst without element at index"""
    return lst[:index] + lst[index+1:]

def step_choices(cp, with_replacement=True):
    result = []
    for i in range(len(cp.remaining)):
        elem = cp.remaining[i]
        if with_replacement:
            new_remaining = exclude_index(cp.remaining, i)
        else:
            new_remaining = cp.remaining[i+1:]
        result.append(ChoicePair(cp.selected + [elem], new_remaining))
    return result

def iterate_choices(lst, n, permute):
    choices = [ChoicePair([], lst)]
    for i in range(n):
        result = []
        for cp in choices:
            result.extend(step_choices(cp, with_replacement=permute))
        choices = result
    return [cp.selected for cp in result]

def my_permutations(lst, n):
    return iterate_choices(lst, n, True)

def my_combinations(lst, n):
    return iterate_choices(lst, n, False)
