def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """

    saveSign = '-' if number < 0 else ''
    number = abs(number)
    curPower = powers[0]
    for i in range(len(powers)-1):
        if number >= base:
            if decimals == 0:
                number //= base
            else:
                number /= base
            curPower = powers[i+1]

    if decimals == 0:
        # use int to round towards zero
        numPart = "{}".format(int(number))
    else:
        # round through format 
        numPart = "{:.{prec}f}".format(number, prec=decimals)

    return saveSign + numPart + "{pwr}{suf}".format(pwr=curPower, suf=suffix)

#These "asserts" using only for self-checking and not necessary for auto-testing
def test():
    # testeql(friendly_number(-150, base=100, powers=['','d','D']), '-1d')
    testeql(friendly_number(10 ** 32), '100000000Y')
    # testeql(friendly_number(102), '102')
    # testeql(friendly_number(10240), '10k')
    # runAsserts()
    
    # testeql(friendly_number(255000000000, powers=['', 'k', 'M']), '255000M')
    # testeql(friendly_number(1024000000, base=1024, suffix='iB'), '976MiB')

def runAsserts():
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
