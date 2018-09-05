from copy import copy
def theGunner(bullets, targets):
        level = 0
        t = sorted(targets, reverse=True)
        b = sorted(bullets, reverse = True)
        y = [x for x in t if x >0]
        while len(y):
               
                pr('y')
                
                b = copy(sorted(bullets, reverse=True))
                t = sorted(t, reverse =True)
                if max(t) == sum(t) and max(b)>= max(t):
                        level +=1
                        break
                
                i = 0
                # print 'round '+ str(level+1)
                # print 'b'
                # print b
                # print 't'
                pret =copy(t)
                preb = copy(b)
                preb2 = copy(b)
                # print t
                pr('preb')
                tocontinue = False
                for j in range(min(len(t), len(b))):
                        if len(b) and b[0] - t[j] <=0:
                                t[j] -= b.pop(0)
                        else:
                                tocontinue = True
               

                # print 't popped'
                # print t
                # print b
                lenpreb = len(preb)
                lent = len(t)
                
                if sum(preb) >= sum(t) and len(preb) >=len(t):
                        # print 'holla'
                        i = 0
                        res = []
                        res2 = []
                        # print 'pret'
                        # print pret
                        # print 'preb'
                        # print preb
                        while len(pret) > 0:
                                a = pret.pop()
                                # print 'a'
                                # print a
                                # print 'preb'
                                # print preb
                                for i in preb:
                                        if a-i in preb2:
                                                # print 'found it'
                                                res2.append(i)
                                                preb.remove(i)
                                                break
                        # print 'res2'
                        # print res2
                        if len(res2) == lent:
                                t = res2
                                level +=1
                                y = [x for x in t if x >0]
                                continue
                                
                                
                                                
                        
                        
                       
                        # print pret
                        # print preb
                        
                        
                if tocontinue:
                        while len(b):
                                x = sorted([[x,abs(b[0] - y)] for x,y in enumerate(t)], key = lambda x:x[1])
                                # print 'sorted mins'
                                # print x
                                first = x[0]

                                t[x[0][0]] -= b.pop(0)
                level +=1
                        
                y = [x for x in t if x >0]
                # print level
                # print t
        # print 'final level'
        return  level
        # print targets
        
        targets = [0,0,0]
    
def test():
    testeql(theGunner([9,5,9], [32,38,29]), 5)
    testeql(theGunner([9,4,4], [41,50,46]), 9)
