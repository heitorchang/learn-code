description = """
You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:

    Put a single space between the words.
    Convert the uppercase letters to lowercase.

Example

    For s = "CodefightsIsAwesome", the output should be
    amendTheSentence(s) = "codefights is awesome";
    For s = "Hello", the output should be
    amendTheSentence(s) = "hello".

Input/Output

    [time limit] 4000ms (py3)

    [input] string s

    A string containing uppercase and lowercase English letters.

    Guaranteed constraints:

    3 ≤ s.length ≤ 100.

    [output] string

    The amended sentence.

"""

def test():
    testeql(amendTheSentence("CodefightsIsAwesome"), "codefights is awesome")
    testeql(amendTheSentence("iFvFAxtViLJDuWWXJesppOcLVdRAJZwBobdczkkWSPHzFLfyvmJYPdqYqRKKvLGYLwEFXcJiyYWLqjBvHjeqE"), "i fv f axt vi l j du w w x jespp oc l vd r a j zw bobdczkk w s p hz f lfyvm j y pdq yq r k kv l g y lw e f xc jiy y w lqj bv hjeq e")



    

def amendTheSentence(s):
    out = s[0].lower()
    for i in range(1, len(s)):
        c = s[i]
        if c.isupper():
            out += " " + c.lower()
        else:
            out += c
    return out
