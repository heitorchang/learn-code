"""
Chinese characters offer few clues about how it's supposed to be pronounced, so various *romanization* schemes have been created for Westerners. The standard scheme for Mandarin is Hanyu Pinyin.

You are working on an educational website and have some texts to digitize. Your colleague is giving you phrases he scanned from a textbook, formatted as strings `pinyin;chinese characters`, where the two parts are separated by a semicolon.

Your task is to generate HTML markup that places the romanization for each character directly above the corresponding character. All characters produce a single syllable, and the input given to you already separated the Pinyin into syllables, with spaces in between. However, Mandarin is typically written entirely without spaces.

The desired output is (a single string without line breaks with a div with the "phrase" class enclosing all characters; use single quotes in the HTML):

```
<div class='phrase'><div class='character'>PINYIN_SYLLABLE<br>CHARACTER</div><div class='character'>PINYIN_SYLLABLE_2<br>CHARACTER_2</div>...</div>
```

Another colleague will deal with an appropriate CSS file.

__Example__

For `scanned: 'zuì jìn hǎo ma;最近好吗'`, you should output:

```
<div class='phrase'><div class='character'>最<br>zuì</div><div class='character'>近<br>jìn</div><div class='character'>好<br>hǎo</div><div class='character'>吗<br>ma</div></div>
```
"""

def chineseRomanization(scanned):
    characters = ""
    py, ch = scanned.split(";")
    for p, c in zip(py.split(" "), ch):
        characters += "<div class='character'>{}<br>{}</div>".format(p, c)
    return "<div class='phrase'>{}</div>".format(characters)
