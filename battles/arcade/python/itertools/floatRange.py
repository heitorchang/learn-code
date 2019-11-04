import math
from itertools import takewhile, count

def floatRange(start, stop, step):
    """Doesn't really use itertools"""
    gen = [start + i * step for i in range(math.ceil((stop-start)/step))]
    return list(gen)

    
def floatRange_hanknq_iter(start, stop, step):
    gen = takewhile(lambda x: x < stop,
                    count(start, step))
    return list(gen)
    
def test():
    testeql(floatRange_hanknq_iter(-0.9, 0.45, 0.2), [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3])
