def applyEncoding(message, n):
    num_lines = n
    len_line = len(message) // num_lines
    pr('num_lines len_line')
    
    line_arr = []
    for i in range(num_lines):
        line_arr.append(message[i*len_line:(i+1)*len_line])
    pr('line_arr')

    result = ""
    for i in range(len(line_arr[0])):
        for j in range(n):
            result += line_arr[j][i]
    return result
                        
def caesarBoxCipherEncoding2(message):
    # did not pass
    total = 0
    for n in range(2, len(message)):
        try:
            c = applyEncoding(applyEncoding(message, n), n)
            pr('c')
            if c == message:
                total += 1
        except:
            pass
    return total
            

def test():
    testeql(caesarBoxCipherEncoding2("abbdbddb"), 2)
    testeql(caesarBoxCipherEncoding2("abaaba"), 0)
