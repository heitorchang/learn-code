def longestp(s):

    ###
    # BROKEN after copying
    ###


    # DP table
    len_s = len(s)
    table = [[False for i in range(len_s)] for j in range(len_s)]
    for i in range(len_s):
        table[i][i] = True

    max_length = 1
    start = 0
    for length in range(2, len_s+1):
        for st in range(len_s - length + 1):
            end = st + length - 1
            if length == 2:
                if s[st] == s[end]:
                    table[st][end] = True
                    max_length = length
                    st = start
            else:
                if s[st] == s[end] and table[st+1][end-1]:
                    table[st][end] = True
                    max_length = length
                    st = start
    return s[start:start+max_length]


def test_long():
    print(longestp("ABBC"))
    print(longestp("cdaabbbaacd"))
    print(longestp("abracarba"))
