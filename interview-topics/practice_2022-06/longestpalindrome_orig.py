def longestPalindrome(_string):

    ###
    # fix'd: start = _start lines
    ###


    # create dp table
    table = [[False for i in range(len(_string))] for i in range(len(_string))]
    # set "diagonals" to true
    for i in range(len(_string)):
        table[i][i] = True
    # max length of the longest palindrome is currently 1
    max_length = 1
    # starting index is currently 0
    start = 0
    # double for loop to go through all the lengths starting with 2
    for length in range(2,len(_string)+1):
        # loop through all possible starting indices
        for _start in range(len(_string)-length+1):
            # declare end index
            end = _start + length - 1
            # if we're checking for a length of 2
            if length==2:
                # we only need to check two values
                if _string[_start] == _string[end]:
                    table[_start][end]=True
                    max_length = length
                    start = _start
            else:
                # we need to check the bookend values and ensure the
                # values in the middle are already set to true
                if _string[_start] == _string[end] and table[_start+1][end-1]:
                    table[_start][end]=True
                    max_length = length
                    start = _start
    return _string[start:start+max_length]

print(longestPalindrome("ABBC"))
print(longestPalindrome("ABCCBBBA"))
print(longestPalindrome("CDAABBBAACD"))
print(longestPalindrome("AAB"))
print(longestPalindrome("ABCDEFG"))
print(longestPalindrome("AABBAA"))
