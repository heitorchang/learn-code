description = """

Your grandma's birthday is coming up and you thought you'd make her a gift with your own hands to reciprocate the dozens of knitted sweaters and socks you received from her.

To change things a bit, you will [try crocheting](https://www.craftyarncouncil.com/standards/how-to-read-crochet-pattern) instead of knitting. 

The two basic crochet stitches you learned are called **chain** and **single crochet**. You will build your piece row-by-row. The first row is always made up of several chain stitches.

A chain stitch extends the current row forward, while a single crochet expands the piece in the perpendicular direction. Both will add a single loop to the current row.

A chain may be made arbitrarily long, but a single crochet needs a loop in the previous row to accommodate it.

You estimate the amount of effort needed for each stitch is:

|Stitch|Abbreviation|Effort|
|-|-|-|
|Chain|ch|1|
|Single Crochet|sc|2|

In a pattern, a `ch` or `sc` instruction may have a number after it indicating how many of that stitch you should make. If there's no number, it is simply `1` stitch.

There are additional instructions found in patterns:

**Increase** (abbreviated as `inc`) indicates that you do not advance a loop, instead, you add another single crochet (or more, if there's a number after `inc`) into the loop you are currently working on. If there is no number you should only add `1` extra **sc**, for a total of `2` **sc** in that loop.

**Skip** means that you should jump one or more loops and continue working on the next available loop. If there is no number after `skip`, you should skip `1` loop.

**Repeat** (abbreviated as `rep`) appears immediately after instructions enclosed in asterisks,`*`, and indicates how many times to repeat that group of instructions. Again, if there is no number after `rep`, repeat those instructions only once.

Only performing actual stitches take effort (following `inc`, `skip`, and `rep` instructions do not).

Before starting your crochet project, you want to measure how much effort (in points as shown above) the pattern will require.

The pattern will be given to you as an **array of strings**, where each string represents a **row**. At the end of each row, you turn the piece around so that as you work, the row will always grow right-to-left (assuming you're right-handed).

The given pattern will be well-formed. That is, for any given row, there will be no gaps or extra loops left over in the previous row (except for the initial chain).

__Examples__

For

```
pattern = [
" ",
" "]
```
, the output should be 0.


"""

def countRowEffort(r):
    pass

def crochetPatternEffort(pattern):
    ch = 0
    sc = 0
    # work through rows increasing ch and sc counts

    for row in pattern:
        pass
