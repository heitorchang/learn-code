from itertools import chain

def swapNeighboringDigits(n):
    digits = list(map(int, str(n)))
    evens = digits[::2]
    odds = digits[1::2]

    return int(''.join(map(str, chain(*zip(odds, evens)))))

test(swapNeighboringDigits(1234), 2143,
     swapNeighboringDigits(12), 21,
     swapNeighboringDigits(10), 1)
