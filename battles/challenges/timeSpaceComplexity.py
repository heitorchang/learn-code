MEM = 0
CPU = 0
VARS = {}

def myadd(a, b):
    global MEM, CPU
    CPU += 1
    print("adding", a, b)
    a = int(a)
    b = int(b)
    print("returning", a+b)
    return a + b

def myget(name):
    global VARS, CPU
    CPU += 1
    return VARS[name]

def myset(name, val):
    global VARS, CPU
    CPU += 1
    VARS[name] = val
    
def myeq(a, b):
    global MEM, CPU
    CPU += 1
    return a == b

def mywhile(cond, block):
    global MEM, CPU
    CPU += 1
    while True:
        if not myeval(cond):
            break
        for line in block:
            myeval(line)

def myeval(fn, args):
    return fn(*args)

def parseLine(line):
    fname, *args = line.split()
    myeval(eval("my" + fname), args)

def timeSpaceComplexity(code, intArray):
    global MEM, CPU
    for line in code:
        parseLine(line)

    print(MEM, CPU)
