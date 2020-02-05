debug = True

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.interactive(True)
plt.ion()

def gentest(x, y):
    pt = [0, 1]
    plt.plot([2,3,x],[4,5,y], 'go')
    plt.show(block=False)

gentest(1, 1)
