def encrypt_letter(c, delta):
    ord_a = ord('a')  # save value
    if c.islower():
        plain_index = ord(c) - ord_a
        enc_index = (plain_index + delta) % 26
        return chr(enc_index + ord_a)
    else:
        return c
        
def to_encrypt(text, delta):
    return ''.join([encrypt_letter(c, delta) for c in text])

def test():
    testeql(encrypt_letter('a', 3), 'd')
    testeql(encrypt_letter('a', -3), 'x')
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
