def binsearch(alist, val):
    first = 0
    last = len(alist) - 1

    while first <= last:
        midpt = (first + last) // 2
        if alist[midpt] == val:
            return val
        if val < alist[midpt]:
            last = midpt - 1
        else:
            first = midpt + 1
    return f"{val} not found"


def test_binsearch():
    a = [1]
    print("a 1", binsearch(a, 1))
    print("a 2", binsearch(a, 2))

    b = [1, 2, 3]
    print("b 1", binsearch(b, 1))
    print("b 2", binsearch(b, 2))
    print("b 3", binsearch(b, 3))
    print("b 4", binsearch(b, 4))

    c = [1,2,3,4,5]
    print("c 4", binsearch(c, 4))
    print("c 14", binsearch(c, 14))
