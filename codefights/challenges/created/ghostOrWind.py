description = """
You're spending the night at your aunt's 300-year-old mansion which you're convinced is haunted. While in bed, the sibilant and shrill noises from around the house keep you awake. Are they really ghosts or just the wind?

You are recording the noises you hear as a sequence of low-pitched noises (represented by a lowercase `o`) and high-pitched ones (represented by an uppercase `U`). Each letter is one second long. The wind blows wildly, but ghosts' wails follow a predictable pattern:

They begin with a non-zero length of low-pitched `o`s, then a non-zero length of high-pitched `U`s, followed by another length of low-pitched `o`s that **are the same length as the initial sequence of `o`s**.

For example:

```
"oUo" = ghost
"ooUUUUUoo" = ghost
"oUUooo" = wind
"Uo" = wind
```

Given an uninterrupted sequence of noise, your task is to determine whether it can be divided into non-overlapping, contiguous subsequences that all follow the pattern of ghosts' wails. If so return `true`, otherwise, return `false`.

"""

from random import randrange

def generateWail(wlen):
    """Generate a ghost's wail of length wlen"""
    pass


def ghostOrWind(wail):
    return True

test(ghostOrWind("oOo"), True,
     ghostOrWind("ooOo"), False,
     ghostOrWind("Oo"), False,
     ghostOrWind("ooOOOoooOo"), True,
     ghostOrWind("oooOOOoooOOOooo"), False,
     ghostOrWind("ooOoooOooooOooo"), True)
