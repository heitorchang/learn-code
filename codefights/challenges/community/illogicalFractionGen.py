from math import isclose as i
from fractions import Fraction as F

def isi(n, d):
    m = set(str(n))
    e = set(str(d))

    C = m & e
    
    if C == m:
        return False
    
    def j(a):
        return "".join(c for c in a if c not in C)
    
    o = j(str(n))
    p = j(str(d))

    if o == "" or p == "":
        return False

    if p == "0" or d % 10 == 0 or d % 100 == 0 or d % 1000 == 0:
        return False

    try:
        f = F(int(o), int(p))
    except:
        return False
    k = float
    return len(C) > 0 and i(n/d, k(o) / k(p)) and f.numerator == int(o)

    
def illogicalFractionGen(upperLimit):
    out = []
    for n in range(10, upperLimit+1):
        # print("n:", n)
        for d in range(n+1, upperLimit+1):
            if isi(n, d):
                out.append("{}/{}".format(n, d))
    out.sort(key=lambda f: eval(f.split("/")[0] + "/" + f.split("/")[1]))
    print(out)
    return " ".join(out)

    thestring = '13/325 105/1806 115/1771 217/2914 205/2624 147/1848 248/2945 251/2259 295/2419 364/2639 139/973 217/1426 273/1729 127/762 19/95 199/995 273/1274 182/819 218/981 605/2662 637/2639 16/64 166/664 187/748 364/1365 436/1635 724/2715 187/682 371/1325 305/1037 187/583 145/435 546/1547 695/1946 604/1661 286/781 176/473 273/728 327/872 187/484 637/1638 26/65 266/665 275/671 728/1729 905/1991 637/1365 763/1635 928/1972 187/385 286/583 385/781 163/326 316/632 1365/2639 374/671 253/451 385/682 124/217 364/637 412/721 436/763 1204/2107 1324/2317 275/473 143/242 1443/2442 1456/2457 1083/1805 1547/2548 154/253 1554/2553 484/781 1638/2639 176/275 1776/2775 1150/1771 187/286 1887/2886 473/671 1365/1932 242/341 275/374 1275/1734 286/385 583/781 138/184 813/1084 1623/2164 1267/1629 2275/2925 352/451 385/484 148/185 473/572 484/583 572/671 583/682 2255/2624 682/781 2037/2328 1785/1974'

    thelist = thestring.split()

    ans = ""

    for f in thelist:
        parts = f.split("/")
        if int(parts[0]) <= upperLimit and int(parts[1]) <= upperLimit:
            ans += f + " "
    return ans.strip()
            
        
    


# test(illogicalFractionGen(714), None)

# test(isi(13, 325), True,
#      isi(101, 707), False)
