# SICP p. 103
# Find x such that f(x) = x

def fixed_pt(f, x):
    prev = x
    trial = f(x)
    while abs(trial - prev) > 0.0001:
        prev = trial
        trial = f(trial)
    return trial

# y = sqrt(x)
# y^2 = x
# y = x/y
# y + y = x/y + y
# 2y = x/y + y
# y = (1/2) * (x/y + y)

# don't think of y as f(x)
# find fixed point of sqrt(x) such that sqrt(x) = x

def fixed_sqrt(x):
    return fixed_pt(lambda y: 0.5 * (x/y + y), x)

# sqrt(2) :
# 1.414 = (1/2) * (2/1.414 + 1.414)

def check(sqrt_x, x):
    # should return sqrt_x if sqrt_x is the square root of x
    return 0.5 * (x/sqrt_x + sqrt_x)
