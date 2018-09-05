def swap_letter(c):
    if c.islower():
        return c.upper()
    else:
        return c.lower()

def swap_case(s):
    return "".join(map(swap_letter, s))
