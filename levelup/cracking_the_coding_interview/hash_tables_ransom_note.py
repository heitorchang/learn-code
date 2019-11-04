from collections import Counter

def ransom_note(magazine, ransom):
    m = Counter(magazine)
    r = Counter(ransom)
    return len((r-m).values()) == 0

def main():
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if(answer):
        print("Yes")
    else:
        print("No")

def test():
    testeql(ransom_note("ok one", "ok one"), True)
    testeql(ransom_note("ok one", "ok two"), False)
    testeql(ransom_note("apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg".split(), "elo lxkvg bg mwz clm w".split()), True) 
