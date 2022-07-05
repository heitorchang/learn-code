# https://pythonalgos.com/technical-interviews-finding-the-longest-palindrome/

# DP problem

def longestPalindrome(s):
    # create dp table
    table = [[False for i in range(len(s))] for i in range(len(s))]
    # set "diagonals" to true
    for i in range(len(s)):
        table[i][i] = True
    # max length of the longest palindrome is currently 1
    max_length = 1
    # starting index is currently 0
    start = 0
    # double for loop to go through all the lengths starting with 2
    for length in range(2,len(s)+1):
        # loop through all possible starting indices
        for _start in range(len(s)-length+1):
            # declare end index
            end = _start + length - 1
            # if we're checking for a length of 2
            if length==2:
                # we only need to check two values
                if s[_start] == s[end]:
                    table[_start][end]=True
                    max_length = length
                    _start = start
            else:
                # we need to check the bookend values and ensure the
                # values in the middle are already set to true
                if s[_start] == s[end] and table[_start+1][end-1]:
                    table[_start][end]=True
                    max_length = length
                    _start = start
    return s[start:start+max_length]
