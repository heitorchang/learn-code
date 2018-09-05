def test():
    testeql(rounders(1445), 2000)
    testeql(rounders(1234), 1000)
    testeql(rounders(90), 90)
    testeql(rounders(99), 100)
    testeql(rounders(85), 100)
    testeql(rounders(999), 1000)
    testeql(rounders(5), 10)

def rounders(value):
    # carry not done correctly, 100/300 only
    if value == 0:
        return 0
    lr = list(reversed(list(str(value))))
    print(lr)
    for i in range(len(lr)-1):
        if int(lr[i]) >= 5:
            lr[i+1] = str(int(lr[i+1]) + 1)
            carry = True
        else:
            carry = False
        lr[i] = 0
        
    if int(lr[-1]) >= 5:
        return 1 * 10 ** len(lr)
    else:
        res = ''.join(map(str, lr))
        res = res[::-1]
        return int(res)
