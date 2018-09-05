from math import cos, sqrt, pi

def sideLen(a, b, angleC):
    return sqrt(a*a + b*b - 2*a*b*cos(angleC))

def radToDeg(r):
    return r / pi * 180

def degToRad(d):
    return d / 180 * pi

def test():
    testeql(degToRad(90), pi / 2)
    testeql(radToDeg(pi), 180)
    testeql(sideLen(2.5, 7.2, degToRad(23)), 4.99518)
