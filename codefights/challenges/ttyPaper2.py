import re

def TTYPaperTape2(tapeText):
    tapeText = tapeText.replace("_", "").replace(" ", "")
    opsPat = re.compile(r'[+\-*/\^]')

    ops = [o if o != "^" else "**" for o in opsPat.findall(tapeText)]
    nums = opsPat.split(tapeText)

    ops.append("X")
    
    print(ops)
    print(nums)

    msgnums = []
    msgops = []
    
    while nums:
        if nums[0] == '':
            msgnums.append('-' + nums[1])
            nums = nums[2:]

            msgops.append(ops[1])
            ops = ops[2:]
        else:
            msgnums.append(nums[0])
            nums = nums[1:]

            msgops.append(ops[0])
            ops = ops[1:]

    ans = msgnums[0]
    msgnums = msgnums[1:]

    print(ans, msgops, msgnums)
    
    for o, n in zip(msgops, msgnums):
        ans = eval(str(ans) + o + n)

        print(ans)
        
    return round(float(ans))


test(

#    TTYPaperTape2("_-1.234+_7.6 /  0.09"), 71,
    TTYPaperTape2(" 2 /  7^-1+3.1415_^7"), 569985)
