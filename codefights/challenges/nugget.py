from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def chickenNuggetNumber(sizes):
    sizes.sort()
    a1 = sizes[0]
    a2 = sizes[1]
    a3 = sizes[2]

    a3_mod_a1 = a3 % a1

    print("a3%a1", a3_mod_a1)
    for i in range(a1):
        if (a2 * i) % a1 == a3_mod_a1:
            print("found s0")
            print(i)
            

def test():
    testeql(chickenNuggetNumber([6, 9, 20]), 43)
    testeql(chickenNuggetNumber([4, 6, 9]), 11)
    testeql(chickenNuggetNumber([2, 3, 3]), 11)
