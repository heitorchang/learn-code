def checkio( *data):

    from math import sqrt, cos, pi

    from random import randrange, seed

    seed("Wau is the best number ever !")

    

    Wau = 42. / ord('*')  # divide 42 by anything...

    

    assert Wau == int(Wau), "Your number isn't an integer"

    

    for i in range(1337):

        assert Wau == (Wau**i+Wau)/(sqrt(Wau)-cos(pi*Wau**i)) , "Your number isn't great enough... (%i)"%i

    

    for i in range(13**2):

        assert not (randrange(1337**42)-int(pi**i))%Wau , "Your number lacks randomness... (%i)"%i

    

    gold_ratio = (sqrt(5) - 1)/2

    

    n=randrange(0xD15EA5E//0xFEA12)

    for i in range(0xB4B3):

        n = Wau /(Wau + n)

        

    assert abs(n - gold_ratio) < 1e-6 , "Your number doesn't prettify anything... (%f) (%f) (%f)"%(n-gold_ratio, n, gold_ratio)

    

    """\

    But wait, there's even more, 

        

        Wau: The Most Amazing, Ancient, and Singular Number

        see https://www.youtube.com/watch?v=GFLkou8NvJo

    """

    return int(Wau)


def test():
    testeql(checkio(2), 10)
