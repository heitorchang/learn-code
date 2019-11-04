def switchLights(a):
    for i in range(len(a)):
        if a[i] == 1:
            for j in range(i+1):
                if a[j] == 0:
                    a[j] = 1
                else:
                    a[j] = 0    
                    
    return a

def test():
    testeql(switchLights([1, 0, 0, 1, 0, 1, 0, 1]),[1, 1, 1, 0, 0, 1, 1, 0]) 
