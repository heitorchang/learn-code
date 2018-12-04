description = """
You're spending the night at your aunt's 300-year-old mansion which you're convinced is haunted. While in bed, the sibilant and shrill noises from around the house keep you awake. Are they really ghosts or just the wind?

You are recording the noises you hear as a sequence of low-pitched noises (represented by `o`) and high-pitched ones (represented by `u`). Each letter is one decisecond (one-tenth of a second) long. The wind blows wildly, but ghosts' wails follow a predictable pattern:

They begin with a non-zero length of low-pitched `o`s, then a non-zero length of high-pitched `u`s, followed by another length of low-pitched `o`s that **are of the same length as the initial sequence of `o`s**.

For example:

```
"ouo" = ghost
"oouuuuuoo" = ghost
"ouuooo" = wind
"uo" = wind
```

Given an uninterrupted sequence of noise, your task is to determine the maximal number of deciseconds out of the sequence that can be interpreted as ghost wails. **Ghost wails should not overlap.**

"""

from random import randrange

def generateWail(olen):
    """Generate a ghost's wail of o's length olen"""
    return 'o' * olen + randrange(1, olen) * 'u' + 'o' * olen

def generateWindA(olen):
    return 'o' * olen + randrange(1, olen) * 'u' + 'o' * (olen - randrange(1, olen))

def generateWindB(olen):
    return 'o' * (olen - randrange(1, olen)) + randrange(1, olen) * 'u' + 'o' * olen

def generateRandom(wlen):
    out = ''
    while len(out) < wlen:
        out += randrange(1, wlen // 3) * 'o'
        out += randrange(1, wlen // 3) * 'u'
    out += randrange(1, wlen // 3) * 'o'
    return out

def generateFalse(reps, avgLen, lensize):
    out = ''

def generateTrue(slen):
    out = ""
    while len(out) < slen:
        out += generateWail(randrange(3, 12))
    return out

def ghostOrWind(wail):
    return True


testcases = """
ouooouuuooo

ouooouuuoo
ooouuuooo

ouuuooouooo

ouuuo oouoo
ooouooo

ououooouooo

ouo ooouooo
ououooouooo

ooouooouo
ooouooo
oouoo ouo


ooouooouo

000100010

000100010

0001000

 00100 010

000100010



