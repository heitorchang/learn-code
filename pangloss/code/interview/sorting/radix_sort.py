# Algorithms (Cormen)

from operator import itemgetter

def radix_sort(lst):
    """Sort a list of integers, first sorting by the ones place,
    then the tens, and so on"""

    # set up the list, separating numbers into digits
    lst_str = list(map(str, lst))
    len_longest = len(max(lst_str, key=len))
    lst_pad = [s.zfill(len_longest) for s in lst_str]

    for i in range(len_longest - 1, -1, -1):
        lst_pad.sort(key=itemgetter(i))
    return list(map(int, lst_pad))
