description = """
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.
"""

import re

def reverseInParentheses(inputString):
    if inputString.find("(") == -1:
        return inputString
    pat = re.compile(r'.*(?P<wrapped>\(.*?\)).*')

    s = pat.search(inputString)
    if s:
        print(s.group('wrapped'))
        n = inputString.replace(s.group('wrapped'), s.group('wrapped')[-2:0:-1])
        print(n)
        return reverseInParentheses(n)


reverseInParentheses("foo(bar(baz))blim"), "foobazrabblim",


# test(

#    reverseInParentheses("(bar)"), "rab",

#    reverseInParentheses("foo(bar)baz"), "foorabbaz",

#
#    )
    
    
