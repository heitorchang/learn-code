def Nav(d):
    pos = [0, 0, 0]
    for c in d:
        if c == ">":
            pos[1] += 1
        elif c == "<":
            pos[1] -= 1
        elif c == "+":
            pos[2] += 1
        elif c == "-":
            pos[2] -= 1
        elif c == "^":
            pos[0] -= 1
        elif c == "v":
            pos[0] += 1
        else:
            raise ValueError("unknown direction")
    return pos
