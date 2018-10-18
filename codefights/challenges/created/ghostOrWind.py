description = """

"oOo" = ghost
"ooOOOoo" = ghost
"oOOoo" = wind

If the uninterrupted wail can be divided into non-overlapping mini-wails such that they're all ghosts' wails, return `true`.

Otherwise, return `false`

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
