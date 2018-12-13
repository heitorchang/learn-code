# pass

def decodeString(s):
    if s.isalpha() or s == "":
        return s

    start_times = None
    end_times = None

    left = ''
    
    for i, c in enumerate(s):
        if c.isdigit() and start_times is None:
            start_times = i
        elif c == "[" and start_times is not None:
            end_times = i
            break
        else:
            if not c.isdigit():
                left += c

    times = int(s[start_times:end_times])
    # print('times', times)

    s = s[end_times:]

    stack = 0
    sub = ''
    end_sub = None
    for i, c in enumerate(s):
        if c == '[':
            stack += 1
        elif c == ']':
            stack -= 1
        sub += c
        if stack == 0:
            end_sub = i
            break
    right = s[end_sub+1:]

    # print("left", left)
    # print('sub', sub)
    # print('right', right)
    return left + times * decodeString(sub[1:-1]) + decodeString(right)
    

test(decodeString('a2[b10[c]]'), 'abccccccccccbcccccccccc',
     decodeString('4[ab]'), 'abababab',
     decodeString('z1[y]zzz2[abc]'), 'zyzzzabcabc',
     decodeString('b10[a]'), 'baaaaaaaaaa')
