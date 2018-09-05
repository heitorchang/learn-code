def checkio(number):
    product = 1
    while number > 0:
        digit = number % 10
        if digit != 0:
            product *= digit
        number //= 10
    return product
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print('end of tests')
