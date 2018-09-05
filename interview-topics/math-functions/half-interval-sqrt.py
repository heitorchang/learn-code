# half-interval method SICP p. 101

def try_pt(x):
    return x * x

def find_sqrt(x):
    if x < 0:
        raise ValueError("x must be non-negative")
    if x == 0:
        return 0
    min_pt = 0
    max_pt = x
    midpoint = (min_pt + max_pt) / 2
    trial = try_pt(midpoint)

    while abs(trial - x) > 0.0001:
        # print(min_pt, midpoint, max_pt, trial)

        if trial > x:
            max_pt = midpoint
        else:
            min_pt = midpoint
        midpoint = (min_pt + max_pt) / 2
        trial = try_pt(midpoint)
    return midpoint
