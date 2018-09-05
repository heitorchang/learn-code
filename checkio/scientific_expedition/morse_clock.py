def convert_digit(n, width):
    bit_str = bin(n)[2:]
    bit_str = bit_str.zfill(width)
    return bit_str.replace('1', '-').replace('0', '.')

def checkio(raw_time):
    # convert to hh:mm:ss
    parts = raw_time.split(":")
    time = ":".join([p.zfill(2) for p in parts])
    # bit widths
    widths = [2, 4, 3, 4, 3, 4]
    result = ""
    counter = 0
    for i, c in enumerate(time):
        # hh:mm:ss
        if i == 2 or i == 5:
            result += ": "
        else:
            result += convert_digit(int(c), widths[counter]) + " "
            counter += 1
    return result.strip()
                                

def test():
    testeql(add_spaces("10:37:49"), "1 0 : 3 7 : 4 9")
    testeql(convert_digit(0, 4), "....")
    testeql(checkio("10:37:49"), ".- .... : .-- .--- : -.. -..-")
    testeql(checkio("00:1:02"), ".. .... : ... ...- : ... ..-.")
    testeql(checkio("23:59:59"), "-. ..-- : -.- -..- : -.- -..-")
