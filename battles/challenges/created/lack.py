def lack(s):
    for c in s:
        if not (65 <= ord(c) <= 90 or ord(c) == 32):
            raise ValueError("invalid character in input")
    alphabet = set(chr(i) for i in range(65, 65+26))
    s = s.replace(' ', '')
    ss = set(s)
    return len(alphabet - ss)
