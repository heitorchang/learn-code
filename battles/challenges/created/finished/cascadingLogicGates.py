link = '''
https://app.codesignal.com/challenge/Wj9MT3GCBMyq8k949
'''

from random import choice

description_no_dup = """
You're using a digital circuit simulator to learn the basics of logic gates but it seems like your rival has installed a virus in it!

In this software, gates are placed so that the input `A` to the gate is a horizontal line above the second input `B`, and the gate's output `Y` is drawn as a line to the right of the gate.

There are six types of gates: `AND, NAND, OR, NOR, XOR, XNOR`. Below is a diagram (with truth tables) that give the correct outputs for all possible inputs.

![diagram](https://i.imgur.com/CmUkP6e.jpg)

The virus restricts you to initially placing gates only in parallel; that is, one on top of another.

After running one step of the simulation, the gates' output wires are placed as inputs to copies of the gates (in the same order from top to bottom) while there are still available outputs.

The output of the first two gates will go into the next step's first gate, the third and fourth into the next step's second gate, and so on.

If it happens that at the bottom there is only one wire remaining, it won't be connected to anything going forward.

This process is repeated until only one gate and its output is produced.

You think that even in the face of adversity, you will use this situation to enrich your understanding of electronics.

Given an array of gates and their initial inputs, output the total number of times a `1` is outputted by any gate.

**Note:** Do not add the `1`s in the initial inputs to the total.

__Example__

For
```
gates = ["XOR", "NAND", "OR"]
```
and
```
inputs = [1, 0, 1, 1, 0, 1]
```

The two steps in the simulation are (pardon the ASCII Art, you may need to resize this panel to see it in full):

```
1 -         
   )- XOR  = 1 -
0 -             )
                 )-- XOR  = 1
1 -             )            
   )- NAND = 0 -             
1 -                          
                             
0 -                          
   )-  OR  = 1 
1 -            
```

The output is `3`, corresponding to outputs equal to `1` from:

* Both `XOR` gates
* The first `OR` gate

For
```
gates = ["AND", "OR", "XOR", "NAND"]
```
and
```
inputs = [1, 1, 0, 1, 1, 1, 0, 1]
```

```
1
 ) AND  = 1
1
            ) AND = 1
0
 ) OR   = 1
1
                      ) AND = 1
1
 ) XOR  = 0
1
            ) OR  = 1
0 
 ) NAND = 1
1
```
The output is `6`.

"""


def opp(x):
    if x == 0:
        return 1
    else:
        return 0

def gateOutput(typ, x, y):
    if typ == "AND":
        return x & y
        
    elif typ == "NAND":
        return opp(x & y)
        
    elif typ == "OR":
        return x | y

    elif typ == "NOR":
        return opp(x | y)

    elif typ == "XOR":
        return (x ^ y)

    elif typ == "XNOR":
        return opp(x ^ y)

    else:
        raise ValueError

def cascadingLogicGates(gates, inputs):
    return cascadingLogicGatesStep(gates, inputs, 0)
    

def cascadingLogicGatesStep(gates, inputs, total):
    lenGates = len(gates)
    
    #print()
    #print()
    

    #print("TOTAL:", total)
    #print("INPUTS:", inputs)
    #print("GATES:", gates)
    
    newInputs = []
        
    for i in range(lenGates):
        newInput = gateOutput(gates[i], inputs[i*2], inputs[i*2 + 1])
        # print(gates[i], inputs[i*2], inputs[i*2 + 1], newInput)
        if newInput == 1:
            #print("gate output +1")
            total += 1
        newInputs.append(newInput)
        
    if lenGates == 1:
        return total

    newGates = gates[:lenGates//2 + 1]
        
    return cascadingLogicGatesStep(newGates[:-1], newInputs, total)


def generateTestCase(leng):
    g = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR"]
    i = [0, 1]
    gates = []
    inputs = []

    for j in range(leng):
        gates.append(choice(g))
        inputs.append(choice(i))
        inputs.append(choice(i))

    print(str(gates).replace("'", '"'))
    print()
    print()
    print(inputs)
    print()
    print(cascadingLogicGates(gates, inputs))

def testOutput():
    g = ["AND", "NAND", "OR", "NOR", "XOR", "XNOR"]

    for gate in g:
        for x in range(2):
            for y in range(2):
                print(gate, x, y, gateOutput(gate, x, y))

test(
     cascadingLogicGates(["XOR", "NAND", "OR"], [1, 0, 1, 1, 0, 1]), 3,
    cascadingLogicGates(["AND", "OR", "XOR", "NAND"], [1,1,0,1,1,1,0,1]), 6)
