def deleteDigit(n):
    maximal = 0
    s = str(n)
    for i in range(len(s)):
        val = int(s[:i] + s[i+1:])
        if val > maximal:
            maximal = val
    return maximal
