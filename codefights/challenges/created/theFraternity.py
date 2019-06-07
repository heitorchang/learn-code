desc = """
**WARNING:** Long story. If you wish, skip straight to the section **Your Task**.

__Story__

For over a thousand years, a clan of weavers silently carries out executions to maintain balance in the world.

You have just joined this elite group, *The Fraternity*, and will receive your mission, containing a small rectangle of fabric.

The mechanized *Loom of Fate* produces such fabric that inexplicably contains multiple flaws--threads that miss the weave and end up on top or underneath where it should have been.

These flaws are actually the words of Fate, encoded as **binary 7-bit ASCII**. 

A group of **7 bits** form a letter from `A` to `Z` or underscore (`_`), and together, several characters form the name of the person you must assassinate.

Every member of the Fraternity must know how to decode the name given by the Loom. Show them that can you do it.

*[based on the 2008 movie "Wanted"]*

__Your Task__

A regular piece of fabric looks like this:

```
-|-|-|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|-|-|-
-|-|-|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|-|-|-
-|-|-|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|-|-|-
-|-|-|-|-|-|-|-|-|-|-|
|-|-|-|-|-|-|-|-|-|-|-
```

The piece of fabric you have been given contains at least two threads of *regular* fabric around its border.

Inside, there are multiple flaws that produce binary numbers, which you will convert to a person's name based on ASCII encoding.

A flaw may be a vertical thread (`|`) being on top of what should be a horizontal thread (`-`), or the other way around.

If a vertical thread is on top, record a `1` (one). Otherwise, record a `0` (zero).

You should proceed row-by-row and left-to-right within a row. 

Once **7 digits** have been recorded, it can be converted from binary to a character (`A` to `Z` or an underscore `_`) corresponding to its ASCII code. These numbers will always start with a `1` (one).

Repeat this procedure until you reach the end of your piece of fabric.

Finally, return the complete name you have decoded.

__Example__

`CROSS`

"""

"""
Idea: based on the first two characters of each line, determine parity and iterate, expected vs. seen. if they do not match, record "seen" character
"""
