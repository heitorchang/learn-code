from collections import Counter

def verify_anagrams(first_word, second_word):
    cleanA = first_word.lower().replace(' ','')
    cleanB = second_word.lower().replace(' ','')
    ctrA = Counter(cleanA)
    ctrB = Counter(cleanB)
    return ctrA == ctrB

def verify_anagrams_top_answer(a,b):
    return sorted(a.lower().replace(' ','')) == sorted(b.lower().replace(' ',''))
    
def test():
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

