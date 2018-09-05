def replaceRL(w):
    return w.replace('right', 'left')

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return ",".join(map(replaceRL, phrases))

def test():
    testeql(replaceRL("bright"), "bleft")
    testeql(replaceRL("bright right"), "bleft left")
    testeql(left_join(("brightness wright",)), "bleftness wleft")
    testeql(left_join(("left", "right", "left", "stop")), "left,left,left,stop")
