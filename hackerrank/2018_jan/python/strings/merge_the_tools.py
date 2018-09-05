"""

Consider the following:

A string,s  , of length n where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .

Summary: split s into equal parts, and for each part, delete duplicate letters. Print each of these parts in a new line

"""

def removeDuplicates(word):
    seen = set()
    out = ""
    for c in word:
        if c not in seen:
            out += c
            seen.add(c)
    return out

def splitToParts(s, size):
    """Split s to parts of given size"""
    return [s[i:i+size] for i in range(0, len(s), size)]

def merge_the_tools(string, k):
    parts = splitToParts(string, k)
    for p in parts:
        print(removeDuplicates(p))

def test():
    testeql(removeDuplicates("ADA"), "AD")
    # testeql(splitToParts("abcdefghi", 3), None)
    testeql(merge_the_tools("AABCAAADA", 3), None)
    
