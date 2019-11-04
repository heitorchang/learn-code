def pagesNumbering(n):
    if n < 10:
        return n
    else:
        lower = len(str(n)) - 1
        pages = n - 10 ** lower + 1
        return (lower + 1) * pages + pagesNumbering(n - pages)

def test():
    testeql(pagesNumbering(11), 13)
    testeql(pagesNumbering(1000), 2893)
    testeql(pagesNumbering(13), 17)
    testeql(pagesNumbering(1001), 2897)
