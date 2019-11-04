def isArithmeticProgression(sequence):
    c = [b - a for (a, b) in zip(sequence, sequence[1:])]

    cs = set(c)
    return len(cs) == 1
