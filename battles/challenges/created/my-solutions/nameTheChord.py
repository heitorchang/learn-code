description7 = """

You have carefully built an Arduino frequency analyzer and its first test will be "listening" to a music sample and deducing which [triad chord](https://en.wikipedia.org/wiki/Chord_(music)#Triads) was played.

**Note**: If you are familiar with music theory, please skip straight to the section **Your task**.

All notes of the chord were played in [twelve-tone equal temperament](https://en.wikipedia.org/wiki/Equal_temperament) with A4 (the note "La" above middle C or "Do" in octave 4) equal to `440 Hertz`.

The twelve notes of the C major scale, with flat notes marked with a lowercase `b`, are:

`C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B`

This cycle repeats endlessly, with `C` following `B`. The interval between any note and the nearest note of the same symbol (above or below) is called an **octave**. 

The interval between any two adjacent notes in the above list is one **semitone**. Since we are working with equal temperament, to determine the number of semitones between two notes, we simply count how many notes away they are. For example, the interval between `C` and `G` of the same octave is `7`.

A chord is a combination of more than one note played together that usually sounds pleasing or elicits other emotions from us. We will work with the triad (three-note) chords shown in the table below. We will not consider chord inversions or other variations.

The intervals (in semitones) of the two notes above the root are given. 

| Quality | Symbol | Semitones above root |
|--|--|--|
|major|*- none -*|4, 7|
|minor|m|3, 7|
|augmented|aug|4, 8|
|diminished|dim|3, 6|

The frequency of a note *n* semitones away from A4 is given by the formula

$f(n) = 440 * a^n$

where

$a = 2^{1/12}$

The frequency for a few notes above and below `A4` are, rounded to three decimal places:

|Note|Frequency|
|--|--|
|G|391.995|
|Ab|415.305|
|A|440.000|
|Bb|466.164|
|B|493.883|

__Your Task__

The Arduino reports the three frequencies (in Hertz) of the triad chord as an array of three floats. Because you are using analog sensors, there may be slight inaccuracies of at most 1 Hz. This array is the input to your function.

You should output the chord symbol represented by the notes, ignoring the octave of the root note. There are no chord inversions or variations.

Because in equal temperament there are equivalent ways of denoting the black keys of the piano, use the "flat" version of these notes, using a lowercase `b` (for example, output `Ab` and not `G#`).

Use the following symbols for the *quality* of the chord: none for major, `m` for minor, `aug` for augmented, and `dim` for diminished. 

__Examples__

For 
```
frequencies: [260.893, 330.221, 391.333]
```
you should output `C`. This is the C major chord with root `C4` and additional notes `E4` and `G4`. 

`E4` is 4 semitones above `C4`, and `G4` is 7 semitones above `C4`. According to the table above, this is a major chord.

(we ignore the octave in the output). The reported frequencies are imprecise; you should determine the closest note for each frequency.

For
```
frequencies: [220.020, 261.633, 330.30]
```
you should output `Am`. It's the A minor chord with root `A3`, `C4`, and `E4`. The intervals are 3 and 7.

For
```
frequencies: [554.001, 699.207, 879.534]
```
you should output `Dbaug`. This is the Db augmented chord with root `Db5`. We use `b` instead of `#` for the notes with black keys on a piano, and write `aug` for augmented chords.

For
```
frequencies: [233.888, 277.777, 330.003]
```
you should output `Bbdim`. It's the Bb diminished chord with root `Bb3`.

"""

constraints = """
The three frequencies detected by the Arduino unit.

*Guaranteed Constraints*
<code>frequencies.length = 3</code>
<code>110 <= frequencies[i] <= 3520</code>



The closest chord with the given frequencies, denoted by its root note and the corresponding symbol. Octaves should be ignored.
"""

import random 

def freq(n, base=440):
    a = 2 ** (1/12)
    return base * (a ** n)


def minIndex(target, arr):
    val, idx = min((abs(val - target), idx) for (idx, val) in enumerate(arr))
    return idx
    

def buildFreqToSyms():
    idxC2 = -33
    cycle = ["C",
             "Db",
             "D",
             "Eb",
             "E",
             "F",
             "Gb",
             "G",
             "Ab",
             "A",
             "Bb",
             "B"]
    out = {}
    for i in range(88):
        # out[round(freq(idxC2), 3)] = cycle[i % 12]
        out[i] = cycle[i % 12]
        idxC2 += 1
    return out

def buildFreqsArr():
    idxC2 = -33
    out = []
    for i in range(88):
        out.append(round(freq(idxC2), 3))
        idxC2 += 1
    return out

syms = buildFreqToSyms()
freqs = buildFreqsArr()

    
def noteNoise(pos):
    """Return the frequency plus noise of up to +/-1 Hz for the note
    in position pos."""

    return freqs[pos] + random.uniform(-3, 3)

    
def generateChord(type="", root=1):
    """Generate a chord of the given type"""
    second = 0
    third = 0
    if type == "":
        second = 4
        third = 7
    elif type == "m":
        second = 3
        third = 7
    elif type == "aug":
        second = 4
        third = 8
    elif type == "dim":
        second = 3
        third = 6
    else:
        raise ValueError("invalid type")

    freqs = []

    freqs.append(noteNoise(root))
    freqs.append(noteNoise(root+second))
    freqs.append(noteNoise(root+third))

    freqs = [round(n, 3) for n in freqs]

    print(syms[root] + type)
    return freqs


def triadChordsHz(fr):
    a, b, c = fr 
    if a <= 109 or c >= 3521:
        raise ValueError("freq out of range")
        
    root = minIndex(0, [u - a for u in freqs])
    second = minIndex(0, [u - b for u in freqs])
    third = minIndex(0, [u - c for u in freqs])

    rootSym = syms[root]

    print(rootSym, syms[second], syms[third])
    
    diff_notes = (second - root, third - root)

    qual = ""
    
    if diff_notes == (4, 7):
        qual = ""
    elif diff_notes == (3, 7):
        qual = "m"
    elif diff_notes == (4, 8):
        qual = "aug"
    elif diff_notes == (3, 6):
        qual = "dim"
    else:
        raise ValueError("unknown triad")

    return rootSym + qual
