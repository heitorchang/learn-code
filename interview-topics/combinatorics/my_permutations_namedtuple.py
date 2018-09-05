from collections import namedtuple

ChoicePair = namedtuple("CPair", ['selected', 'remaining'])

def take_from(lst, index):
    return lst[:index] + lst[index+1:]

def expand(cp):
    result = []
    for i in range(len(cp.remaining)):
        result.append(ChoicePair(cp.selected + [cp.remaining[i]], take_from(cp.remaining, i)))
    return result

def permute(lst, n):
    choices = [ChoicePair([], lst)]
    for i in range(n): 
        result = []
        for cp in choices:
            result.extend(expand(cp))
        choices = result

    return [cp.selected for cp in result]
