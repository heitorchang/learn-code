from itertools import zip_longest

arr = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*arr)))

arr_uneven = [[1, 2], [3, 4, 5, 6], [7, 8, 9]]
print(list(zip_longest(*arr_uneven, fillvalue=0)))

def test():
    pass
