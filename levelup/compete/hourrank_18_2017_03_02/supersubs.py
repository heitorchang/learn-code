def get_subs(s):
    len_s = len(s)
    for init in range(len_s):
        for end in range(init+1, len_s+1):
            yield s[init:end]

def is_super(s):
    if s == "0":
        return True
    elif s[0] == "0" and len(s) > 1:
        return False
    elif int(s) % 6 == 0:
        return True
    else:
        return False

list(map(is_super, get_subs("4806"))).count(True)
