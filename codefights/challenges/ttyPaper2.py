import re

def TTYPaperTape2(tapeText):
    tapeText = tapeText.replace("_", "")
    opsPat = re.compile(r'[+\-*/\^]')

    ops = [o if o != "^" else "**" for o in opsPat.findall(tapeText)]
    nums = opsPat.split(tapeText)

    print(ops)
    print(nums)

    ans = nums[0]
    nums = nums[1:]

    # how to distinguish negatives from subtraction?
    # subtraction has two numbers surrounding it. negative numbers don't

test(

    TTYPaperTape2("2.3*_3.7"), None,
    TTYPaperTape2(" 2 /  7^-1+3.1415_^7"), None,
    )
