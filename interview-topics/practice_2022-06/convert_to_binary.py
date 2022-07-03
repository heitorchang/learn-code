def dec_to_bin(n):
    bin = ""
    while n > 0:
        bin += str(n % 2)
        n //= 2
    return "0B" + bin[::-1]
