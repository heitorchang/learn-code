# Produce combinations of a certain length, given a list of items

from collections import namedtuple

ChoicePair = namedtuple("CP", "selected, remaining")

def divide(cp):
    result = []
    for i in range(len(cp.remaining)):
        elem = cp.remaining[i]
        result.append(ChoicePair(cp.selected + [elem], cp.remaining[i+1:]))
    return result

def my_combinations(lst, n):
    iteration = [ChoicePair([], lst)]
    for i in range(n):
        result = []
        for cp in iteration:
            result.extend(divide(cp))
        iteration = result
    
    return [cp.selected for cp in result]
