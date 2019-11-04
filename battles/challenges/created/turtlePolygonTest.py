import sys
from turtle import fd, lt, rt

if __name__ == "__main__":

    test_cases = [
        ["fd(10)"],
        
         ["fd(60)", 
 "rt(90)", 
 "fd(40)", 
 "rt(90)", 
 "fd(40)", 
 "rt(90)", 
 "fd(60)"],

        ["lt(90)", 
 "fd(100)", 
 "rt(135)", 
 "fd(80)", 
 "lt(90)", 
 "fd(80)", 
 "rt(135)", 
 "fd(80)", 
 "rt(45)", 
 "fd(80)", 
 "rt(90)", 
 "fd(120)"]]
    
    cmds = test_cases[int(sys.argv[1])]
    
    for c in cmds:
        eval(c)

    print(cmds)
        
    dummy = input("Press Enter to quit.")
