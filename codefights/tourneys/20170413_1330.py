def revAll(words):
    sdrow = list(map(lambda w: w[::-1], words))
    return sdrow                 
        
def unusualLexOrder(words):
    sdrow = revAll(words)
    sdrow = sorted(sdrow)
    return revAll(sdrow)
    
def test():
    testeql(unusualLexOrder( ["nigeb", 
 "ta", 
 "eht", 
 "gninnigeb"]), 
["ta", 
 "nigeb", 
 "gninnigeb", 
 "eht"])
