after_adding_tests = """
Your friend has built an Arduino frequency analyzer and asked you to help her with your coding skills. The device will "listen" to a music sample and your task is to deduce which [triad chord](https://en.wikipedia.org/wiki/Chord_(music)#Triads) was played.

**Note**: If you are familiar with music theory, please go straight to the section **Your task**.

All notes of the chord were played in [twelve-tone equal temperament](https://en.wikipedia.org/wiki/Equal_temperament) with A4 (the note "La" above middle C or "Do" in octave 4) equal to `440 Hertz`.

The twelve notes of the C major scale, with flat notes marked with a lowercase `b`, are:

`C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B`

Though it's technically acceptable, do not use `Fb` to represent `E`, or `Cb` to represent `B`, or a combination of several `b`s.

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

The Arduino reports the three frequencies (in Hertz) of the triad chord as an array of three floats. Because it uses analog sensors, there may be slight inaccuracies of at most &plusmn; 3 Hz. This array is the input to your function.

You should output the chord symbol represented by the notes, ignoring the octave of the root note. There are no chord inversions or variations.

In equal temperament there are equivalent ways of denoting the black keys of the piano. **Here, use the "flat" version of these notes, outputting a lowercase `b` (for example, output `Ab` and not `G#`)**.

Use the following symbols for the *quality* of the chord: none for major, `m` for minor, `aug` for augmented, and `dim` for diminished. 

__Examples__

For
```
frequencies: [394.678, 491.968, 588.13]
```
you should output `G`. This is the G major chord with root `G4` and additional notes `B4` and `D5`.

`B4` is 4 semitones above `G4`, and `D5` is 7 semitones above `G4`. According to the table above, this is a major chord. We ignore the chord root's octave in the output. 

Note that the reported frequencies are imprecise (for `G`, we observed 394.678 vs. the theoretical 391.995. You should determine the closest note for each frequency.

For 
```
frequencies: [260.893, 330.221, 391.333]
```
you should output `C`. This is the C major chord with root `C4` and additional notes `E4` and `G4`. 

For
```
frequencies: [220.020, 261.633, 330.30]
```
you should output `Am`. It's the A minor chord with root `A3`, `C4`, and `E4`. The intervals are 3 and 7.

For
```
frequencies: [554.001, 699.207, 879.534]
```
you should output `Dbaug`. This is the Db augmented chord with root `Db5`. We use `b` instead of `#` for the notes on a piano's black keys, and write `aug` for augmented chords. The notes are `Db`, `F`, and `A`.

For
```
frequencies: [233.888, 277.777, 330.003]
```
you should output `Bbdim`. It's the Bb diminished chord with root `Bb3`. The notes are `Bb`, `Db`, and `E`."""


constraints = """
The three frequencies detected by the Arduino unit.

*Guaranteed Constraints*
<code>frequencies.length = 3</code>
<code>110 <= frequencies[i] <= 3520</code>



The closest chord with the given frequencies, denoted by its root note and the corresponding symbol. Octaves should be ignored.
"""


def freq(n, base=440):
    a = 2 ** (1/12)
    return base * (a ** n)


def minIndex(target, arr):
    val, idx = min((abs(val - target), idx) for (idx, val) in enumerate(arr))
    return idx
    

def buildFreqToSyms():
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
