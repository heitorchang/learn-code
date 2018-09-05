import unicodedata

def remove_accents(s):
    # https://stackoverflow.com/questions/15261793/
    # ... python-efficient-method-to-replace-accents-%C3%A9-to-e-remove-a-za-z-d-s-and
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    
def checkio(in_string):        
    return remove_accents(in_string)

    #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Préfèrent") == u"Preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
