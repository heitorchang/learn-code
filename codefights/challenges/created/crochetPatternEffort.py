description = """

You're taking a break from coding all day, and found some yarn, a hook, and a notebook with crochet patterns in the attic. 

After a [bit of Internet research](https://www.craftyarncouncil.com/standards/how-to-read-crochet-pattern), you learned that two basic crochet stitches are the **chain** and **single crochet**.

A chain loops the yarn forward in a line, while a single crochet expands the piece in the direction perpendicular to the chain.

A single crochet requires the hook to be inserted into a previously created loop (made either by a chain or single crochet), while a chain does not require inserting the hook into a loop.

Therefore, a chain may be made arbitrarily long, but a single crochet needs a loop in the previous row to accommodate it.

Stitching either a chain or a single crochet will add a single loop to the current row.

Based on some experiments, you estimate the amount of effort needed for each stitch as:

|Stitch|Abbreviation|Effort|
|-|-|-|
|Chain|ch|1|
|Single Crochet|sc|2|

In a pattern, a `ch` or `sc` instruction may have a number after it, indicating how many of that stitch you should make. If there's no number, it is simply `1` stitch.

There are additional instructions found in patterns:

**Increase** (abbreviated as `inc`) indicates that you do not advance a loop, instead, you add another single crochet (or more, if there's a number after `inc`) into the loop you are currently working on. If there is no number you should only add `1` extra **sc**, for a total of `2` **sc** in that loop.

**Skip** means that you should jump one or more loops and continue working on the next available loop. If there is no number after `skip`, you should skip `1` loop.

**Repeat** (abbreviated as `rep`) appears immediately after instructions enclosed in asterisks,`*`, and indicates how many times to repeat that group of instructions. Again, if there is no number after `rep`, repeat those instructions only once.

`inc`, `skip`, and `rep` take `0` effort. 

Before starting your first crochet project, you want to measure how much effort (in points) the whole project will require. You will work with two-dimensional patterns (roughly rectangular), which is built up row-by-row.

A pattern will be given to you as an **array of strings**, where each string represents a **row**. At the end of each row, you turn the piece around so that as you work, the row will always grow right-to-left (assuming you're right-handed).

Assume the pattern is well-formed. That is, for any given row, there will be no gaps or extra loops left over in the previous row (except for the initial chain).

__Examples__

For

```
pattern = [
" ",
" "]
```
, the output should be 0.


"""

def crochetPatternEffort(pattern):
    ch = 0
    sc = 0
    # work through rows increasing ch and sc counts

    return ch + 2 * sc
