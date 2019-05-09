from itertools import groupby

def caolLeCaol(word):
    word = word.replace('á', 'a')
    word = word.replace('é', 'e')
    word = word.replace('í', 'i')
    word = word.replace('ó', 'o')
    word = word.replace('ú', 'u')
    
    consonants = "bcdfghjklmnpqrstvwxyz"
    
    shape = ""
    
    # replace consonants with C, Broad or Slender
    for c in word:
        if c in consonants:
            shape += "C"
        elif c == "a" or c == "o" or c == "u":
            shape += "B"
        elif c == "e" or c == "i":
            shape += "S"
        else:
            shape += "X"
            
    # collapse consonants
    shape = ''.join(k for k, g in groupby(shape))
    
    print(shape)
            
    if "BCS" in shape or "SCB" in shape:
        return False
    return True


pairtest(
    caolLeCaol("folús"), True,
    caolLeCaol("glacfidh"), False,
    caolLeCaol("tiocfaidh"), True,
    caolLeCaol("comhghairdeas"), True,
    caolLeCaol("úll"), True,
    caolLeCaol("páste"), False,
    caolLeCaol("ceapaire"), True,
    caolLeCaol("agus"), True,
    caolLeCaol("arán"), True,
    caolLeCaol("buachill"), False,

    caolLeCaol("an"), True,
    caolLeCaol("beanne"), False,
    caolLeCaol("leabhear"), False,
    caolLeCaol("conas"), True,
    caolLeCaol("daoibh"), True,
    caolLeCaol("muure"), False,
    caolLeCaol("ithum"), False,
    caolLeCaol("fáilte"), True,
    caolLeCaol("slán"), True,
    caolLeCaol("labhraím"), True,

    caolLeCaol("dóimaid"), False,
    caolLeCaol("nuachtán"), True,
    caolLeCaol("romhat"), True,
    caolLeCaol("abáicé"), True,
    caolLeCaol("abaico"), False,
    caolLeCaol("elimá"), False,
    caolLeCaol("nelíomáh"), True,
    caolLeCaol("uisce"), True,
    caolLeCaol("whisku"), False,
    caolLeCaol("againn"), True,    
)
