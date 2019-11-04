def nthNumber(s, n):
    pattern = re.compile(r'(?:.*?\d+\D*?){%d}.*?([1-9]\d*)' % (n - 1))
    return re.match(pattern, s).group(1)

    # (?: ... ) a non-capturing version of regular parentheses
    # {m} exactly m copies of the previous RE should be matched.

def test():
    testeql(nthNumber('123ab 39', 2), "39")
    testeql(nthNumber("8one 003number 201numbers li-000233le number444", 4), "233")
    testeql(nthNumber("some023020 num ber 033 02103 32 meh peh beh 4328 ", 5), "4328")
    # testeql(nthNumber("007 is an awesome agent", 1), "7")
    testeql(nthNumber("07 is an awesome agent", 1), "7")
    testeql(nthNumber("LaS003920tP3rEt4t04Yte0023s3t", 4), "4")
