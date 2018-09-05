from string import ascii_lowercase as az

def substitutionCipherDecryption(contents, signature, encryptedSignature):
    al = set(az)
    cab = al - set(encryptedSignature)
    cab = sorted(cab, reverse=True)
    ma = dict(zip(signature, encryptedSignature))
    
    ca = ""
    for p in az:
        if p in ma:
            ca += ma[p]
        else:
            ca += cab.pop()
    
    trtab = str.maketrans(ca, az)
    return contents.translate(trtab)
