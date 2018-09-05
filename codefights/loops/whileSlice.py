# Given a string (or array), iterate as follows:
# take the first character as a "base"
# produce all slices that start with this base
# once all slices are produced, advance the base to the right

def subslices(s):
    baseIndex = 0
    lenS = len(s)
    while baseIndex < lenS:
        subslice = ""
        endIndex = baseIndex
        while endIndex < lenS:
            subslice += s[endIndex]
            endIndex += 1
        baseIndex += 1

def test():
    testeql(subslices('abcde'), None)

        
