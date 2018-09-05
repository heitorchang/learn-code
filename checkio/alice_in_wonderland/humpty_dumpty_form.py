from math import asin, atanh, sqrt, pi

def checkio(height, width):
    c = height / 2
    a = width / 2

    if c == a:  # sphere
        area = 4 * pi * a ** 2
        vol = (4 / 3) * pi * a ** 3
    else: 
        if c < a:
            e = sqrt(1 - (c ** 2) / (a ** 2))
            area = 2 * pi * a ** 2 * (1 + ((1 - e ** 2) / e) * atanh(e))
        else:
            e = sqrt(1 - (a ** 2) / (c ** 2))
            area = 2 * pi * a ** 2 * (1 + (c / (a * e)) * asin(e))

        vol = ((4 * pi) / 3) * a ** 2 * c

    return [round(vol, 2), round(area, 2)]
        

def test():
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"

    
