from collections import defaultdict

def launchSequenceChecker(systemNames, stepNumbers):
    def isStrictlyInc(lst):
        diffs = [(b - a) > 0 for (a, b) in zip(lst, lst[1:])]
        return all(diffs)
        
    systems = defaultdict(list)
    for i in range(len(systemNames)):
        systems[systemNames[i]].append(stepNumbers[i])

    # check lists

    for system in systems:
        pr('systems[system]')
        if not isStrictlyInc(systems[system]):
            return False
    return True

def testLaunchSequence():
    testeql(launchSequenceChecker(["stage_1", 
                                   "stage_2", 
                                   "dragon", 
                                   "stage_1", 
                                   "stage_2", 
                                   "dragon"], [1, 10, 11, 2, 12, 111]), True)

    
packetDescription = """
SpaceX has built a reliable Earth-Mars communication system that uses n links to transmit messages that are broken into fragments. The messages are sequences of ASCII characters that terminate with '#'. n copies of each fragment are sent, meaning that normally n copies of each fragment are received (one per link). However, some fragments may be lost. It's also possible that they can be corrupted or arrive out of order.

Each fragment contains the following data:

    seq - The sequential number of the fragment in the message. This part of the fragment is never corrupted.
    fragmentData - A single character from the message contained in the fragment.

Implement a function that receives an array of message fragments and reconstructs the original message according to the following rules:

    For each sequential number, pick the data character that is present in more than 50% of the fragments with that sequential number. Note that we calculate 50% based on the total number of copies that were sent (which is always equal to n), while the number of received fragments can be smaller.
    The last fragment of the message that's been reconstructed according to rule 1 (and no other fragment) contains '#'.
    There can be no gaps in the message, so all of the fragments numbered 0, 1, 2, ..., <number of the last fragment> should be restored.

If the message cannot be reconstructed, return an empty string. Otherwise, return the reconstructed message.

Example

For seq = [1, 1, 0, 0, 0, 2, 2, 2], fragmentData = ['+', '+', 'A', 'A', 'B', '#', '#', '#'], and n = 3, the output should be
packetDescrambler(seq, fragmentData, n) = "A+#".

    For the fragment with index 0 (sequential number), 2 'A's and 1 'B' were received. So, the number of fragments with 'A' is more than 50% out of n = 3. Both parts of rule 1 hold, meaning that the initial character of the message is 'A'.
    For the fragment with index 1 (sequential number), 2 '+'s were received and the third fragment was lost. Again, the number of fragments with '+' is more than 50% out of n = 3. Therefore, the next character of the message is '+'.
    For the fragment with index 2 (sequential number), 3 '#'s were received. All the sent fragments agree, so rule 1 holds. There are no fragments with a sequential number of more than 2, meaning that this is the last character. Since this character is '#', rule 2 holds as well.
    Note that there were no gaps before '#', so rule 3 holds. Hence, the message can be considered correctly reconstructed.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer seq

    An array of non-negative integers. seq[i] contains the sequential number of the ith received fragment.

    Guaranteed constraints:
    1 ≤ seq.length ≤ 105,
    0 ≤ seq[i] < 25000.

    [input] array.char fragmentData

    An array of characters. fragmentData[i] contains a printable ASCII character transmitted in the ith received fragment.

    Guaranteed constraints:
    fragmentData.length = seq.length.

    [input] integer n

    The number of links (in other words, the number of copies of the message that were sent).

    Guaranteed constraints:
    3 ≤ n ≤ 25000.

    [output] string

    Return the reconstructed message. If the message can't be reconstructed correctly, return an empty string.

"""

from collections import defaultdict, Counter

def overHalf(ctr, n):
    mc = ctr.most_common(2)
    
    if len(mc) < 1:
        raise ValueError("No data")
    if len(mc) > 1 and mc[0][1] == mc[1][1]:
        raise ValueError("Ambiguous data (more than one most common)")
    ratio = mc[0][1] / n
    if ratio <= 0.5:
        raise ValueError("Data is not majority")
    return mc[0][0]    

def packetDescrambler(seq, fragmentData, n):
    msgLen = max(seq)
    charDict = defaultdict(Counter)
    for i in range(len(seq)):
        charDict[seq[i]].update(fragmentData[i])
    msg = ""
    for i in range(msgLen+1):
        try:
            msg += overHalf(charDict[i], n)
        except ValueError:
            return ""
    if msg[-1] != "#":
        return ""
    return msg
    
def testPacketDescrambler():
    testeql(packetDescrambler([1, 1, 0, 0, 0, 2, 2, 2], ["+", 
                                                         "+", 
                                                         "A", 
                                                         "A", 
                                                         "B", 
                                                         "#", 
                                                         "#", 
                                                         "#"], 3),
            "A+#")

    testeql(packetDescrambler([1, 1, 0, 0, 0, 2, 2, 2], ["+", 
                                                         "+", 
                                                         "A", 
                                                         "A", 
                                                         "B", 
                                                         "#", 
                                                         "#", 
                                                         "#"], 4),
            "")
        
def cpuEmulator(subroutine):
    subroutine = ["NOP"] + subroutine  # make subroutines one-based
    instruction = 1
    
    R = [0 for _ in range(43)]  # registers

    def Rval(r):
        # parse Rxx and get its value
        return R[int(r[1:])]
        
    def MOV(a, b):
        if a[0] == 'R':
            # copy instruction
            R[int(b[1:])] = R[int(a[1:])]
        else:
            # set Rxx to constant d
            R[int(b[1:])] = int(a)

    def ADD(x, y):
        tmp = (Rval(x) + Rval(y)) % (2 ** 32)
        R[int(x[1:])] = tmp
        
    def DEC(x):
        tmp = Rval(x)
        if tmp == 0:
            tmp = 2 ** 32 - 1
        else:
            tmp -= 1
        R[int(x[1:])] = tmp

    def INC(x):
        tmp = Rval(x)
        if tmp == 2 ** 32 - 1:
            tmp = 0;
        else:
            tmp += 1
        R[int(x[1:])] = tmp

    def INV(x):
        tmp = Rval(x)
        tmp = ~tmp & 0xFFFFFFFF
        R[int(x[1:])] = tmp

    # begin simulation

    counter = 1
    while True:
    # while counter < 30:
        tokens = subroutine[instruction].split()
        cmd = tokens[0]
        if cmd != "NOP":
            args = tokens[1]
        else:
            args = ""
        counter += 1
        print("start inst ", end="")
        pr('instruction cmd args')
        if cmd == "MOV":
            arglist = args.split(",")
            MOV(arglist[0], arglist[1])
            instruction += 1
        elif cmd == "ADD":
            arglist = args.split(",")
            ADD(arglist[0], arglist[1])
            instruction += 1
        elif cmd == "DEC":
            DEC(args)
            instruction += 1
        elif cmd == "INC":
            INC(args)
            instruction += 1
        elif cmd == "INV":
            INV(args)
            instruction += 1
        elif cmd == "JMP":
            # JMP(args)
            instruction = int(args)
        elif cmd == "JZ":
            if Rval("R00") == 0:
                instruction = int(args)
            else:
                instruction += 1
        elif cmd == "NOP":
            instruction += 1
        else:
            raise ValueError("Unknown command", cmd)

        pr('R')

        print()
        if instruction == len(subroutine):
            return str(Rval("R42"))
    
def test():
 #    testeql(cpuEmulator(["MOV 5,R00", 
 #                         "MOV 10,R01", 
 #                         "JZ 7", 
 #                         "ADD R02,R01", 
 #                         "DEC R00", 
 #                         "JMP 3", 
 #                         "MOV R02,R42"]), "50")

 #    testeql(cpuEmulator(["MOV 32,R00", 
 # "MOV 1,R41", 
 # "JZ 8", 
 # "MOV R41,R42", 
 # "ADD R41,R42", 
 # "DEC R00", 
 # "JMP 3", 
 # "NOP"]), "2147483648")

    testeql(cpuEmulator(["DEC R42", 
                         "INC R01", 
                         "ADD R02,R01", 
                         "ADD R00,R02", 
                         "ADD R00,R42", 
                         "JZ 1"]), "4294967294")
