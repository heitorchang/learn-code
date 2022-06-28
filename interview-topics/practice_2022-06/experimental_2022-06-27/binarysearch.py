def binary_search(sorted_list, value):
    first = 0
    last = len(sorted_list) - 1

    # must be <= to cover endpoints
    while first <= last:
        midpoint = (first + last) // 2
        if sorted_list[midpoint] == value:
            return value
        if sorted_list[midpoint] > value:
            # must move away from midpoint
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False
